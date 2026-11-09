# frozen_string_literal: true

# Static collection: never loads the application or executes its Ruby files.
require 'json'
require 'csv'
require 'set'
require 'ripper'
require 'digest'
require 'fileutils'
require 'open3'
require 'time'
require 'rubocop'

abort 'Usage: ruby scripts/collect_maintainability.rb SOURCE DECIDIM OUTPUT' unless ARGV.size == 3
SOURCE, CORE, OUTPUT = ARGV.map { |path| File.expand_path(path) }
abort 'RuboCop 1.86.2 is required' unless RuboCop::Version::STRING == '1.86.2'

def git(root, *args)
  out, err, status = Open3.capture3('git', '-c', "safe.directory=#{root}", '-C', root, *args)
  raise err unless status.success?
  out.strip
end

def tracked(root)
  git(root, 'ls-files', '-z').split("\0")
end

def parse(root, path)
  source = RuboCop::ProcessedSource.new(File.read(File.join(root, path)), 3.0, path)
  raise "Parse error: #{path}" unless source.valid_syntax?
  source
end

def const_name(node)
  return '' unless node
  return '::' if node.type == :cbase
  return nil unless node.type == :const
  prefix = const_name(node.children[0])
  return nil unless prefix
  prefix.empty? || prefix == '::' ? "#{prefix}#{node.children[1]}" : "#{prefix}::#{node.children[1]}"
end

def declarations(node, namespace = [], result = [])
  return result unless node.is_a?(RuboCop::AST::Node)
  if %i[class module].include?(node.type)
    name = const_name(node.children[0])
    raise "Unsupported dynamic class at #{node.first_line}" unless name
    full = name.start_with?('::') ? name.delete_prefix('::') : (namespace + [name]).join('::')
    result << { name: full, line: node.first_line } if node.class_type?
    declarations(node.children.last, [full], result)
  else
    node.child_nodes.each { |child| declarations(child, namespace, result) }
  end
  result
end

# Test support is also versioned under lib/ in this application.
def production_path?(path)
  path.match?(%r{\A(app|lib)/.*\.rb\z}) &&
    !path.match?(%r{/(test|spec|rspec_support|fixtures)/})
end

def lexical_namespaces(node)
  scopes = node.each_ancestor.select { |parent| %i[class module].include?(parent.type) }.reverse
  scopes.each_with_object([]) do |scope, names|
    name = const_name(scope.children.first)
    raise "Unsupported dynamic namespace at #{scope.first_line}" unless name
    names << if name.start_with?('::')
               name.delete_prefix('::')
             else
               [names.last, name].compact.join('::')
             end
  end.reverse
end

def described_class_name(group, known_classes)
  target = group.send_node.arguments.first
  return target.value if target&.str_type? && known_classes.include?(target.value)
  return unless target&.const_type?

  name = const_name(target)
  return unless name
  candidates = if name.start_with?('::')
                 [name.delete_prefix('::')]
               else
                 lexical_namespaces(group).map { |namespace| "#{namespace}::#{name}" } + [name]
               end
  candidates.find { |candidate| known_classes.include?(candidate) }
end

def pending_metadata?(call)
  call.arguments.any? do |arg|
    if arg.sym_type?
      %i[skip pending].include?(arg.value)
    elsif arg.hash_type?
      arg.pairs.any? do |pair|
        key = pair.key
        (key.sym_type? || key.str_type?) && %w[skip pending].include?(key.value.to_s) &&
          !pair.value.false_type? && !pair.value.nil_type?
      end
    end
  end
end

def active_example?(example)
  call = example.send_node
  return false unless %i[it specify example scenario fit fspecify fexample fscenario].include?(call.method_name)
  return false unless example.body
  return false if pending_metadata?(call)
  return false if example.each_ancestor(:block).any? do |parent|
    %i[xdescribe xcontext skip pending].include?(parent.send_node.method_name) || pending_metadata?(parent.send_node)
  end
  return false if example.each_descendant(:send).any? do |send|
    send.receiver.nil? && %i[skip pending].include?(send.method_name)
  end

  true
end

def file_class?(name, path)
  basename = name.split('::').last.gsub(/([A-Z]+)([A-Z][a-z])/, '\\1_\\2')
                 .gsub(/([a-z\d])([A-Z])/, '\\1_\\2').downcase
  File.basename(path, '.rb') == basename
end

def sloc(text)
  ignored = %i[on_sp on_ignored_sp on_nl on_ignored_nl on_comment on_embdoc_beg on_embdoc on_embdoc_end]
  lines = Set.new
  Ripper.lex(text).each do |position, kind, token, _state|
    next if ignored.include?(kind)
    token.lines.each_with_index do |line, offset|
      lines << position[0] + offset unless line.strip.empty?
    end
  end
  lines.size
end

def write_csv(name, rows, fields)
  CSV.open(File.join(OUTPUT, name), 'w') do |csv|
    csv << fields
    rows.each { |row| csv << fields.map { |field| row[field] } }
  end
end

[SOURCE, CORE].each do |root|
  raise "Dirty checkout: #{root}" unless git(root, 'status', '--porcelain').empty?
end
FileUtils.mkdir_p(OUTPUT)
source_paths = tracked(SOURCE)
production_paths = source_paths.select { |path| production_path?(path) }
sources = production_paths.to_h { |path| [path, parse(SOURCE, path)] }
source_declarations = sources.transform_values { |source| declarations(source.ast) }
known_classes = source_declarations.values.flatten.map { |entry| entry[:name] }.to_set
core_paths = tracked(CORE).select do |path|
  path.match?(%r{\Adecidim-[^/]+/}) && production_path?(path.split('/', 2).last)
end
core_classes = Hash.new { |hash, key| hash[key] = [] }
core_paths.each do |path|
  declarations(parse(CORE, path).ast).each { |entry| core_classes[entry[:name]] << path }
end

specs = source_paths.grep(%r{\Aspec/.*_spec\.rb\z})
# A literal describe of the class with at least one non-pending example is
# evidence of test presence, not proof that tests execute or assert behavior.
spec_index = Hash.new { |hash, key| hash[key] = [] }
active_specs = Set.new
class_subject_specs = Set.new
specs.each do |path|
  ast = parse(SOURCE, path).ast
  next unless ast
  ast.each_node(:block).each do |group|
    call = group.send_node
    next unless %i[describe context fdescribe fcontext].include?(call.method_name)
    next if pending_metadata?(call)
    next unless group.each_descendant(:block).any? { |example| active_example?(example) }

    name = described_class_name(group, known_classes)
    spec_index[name] << path if name
    class_subject_specs << path if name || call.arguments.first&.const_type?
    active_specs << path
  end
end

classes = []
methods = []
files = []
cop = RuboCop::Cop::Metrics::CyclomaticComplexity.new(RuboCop::ConfigLoader.default_configuration)
sources.each do |path, source|
  entries = source_declarations.fetch(path)
  entries.each do |entry|
    matches = core_classes[entry[:name]]
    override = path.start_with?('app/') && !matches.empty?
    mirrored = path.sub(%r{\Aapp/}, 'spec/').sub(/\.rb\z/, '_spec.rb')
    evidence = spec_index[entry[:name]].dup
    if file_class?(entry[:name], path) && active_specs.include?(mirrored) && !class_subject_specs.include?(mirrored)
      evidence << mirrored
    end
    classes << entry.merge(path: path, override: override, core: matches.join(';'),
                           specs: evidence.uniq.sort.join(';'))
  end
  if path.start_with?('app/') && !entries.empty?
    files << { path: path, classes: entries.map { |entry| entry[:name] }.join(';'), sloc: sloc(source.raw_source) }
  end
  next unless path.match?(%r{\Aapp/(commands|controllers|permissions|services)/}) && source.ast
  source.ast.each_node(:def, :defs).each do |node|
    cop.send(:reset_repeated_csend)
    complexity = node.body ? cop.send(:complexity, node.body) : 1
    methods << { path: path, line: node.first_line, method: node.method_name.to_s,
                 complexity: complexity, empty: node.body.nil? }
  end
  # Dynamic definitions would require an explicit extension of the protocol.
  if source.ast.each_node(:send).any? { |node| node.method_name == :define_method }
    raise "define_method requires manual review: #{path}"
  end
end

unique_classes = classes.map { |entry| entry[:name] }.uniq
overrides = classes.select { |entry| entry[:override] }.group_by { |entry| entry[:name] }
covered = overrides.count { |_name, entries| entries.any? { |entry| !entry[:specs].empty? } }
summary = {
  'M2.1' => { classes: unique_classes.size, overrides: overrides.size, percent: 100.0 * overrides.size / unique_classes.size },
  'M2.2' => { methods: methods.size, sum: methods.sum { |entry| entry[:complexity] },
             mean: methods.sum { |entry| entry[:complexity] }.fdiv(methods.size), maximum: methods.map { |entry| entry[:complexity] }.max },
  'M2.3' => { class_files: files.size, sloc: files.sum { |entry| entry[:sloc] },
             mean: files.sum { |entry| entry[:sloc] }.fdiv(files.size), maximum: files.map { |entry| entry[:sloc] }.max },
  'M2.4' => { overrides: overrides.size, with_spec: covered, percent: 100.0 * covered / overrides.size }
}
metadata = {
  collected_at: Time.now.getlocal('-03:00').iso8601,
  source_commit: git(SOURCE, 'rev-parse', 'HEAD'), core_commit: git(CORE, 'rev-parse', 'HEAD'),
  ruby: RUBY_DESCRIPTION, rubocop: RuboCop::Version::STRING,
  dependencies: Gem.loaded_specs.transform_values { |gem| gem.version.to_s },
  script_sha256: Digest::SHA256.file(__FILE__).hexdigest,
  scope: 'Unique named classes in tracked app/ and lib/ Ruby files; overrides are app/ classes also declared in Decidim 0.27.2 app/ or lib/.',
  exclusions: 'spec/, test/, db/, config/, vendor/, nested test/spec/rspec_support/fixtures directories and external gems; modules are not classes.',
  spec_rule: 'Literal describe/context resolved in lexical namespaces, or exact app-to-spec mirrored path for the class named by the file; requires a non-pending example; static evidence only.',
  sloc_rule: 'Ripper lexical nonblank code lines per app/ file containing a class; comments and embedded documentation excluded.',
  source_files: source_paths.grep(%r{\A(app|lib|spec)/.*\.rb\z}).to_h { |path| [path, Digest::SHA256.file(File.join(SOURCE, path)).hexdigest] }
}
write_csv('M2.1-classes.csv', classes, %i[path line name override core specs])
write_csv('M2.2-methods.csv', methods, %i[path line method complexity empty])
write_csv('M2.3-sloc.csv', files, %i[path classes sloc])
write_csv('M2.4-specs.csv', classes.select { |entry| entry[:override] }, %i[path name specs])
File.write(File.join(OUTPUT, 'summary.json'), JSON.pretty_generate(summary) + "\n")
File.write(File.join(OUTPUT, 'execution.json'), JSON.pretty_generate(metadata) + "\n")
puts JSON.pretty_generate(summary)
