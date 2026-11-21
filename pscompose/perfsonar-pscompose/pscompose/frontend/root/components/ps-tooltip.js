class TooltipBubble extends HTMLElement {
    static observedAttributes = ["desc"];

    constructor() {
        super();
        this._enterHandlers = [];
        this._leaveHandlers = [];
    }

    connectedCallback() {
        this.render();
        lucide.createIcons();
    }

    disconnectedCallback() {
        this._cleanupListeners();
    }

    attributeChangedCallback(name, oldValue, newValue) {
        this[name] = newValue;
        this._cleanupListeners();
        this.render();
        lucide.createIcons();
    }

    _cleanupListeners() {
        this.querySelectorAll(".tooltip-container").forEach((container, i) => {
            const iconWrapper = container.querySelector(".icon-wrapper");
            if (iconWrapper && this._enterHandlers[i]) {
                iconWrapper.removeEventListener("mouseenter", this._enterHandlers[i]);
                iconWrapper.removeEventListener("mouseleave", this._leaveHandlers[i]);
            }
        });
        this._enterHandlers = [];
        this._leaveHandlers = [];
    }

    attachToggleListener() {
        this.querySelectorAll(".tooltip-container").forEach((container, i) => {
            const iconWrapper = container.querySelector(".icon-wrapper");
            const tooltipBubble = container.querySelector(".tooltip-bubble");

            const onEnter = () => {
                this.attachDirection(tooltipBubble);
                tooltipBubble.classList.add("show");
            };
            const onLeave = () => {
                tooltipBubble.classList.remove("show");
            };

            this._enterHandlers[i] = onEnter;
            this._leaveHandlers[i] = onLeave;

            iconWrapper.addEventListener("mouseenter", onEnter);
            iconWrapper.addEventListener("mouseleave", onLeave);
        });
    }

    attachDirection(tooltipBubble) {
        const rect = this.getBoundingClientRect();
        const screenWidth = window.innerWidth;
        const tooltip = tooltipBubble.querySelector(".tooltip");
        if (rect.left > screenWidth / 2) {
            tooltip.classList.add("right");
        } else {
            tooltip.classList.add("left");
        }
    }

    render() {
        this.innerHTML = `
        <div class="tooltip-container" style="display: flex; align-items: center;">
            <div class="icon-wrapper"><i class="info-icon" data-lucide="info"></i></div>
            <div class="tooltip-bubble">
                <div class="tooltip">${this.getAttribute("desc")}</div>
                <div class="indicator">
                    <svg xmlns="http://www.w3.org/2000/svg" width="30" height="20" viewBox="0 0 10 8">
                    <path d="M5.86604 7.5C5.48114 8.16667 4.51889 8.16667 4.13399 7.5L0.669889 1.5C0.284989 0.833333 0.766115 -8.24401e-07 1.53592 -7.57103e-07L8.46412 -1.51421e-07C9.23392 -8.41226e-08 9.71504 0.833333 9.33014 1.5L5.86604 7.5Z"/>
                    </svg>
                </div>
            </div>
        </div>
    `;
        this.attachToggleListener();
    }
}

customElements.define("ps-tooltip", TooltipBubble);
