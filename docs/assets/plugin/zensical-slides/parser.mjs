export const SlideParser = {
	parse(article) {
		if (!article) return [];

		const groups = [];
		let currentGroup = [];
		const children = Array.from(article.children);

		for (let i = 0; i < children.length; i++) {
			const el = children[i];
			if (el.id === 'pres-controls') continue;

			if (el.tagName === 'H2') {
				if (currentGroup.length > 0) {
					groups.push(currentGroup);
				}
				currentGroup = [el];
			} else {
				currentGroup.push(el);
			}
		}

		if (currentGroup.length > 0) {
			groups.push(currentGroup);
		}

		groups.forEach((group, gIdx) => {
			group.forEach(el => {
				el.setAttribute('data-pres-slide', String(gIdx));
			});
		});

		return groups.map((elements, index) => ({
			index,
			elements,
			title: this.extractTitle(elements)
		}));
	},

	extractTitle(elements) {
		const heading = elements.find(el => el.tagName === 'H2' || el.tagName === 'H1');
		return heading ? heading.textContent.replace('¶', '').trim() : '';
	}
};
