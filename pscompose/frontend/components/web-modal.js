export class WebModal extends HTMLElement {
    static observedAttributes = ["confirm-label", "link", "theme", "question", "message", "icon"];

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

    attachListeners() {
        // yes
        this.querySelector("#confirm-yes").onclick = () => {
            this.style.display = "none";
            this.dispatchEvent(new CustomEvent("confirm-yes-clicked", { bubbles: true }));
        };

        // escape
        this.querySelector("#confirm-no").onclick = () => {
            this.style.display = "none";  // Hide current modal instance
        };
        this.querySelector(".modal-underlay").onclick = () => {
            this.style.display = "none";  // Hide current modal instance
        };
    }

    render() {
        let accentColor = "var(--copy-color)";
        if (this.getAttribute("theme")) {
            if (this.getAttribute("theme") == "Success") {
                accentColor = "var(--success-color)";
            }
            if (this.getAttribute("theme") == "Error") {
                accentColor = "var(--error-color)";
            }
            if (this.getAttribute("theme") == "Warning") {
                accentColor = "var(--warning-color)";
            }
        }

        this.innerHTML = `
            <div id="confirm-modal">
                <div class="modal-underlay"></div>

                <div class="modal-content" style="border-color:${accentColor}" >
                    <i style="width: 2rem; height: 2rem; color: ${accentColor}" data-lucide="alert-triangle">
                    </i>
                    <h4 id="confirm-question">${this.getAttribute("question")}</h4>
                    ${this.getAttribute("message") ? this.getAttribute("message") : ""}
                    <p id="confirm-find"></p>
                    <div class="save-cancel">
                        <web-button 
                            type="button" 
                            id="confirm-no" 
                            data-label="Cancel" 
                            data-theme="Shadow" 
                            data-righticon="x" 
                        ></web-button>
                        <web-button
                            id="confirm-yes"
                            ${
                                this.getAttribute("icon")
                                    ? `data-righticon=${this.getAttribute("icon")}`
                                    : ""
                            }
                            ${this.getAttribute("link") ? `link=${this.getAttribute("link")}` : ""}
                            ${this.getAttribute("hxAttr") ? `${this.getAttribute("hxAttr")}` : ""}
                            data-label=${this.getAttribute("confirm-label")}
                            data-theme=${this.getAttribute("theme")}
                        ></web-button>
                    </div>
                </div>
            </div>
        `;
        this.attachListeners();
    }
}

customElements.define("web-modal", WebModal);
