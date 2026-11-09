# frozen_string_literal: true

# Run independently of Rails and the database. This file belongs at
# spec/services/decidim/meetings/meeting_iframe_embedder_spec.rb in decidim-govbr.
require 'spec_helper'
require 'uri'
require 'active_support/core_ext/object/blank'
require_relative '../../../../app/services/decidim/meetings/meeting_iframe_embedder'

RSpec.describe Decidim::Meetings::MeetingIframeEmbedder do
  let(:request_host) { 'participacao.test' }

  describe '#embed_transformed_url' do
    {
      'https://www.youtube.com/watch?v=abc123' => 'https://www.youtube-nocookie.com/embed/abc123',
      'https://youtube.com/watch?v=first&v=second' => 'https://www.youtube-nocookie.com/embed/first',
      'https://youtube.com/watch?list=playlist&v=abc123&t=10' => 'https://www.youtube-nocookie.com/embed/abc123',
      'https://youtube.com/watch' => 'https://youtube.com/watch',
      'https://youtube.com/watch?list=playlist' => 'https://youtube.com/watch?list=playlist',
      'https://youtube.com/watch?v=' => 'https://youtube.com/watch?v=',
      'https://www.twitch.tv/videos/12345' => 'https://player.twitch.tv/?video=12345&parent=participacao.test',
      'https://twitch.tv/channel/12345' => 'https://twitch.tv/channel/12345',
      'https://twitch.tv/videos/' => 'https://twitch.tv/videos/',
      'https://example.test/video' => 'https://example.test/video'
    }.each do |input, expected|
      it "preserves the transformation contract for #{input}" do
        expect(described_class.new(input).embed_transformed_url(request_host)).to eq(expected)
      end
    end

    it 'returns nil for an empty URL' do
      expect(described_class.new('').embed_transformed_url(request_host)).to be_nil
    end

    it 'passes the request host to the Twitch parent parameter' do
      result = described_class.new('https://twitch.tv/videos/12345').embed_transformed_url('other.test')
      expect(result).to eq('https://player.twitch.tv/?video=12345&parent=other.test')
    end
  end

  describe '#embeddable?' do
    def configured_embedder(url)
      embedder = described_class.new(url)
      # The private accessor exists on the real service. Replacing only its
      # configuration keeps the project's verified partial doubles enabled.
      allow(embedder).to receive(:embeddable_services).and_return(['www.youtube.com', 'twitch.tv'])
      embedder
    end

    it 'normalizes www in the URL and configured hosts' do
      expect(configured_embedder('https://www.youtube.com/watch?v=abc').embeddable?).to be true
    end

    it 'accepts a configured host without www' do
      expect(configured_embedder('https://twitch.tv/videos/123').embeddable?).to be true
    end

    it 'rejects an unconfigured host' do
      expect(configured_embedder('https://example.test/video').embeddable?).to be false
    end

    it 'does not match a host that only contains an allowed domain' do
      expect(configured_embedder('https://youtube.com.example.test/video').embeddable?).to be false
    end

    it 'returns nil for an empty URL' do
      expect(configured_embedder('').embeddable?).to be_nil
    end
  end

  describe '#embed_code' do
    it 'returns nil for an empty URL' do
      expect(described_class.new('').embed_code(request_host)).to be_nil
    end

    it 'keeps the iframe disabled as in the evaluated version' do
      html = described_class.new('https://youtube.com/watch?v=abc').embed_code(request_host)
      visible_html = html.gsub(/<!--.*?-->/m, '')
      expect(visible_html).to include('class="disabled-iframe"')
      expect(visible_html).not_to include('<iframe')
    end

    it 'keeps the transformed URL in the commented template' do
      html = described_class.new('https://youtube.com/watch?v=abc').embed_code(request_host)
      expect(html).to include('src="https://www.youtube-nocookie.com/embed/abc"')
    end
  end
end
