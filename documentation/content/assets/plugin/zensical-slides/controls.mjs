import { getCurrentTranslations } from './i18n.mjs';
import { config } from './config.mjs';

export class ControlsUI {
	constructor(handlers = {}) {
		this.handlers = handlers;
		this.controlsEl = null;
		this.floatingBtn = null;
		this.progressBarEl = null;
		this.progressFillEl = null;
		this.totalSlides = 0;
	}

	ensureFloatingButton(onToggle) {
		const t = getCurrentTranslations();
		let btn = document.getElementById('pres-toggle-btn');
		if (!btn) {
			btn = document.createElement('button');
			btn.id = 'pres-toggle-btn';
			btn.innerHTML = t.toggleButton;
			btn.title = t.toggleTitle;
			btn.addEventListener('click', onToggle);
			document.body.appendChild(btn);
		} else {
			btn.innerHTML = t.toggleButton;
			btn.title = t.toggleTitle;
		}
		this.floatingBtn = btn;
		return btn;
	}

	ensureControls() {
		const t = getCurrentTranslations();
		let controls = document.getElementById('pres-controls');
		if (!controls) {
			controls = document.createElement('div');
			controls.id = 'pres-controls';
			controls.innerHTML =
				`<button id="pres-prev-btn" class="pres-nav-btn pres-left" title="${t.prevTitle}">&#8249;</button>` +
				`<button id="pres-next-btn" class="pres-nav-btn pres-right" title="${t.nextTitle}">&#8250;</button>` +
				'<div id="pres-bottom-bar">' +
				'<span id="pres-current-title"></span>' +
				'<div class="pres-right-actions">' +
				'<span id="pres-counter"></span>' +
				`<button id="pres-fullscreen-btn" title="${t.fullscreenTitle}">&#x26F6;</button>` +
				`<button id="pres-exit-btn" title="${t.exitTitle}">${t.exitButton}</button>` +
				'</div>' +
				'</div>';
			document.body.appendChild(controls);

			document.getElementById('pres-prev-btn')?.addEventListener('click', () => this.handlers.onPrev?.());
			document.getElementById('pres-next-btn')?.addEventListener('click', () => this.handlers.onNext?.());
			document.getElementById('pres-fullscreen-btn')?.addEventListener('click', () => this.handlers.onFullscreen?.());
			document.getElementById('pres-exit-btn')?.addEventListener('click', () => this.handlers.onExit?.());
		}

		const progressPosition = config?.progressBar ?? 'top';
		if (progressPosition !== 'none' && progressPosition !== false) {
			let progressContainer = document.getElementById('pres-progress-container');
			if (!progressContainer) {
				progressContainer = document.createElement('div');
				progressContainer.id = 'pres-progress-container';
				progressContainer.setAttribute('role', 'progressbar');
				progressContainer.setAttribute('aria-label', t.progressTitle);
				progressContainer.title = t.progressTitle;
				progressContainer.innerHTML = '<div id="pres-progress-fill"></div>';
				controls.appendChild(progressContainer);

				progressContainer.addEventListener('click', (e) => {
					if (!this.totalSlides) return;
					const rect = progressContainer.getBoundingClientRect();
					const clickX = e.clientX - rect.left;
					const fraction = Math.max(0, Math.min(1, clickX / rect.width));
					const targetIndex = Math.min(
						this.totalSlides - 1,
						Math.floor(fraction * this.totalSlides)
					);
					this.handlers.onGoTo?.(targetIndex);
				});
			} else {
				progressContainer.setAttribute('aria-label', t.progressTitle);
				progressContainer.title = t.progressTitle;
			}

			progressContainer.className = `pres-progress-${progressPosition}`;
			this.progressBarEl = progressContainer;
			this.progressFillEl = document.getElementById('pres-progress-fill');
		}

		this.controlsEl = controls;
		return controls;
	}

	show() {
		const controls = this.ensureControls();
		controls.style.display = 'block';
	}

	hide() {
		if (this.controlsEl) {
			this.controlsEl.style.display = 'none';
		}
	}

	update({ currentIndex, total, title, isFirst, isLast }) {
		this.totalSlides = total;
		const prevBtn = document.getElementById('pres-prev-btn');
		const nextBtn = document.getElementById('pres-next-btn');
		const counter = document.getElementById('pres-counter');
		const titleEl = document.getElementById('pres-current-title');

		if (prevBtn) {
			prevBtn.disabled = isFirst;
			prevBtn.style.opacity = isFirst ? '0.2' : '0.85';
		}

		if (nextBtn) {
			nextBtn.disabled = isLast;
			nextBtn.style.opacity = isLast ? '0.2' : '0.85';
		}

		if (counter) {
			counter.textContent = `${currentIndex + 1} / ${total}`;
		}

		if (titleEl) {
			titleEl.textContent = title || '';
		}

		if (this.progressFillEl && total > 0) {
			const percent = Math.min(100, Math.max(0, ((currentIndex + 1) / total) * 100));
			this.progressFillEl.style.width = `${percent}%`;
			this.progressBarEl?.setAttribute('aria-valuenow', String(currentIndex + 1));
			this.progressBarEl?.setAttribute('aria-valuemin', '1');
			this.progressBarEl?.setAttribute('aria-valuemax', String(total));
		}
	}
}
