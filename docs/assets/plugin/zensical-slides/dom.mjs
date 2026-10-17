export const DOMUtils = {
	getArticleContent() {
		return (
			document.querySelector('article.md-content__inner') ||
			document.querySelector('.md-content__inner') ||
			document.querySelector('article')
		);
	},

	isInputElement(target) {
		if (!target || !target.tagName) return false;
		const tag = target.tagName.toUpperCase();
		return tag === 'INPUT' || tag === 'TEXTAREA' || tag === 'SELECT' || target.isContentEditable;
	}
};
