import { config } from './config.mjs';

export const TRANSLATIONS = {
	en: {
		toggleButton: '&#9654; Show',
		toggleTitle: 'Enter presentation mode (P)',
		prevTitle: 'Previous slide (Left arrow)',
		nextTitle: 'Next slide (Right arrow)',
		fullscreenTitle: 'Fullscreen',
		exitButton: '&#10005; Exit',
		exitTitle: 'Exit presentation (Esc)',
		progressTitle: 'Jump to slide'
	},
	ja: {
		toggleButton: '&#9654; スライド',
		toggleTitle: 'プレゼンテーションモードを開始 (Pキー)',
		prevTitle: '前のスライド (左矢印)',
		nextTitle: '次のスライド (右矢印)',
		fullscreenTitle: '全画面表示',
		exitButton: '&#10005; 終了',
		exitTitle: 'プレゼンテーションを終了 (Esc)',
		progressTitle: 'スライドに移動'
	},
	pt: {
		toggleButton: '&#9654; Apresentar',
		toggleTitle: 'Entrar no modo apresentação (tecla P)',
		prevTitle: 'Slide anterior (Seta esquerda)',
		nextTitle: 'Próximo slide (Seta direita)',
		fullscreenTitle: 'Tela cheia',
		exitButton: '&#10005; Sair',
		exitTitle: 'Sair da apresentação (Esc)',
		progressTitle: 'Ir para o slide'
	}
};

export function resolveLanguage(lang) {
	if (!lang || typeof lang !== 'string') return 'en';
	const normalized = lang.trim().toLowerCase().split(/[-_]/)[0];
	if (normalized === 'ja') return 'ja';
	if (normalized === 'pt') return 'pt';
	return 'en';
}

export function getTranslations(lang) {
	const resolved = resolveLanguage(lang);
	return TRANSLATIONS[resolved] || TRANSLATIONS.en;
}

export function getCurrentTranslations() {
	const docLang =
		typeof document !== 'undefined' && document.documentElement
			? document.documentElement.lang
			: null;
	const lang = docLang || config?.language;
	return getTranslations(lang);
}
