export class PSModal extends HTMLElement {
    static observedAttributes = [
        "confirm-label",
        "link",
        "theme",
        "question",
        "message",
        "icon",
        "confirm-data-name",
    ];

    constructor() {
        super();
    }

    connectedCallback() {
        this.render();
        this._onKeydown = (e) => {
            if (this.style.display !== "block") return;
            if (e.key === "Escape") {
                this.style.display = "none";
                return;
            }
            if (e.key === "Tab") {
                const focusable = [
                    ...this.querySelectorAll(
                        'button:not([disabled]), [href], input:not([disabled]), [tabindex]:not([tabindex="-1"])',
                    ),
                ];
                if (!focusable.length) return;
                const first = focusable[0];
                const last = focusable[focusable.length - 1];
                if (e.shiftKey) {
                    if (document.activeElement === first) {
                        e.preventDefault();
                        last.focus();
                    }
                } else {
                    if (document.activeElement === last) {
                        e.preventDefault();
                        first.focus();
                    }
                }
            }
        };
        document.addEventListener("keydown", this._onKeydown);
    }

    disconnectedCallback() {
        document.removeEventListener("keydown", this._onKeydown);
    }

    attributeChangedCallback(name, oldValue, newValue) {
        this[name] = newValue;
        this.render();
    }

    attachListeners() {
        this.querySelector("#confirm-yes").onclick = () => {
            this.style.display = "none";
            this.dispatchEvent(new CustomEvent("confirm-yes-clicked", { bubbles: true }));
        };
        this.querySelector("#confirm-no").onclick = () => {
            this.style.display = "none";
        };
        this.querySelector(".modal-underlay").onclick = () => {
            this.style.display = "none";
        };
    }

    render() {
        let accentColor = "var(--copy)";
        const theme = this.getAttribute("theme");
        if (theme === "Success") accentColor = "rgb(var(--success))";
        else if (theme === "Error") accentColor = "rgb(var(--error))";
        else if (theme === "Warning") accentColor = "rgb(var(--warning))";

        this.innerHTML = `
            <div id="confirm-modal"
                role="dialog"
                aria-modal="true"
                aria-labelledby="confirm-question">
                <div class="modal-underlay"></div>
                <div class="modal-content" style="border-color:${accentColor}">
                    <i style="width: 2rem; height: 2rem; color: ${accentColor}" data-lucide="alert-triangle"></i>
                    <h4 id="confirm-question">${this.getAttribute("question")}</h4>
                    ${this.getAttribute("message") ? this.getAttribute("message") : ""}
                    <div class="save-cancel">
                        <ps-button type="button" id="confirm-no" label="Cancel" theme="Shadow" righticon="x"></ps-button>
                        <ps-button
                            id="confirm-yes"
                            ${
                                this.getAttribute("icon")
                                    ? `righticon=${this.getAttribute("icon")}`
                                    : ""
                            }
                            ${this.getAttribute("link") ? `link=${this.getAttribute("link")}` : ""}
                            label=${this.getAttribute("confirm-label")}
                            theme=${this.getAttribute("theme")}
                        ></ps-button>
                    </div>
                </div>
            </div>
        `;
        this.attachListeners();
    }
}

customElements.define("ps-modal", PSModal);
