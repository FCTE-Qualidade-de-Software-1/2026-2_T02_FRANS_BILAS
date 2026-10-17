/**
 * Zensical Slides - Entry point
 */
import { PresentationController } from './controller.mjs';

const controller = new PresentationController();

function setup() {
	controller.init();
}

if (window.document$) {
	window.document$.subscribe(setup);
} else if (document.readyState === 'loading') {
	document.addEventListener('DOMContentLoaded', setup);
} else {
	setup();
}

window.ZensicalSlides = controller;
export default controller;