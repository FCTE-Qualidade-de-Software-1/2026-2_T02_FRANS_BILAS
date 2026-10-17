export class SlideDeck {
	constructor() {
		this.slides = [];
		this.currentIndex = 0;
		this.active = false;
	}

	setSlides(slides) {
		this.slides = slides || [];
		this.currentIndex = 0;
	}

	get count() {
		return this.slides.length;
	}

	get currentSlide() {
		return this.slides[this.currentIndex] || null;
	}

	get isFirst() {
		return this.currentIndex === 0;
	}

	get isLast() {
		return this.currentIndex >= this.count - 1;
	}

	show(index, article) {
		if (this.count === 0) return null;
		this.currentIndex = Math.max(0, Math.min(this.count - 1, index));

		if (!article) return this.currentSlide;

		const children = Array.from(article.children);
		children.forEach(el => {
			if (el.id === 'pres-controls') return;
			const slideAttr = el.getAttribute('data-pres-slide');
			if (slideAttr === null) return;

			if (this.active) {
				el.style.display = slideAttr === String(this.currentIndex) ? '' : 'none';
			} else {
				el.style.display = '';
			}
		});

		window.scrollTo({ top: 0, behavior: 'instant' });
		return this.currentSlide;
	}

	reset(article) {
		if (!article) return;
		const children = Array.from(article.children);
		children.forEach(el => {
			if (el.id !== 'pres-controls') {
				el.style.display = '';
			}
		});
	}
}
