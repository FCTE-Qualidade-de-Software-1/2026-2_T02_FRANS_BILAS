import { DOMUtils } from './dom.mjs';

export class KeyboardNavigator {
	constructor(controller) {
		this.controller = controller;
		this.onKeyDown = this.handleKeyDown.bind(this);
	}

	bind() {
		document.addEventListener('keydown', this.onKeyDown);
	}

	unbind() {
		document.removeEventListener('keydown', this.onKeyDown);
	}

	handleKeyDown(e) {
		if (DOMUtils.isInputElement(e.target)) return;

		if (e.key === 'p' || e.key === 'P') {
			if (!e.ctrlKey && !e.metaKey && !e.altKey) {
				this.controller.toggle();
				e.preventDefault();
				return;
			}
		}

		if (!this.controller.isActive) return;

		if (e.key === 'ArrowRight' || e.key === 'PageDown' || e.key === ' ') {
			this.controller.next();
			e.preventDefault();
		} else if (e.key === 'ArrowLeft' || e.key === 'PageUp') {
			this.controller.prev();
			e.preventDefault();
		} else if (e.key === 'Escape') {
			this.controller.exit();
			e.preventDefault();
		} else if (e.key === 'f' || e.key === 'F') {
			this.controller.toggleFullscreen();
			e.preventDefault();
		}
	}
}
