class TooltipBubble extends HTMLElement {
    static observedAttributes = ["description"];

    constructor() {
        super();
    }

    connectedCallback() {
        this.render();
    }

    attributeChangedCallback(name, oldValue, newValue) {
        this[name] = newValue;
        this.render();
    }

    attachToggleListener() {
        this.querySelectorAll(".tooltip-container").forEach((container) => {
            const iconWrapper = container.querySelector(".icon-wrapper");
            const tooltipBubble = container.querySelector(".tooltip-bubble");

            // Hover state
            iconWrapper.addEventListener("mouseenter", (e) => {
                this.attachDirection(tooltipBubble);
                tooltipBubble.classList.add("show");
            });
            iconWrapper.addEventListener("mouseleave", (e) => {
                tooltipBubble.classList.remove("show");
            });
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
          <div class="tooltip">${this.getAttribute("description")}</div>
          <div class="indicator">
            <svg xmlns="http://www.w3.org/2000/svg" width="30" height="20" viewBox="0 0 10 8" fill="none">
              <path d="M5.86604 7.5C5.48114 8.16667 4.51889 8.16667 4.13399 7.5L0.669889 1.5C0.284989 0.833333 0.766115 -8.24401e-07 1.53592 -7.57103e-07L8.46412 -1.51421e-07C9.23392 -8.41226e-08 9.71504 0.833333 9.33014 1.5L5.86604 7.5Z" fill="#F2F2F2"/>
            </svg>
          </div>
        </div>
      </div>
    `;
        this.attachToggleListener();
    }
}

customElements.define("web-tooltip", TooltipBubble);
