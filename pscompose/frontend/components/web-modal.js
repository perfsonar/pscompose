export class WebModal extends HTMLElement {
    static observedAttributes = ["confirm-label", "link", "theme", "question", "message", "icon", "confirm-data-name"];

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
        let accentColor = "var(--copy)";
        if (this.getAttribute("theme")) {
            if (this.getAttribute("theme") == "Success") {
                accentColor = "rgb(var(--success))";
            }
            if (this.getAttribute("theme") == "Error") {
                accentColor = "rgb(var(--error))";
            }
            if (this.getAttribute("theme") == "Warning") {
                accentColor = "rgb(var(--warning))";
            }
        }

        this.innerHTML = `
            <div id="confirm-modal">
                <div class="modal-underlay"></div>

                <div class="modal-content" style="border-color:${accentColor}" >
                    <i style="width: 2rem; height: 2rem; color: ${accentColor}" data-lucide="alert-triangle">
                    </i>
                    <h4 id="confirm-question">${this.getAttribute("question")}</h4>
                    <div class="data-box">
                        <i
                            data-lucide="${ psCompose.activeRoute.icon }"
                            class="shortcut-icon"
                            aria-hidden="true"
                        ></i>
                        <div class="data-info">
                            <span>${ psCompose.activeRoute.singular }</span>
                            <h5>${this.getAttribute("confirm-data-name") || ""}</h5>
                        </div>
                    </div>
                    <br/>
                    ${this.getAttribute("message") ? this.getAttribute("message") : ""}
                    <div class="save-cancel">
                        <web-button 
                            type="button" 
                            id="confirm-no" 
                            label="Cancel" 
                            theme="Shadow" 
                            righticon="x" 
                        ></web-button>
                        <web-button
                            id="confirm-yes"
                            ${
                                this.getAttribute("icon")
                                    ? `righticon=${this.getAttribute("icon")}`
                                    : ""
                            }
                            ${this.getAttribute("link") ? `link=${this.getAttribute("link")}` : ""}
                            ${this.getAttribute("hxAttr") ? `${this.getAttribute("hxAttr")}` : ""}
                            label=${this.getAttribute("confirm-label")}
                            theme=${this.getAttribute("theme")}
                        ></web-button>
                    </div>
                </div>
            </div>
        `;
        this.attachListeners();
    }
}

customElements.define("web-modal", WebModal);
