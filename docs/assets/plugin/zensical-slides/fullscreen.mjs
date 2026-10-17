export const FullscreenManager = {
	isFullscreen() {
		return Boolean(document.fullscreenElement);
	},

	toggle() {
		if (!document.fullscreenElement) {
			document.documentElement.requestFullscreen().catch(() => {});
		} else if (document.exitFullscreen) {
			document.exitFullscreen().catch(() => {});
		}
	}
};
