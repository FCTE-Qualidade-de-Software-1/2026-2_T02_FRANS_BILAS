export const MermaidIntegration = {
	init(retries = 25) {
		if (typeof mermaid !== 'undefined') {
			try {
				mermaid.initialize({
					startOnLoad: false,
					theme: 'default',
					securityLevel: 'loose',
					flowchart: { useMaxWidth: true, htmlLabels: true }
				});
				const nodes = document.querySelectorAll('.mermaid:not([data-processed="true"])');
				if (nodes.length > 0) {
					mermaid.run({ nodes });
				}
			} catch (err) {
				console.error('Mermaid render error:', err);
			}
		} else if (retries > 0) {
			setTimeout(() => this.init(retries - 1), 150);
		}
	}
};
