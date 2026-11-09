# frozen_string_literal: true

require 'tmpdir'
require 'fileutils'
require 'open3'
require 'json'
require 'rbconfig'

RSpec.describe 'Static maintainability collector' do
  let(:collector) { File.expand_path('../collect_maintainability.rb', __dir__) }

  def command(*args)
    stdout, stderr, status = Open3.capture3(*args)
    raise "#{args.inspect}: #{stderr}" unless status.success?
    stdout
  end

  def repository(path, files)
    FileUtils.mkdir_p(path)
    command('git', 'init', '-q', path)
    files.each do |name, source|
      target = File.join(path, name)
      FileUtils.mkdir_p(File.dirname(target))
      File.write(target, source)
    end
    command('git', '-C', path, 'add', '.')
    command('git', '-C', path, '-c', 'user.name=Fixture', '-c', 'user.email=fixture@example.test',
            '-c', 'core.hooksPath=/dev/null', 'commit', '-qm', 'Synthetic fixture')
  end

  def collect(spec_source, dirty: false, spec_path: 'spec/services/decidim/existing_spec.rb',
              extra_source: {}, extra_core: {})
    Dir.mktmpdir('maintainability-spec') do |tmp|
      source = File.join(tmp, 'source')
      core = File.join(tmp, 'core')
      output = File.join(tmp, 'output')
      repository(source, {
        'app/services/decidim/existing.rb' => <<~RUBY,
          # A comment is not a code line.
          module Decidim
            class Existing
              def choose(value)
                value ? 1 : 2 # inline comment
              end
              def empty; end
            end
            class Added
            end
          end
        RUBY
        'lib/helper.rb' => "class Helper; end\n",
        'db/migrate/001_fake.rb' => "class Migration; end\n",
        spec_path => spec_source
      }.merge(extra_source))
      repository(core, { 'decidim-core/app/services/decidim/existing.rb' => "module Decidim; class Existing; end; end\n" }.merge(extra_core))
      File.write(File.join(source, 'lib/helper.rb'), "class Changed; end\n") if dirty
      stdout, stderr, status = Open3.capture3(RbConfig.ruby, collector, source, core, output)
      yield(status, stdout, stderr, output)
    end
  end

  it 'counts actual upstream classes, all methods and lexical code lines' do
    collect("RSpec.describe Decidim::Existing do\n  it('works') { expect(true).to eq(true) }\nend\n") do |status, _stdout, stderr, output|
      expect(status.success?).to be(true), stderr
      result = JSON.parse(File.read(File.join(output, 'summary.json')))
      expect(result['M2.1']).to include('classes' => 3, 'overrides' => 1)
      expect(result['M2.2']).to include('methods' => 2, 'sum' => 3, 'mean' => 1.5)
      expect(result['M2.3']).to include('class_files' => 1, 'sloc' => 10)
      expect(result['M2.4']).to include('with_spec' => 1, 'percent' => 100.0)
    end
  end

  it 'accepts a mirrored spec with a descriptive string' do
    collect("describe 'existing service' do\n  it('works') { expect(true).to eq(true) }\nend\n") do |status, _stdout, stderr, output|
      expect(status.success?).to be(true), stderr
      expect(JSON.parse(File.read(File.join(output, 'summary.json')))['M2.4']['with_spec']).to eq(1)
    end
  end

  it 'does not count examples inside a disabled group' do
    collect("describe Decidim::Existing do\n xcontext 'disabled' do\n it('pending') { expect(true).to eq(true) }\n end\nend\n") do |status, _stdout, stderr, output|
      expect(status.success?).to be(true), stderr
      expect(JSON.parse(File.read(File.join(output, 'summary.json')))['M2.4']['with_spec']).to eq(0)
    end
  end

  it 'excludes test support even when it lives below lib/' do
    collect("describe Decidim::Existing do; it('works') { true }; end\n",
            extra_source: { 'lib/decidim/dev/test/rspec_support/provider.rb' => "class TestProvider; end\n" }) do |status, _stdout, stderr, output|
      expect(status.success?).to be(true), stderr
      expect(JSON.parse(File.read(File.join(output, 'summary.json')))['M2.1']['classes']).to eq(3)
    end
  end

  it 'resolves class descriptions inside lexical modules without a mirrored path' do
    collect("module Decidim; describe Existing do; it('works') { true }; end; end\n",
            spec_path: 'spec/requests/service_spec.rb') do |status, _stdout, stderr, output|
      expect(status.success?).to be(true), stderr
      expect(JSON.parse(File.read(File.join(output, 'summary.json')))['M2.4']['with_spec']).to eq(1)
    end
  end

  it 'keeps absolute descriptions absolute inside a different module' do
    collect("module Other; describe ::Decidim::Existing do; it('works') { true }; end; end\n",
            spec_path: 'spec/requests/service_spec.rb') do |status, _stdout, stderr, output|
      expect(status.success?).to be(true), stderr
      expect(JSON.parse(File.read(File.join(output, 'summary.json')))['M2.4']['with_spec']).to eq(1)
    end
  end

  it 'does not give a mirrored spec to other classes declared in the same file' do
    collect("describe 'existing service' do; it('works') { true }; end\n",
            extra_core: { 'decidim-core/app/services/decidim/added.rb' => "module Decidim; class Added; end; end\n" }) do |status, _stdout, stderr, output|
      expect(status.success?).to be(true), stderr
      expect(JSON.parse(File.read(File.join(output, 'summary.json')))['M2.4']).to include('overrides' => 2, 'with_spec' => 1)
    end
  end

  it 'does not let a mirrored path override a description of another class' do
    collect("describe Decidim::Added do; it('works') { true }; end\n") do |status, _stdout, stderr, output|
      expect(status.success?).to be(true), stderr
      expect(JSON.parse(File.read(File.join(output, 'summary.json')))['M2.4']['with_spec']).to eq(0)
    end
  end

  ["skip: 'not implemented'", ':pending'].each do |metadata|
    it "excludes examples marked with #{metadata}" do
      collect("describe Decidim::Existing do; it('works', #{metadata}) { true }; end\n") do |status, _stdout, stderr, output|
        expect(status.success?).to be(true), stderr
        expect(JSON.parse(File.read(File.join(output, 'summary.json')))['M2.4']['with_spec']).to eq(0)
      end
    end
  end

  it 'rejects modified input rather than attributing it to a clean commit' do
    collect("describe 'unused' do; end\n", dirty: true) do |status, _stdout, stderr, _output|
      expect(status.success?).to be false
      expect(stderr).to include('Dirty checkout')
    end
  end
end
