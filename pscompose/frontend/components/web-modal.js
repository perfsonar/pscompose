export class WebModal extends HTMLElement {
    static observedAttributes = ["confirm-label", "link", "theme", "message", "hxAttr"];

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
        const yes = document.querySelector("#confirm-yes");
        const no = document.querySelector("#confirm-no");
        const underlay = document.querySelector(".modal-underlay");

        yes.onclick = function () {
            document.getElementById("confirm-modal").style.display = "none";
            const confirmEvent = new CustomEvent("confirm-yes-clicked", {
                bubbles: true,
            });
            document.body.dispatchEvent(confirmEvent);
        };
        no.onclick = function () {
            document.getElementById("confirm-modal").style.display = "none";
        };
        underlay.onclick = function () {
            document.getElementById("confirm-modal").style.display = "none";
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
                    <i  style="width: 2rem; height: 2rem; color: ${accentColor}" data-lucide=  "alert-triangle">
                    </i>
                    <h4 id="confirm-question">${this.getAttribute("message")}</h4>
                    <div class="save-cancel">
                        <web-button id="confirm-no" data-label="Cancel" data-theme="Shadow"></web-button>
                        <web-button
                            id="confirm-yes"
                            ${
                                this.getAttribute("link")
                                    ? `data-link=${this.getAttribute("link")}`
                                    : ""
                            }
                            ${
                                this.getAttribute("icon")
                                    ? `data-righticon=${this.getAttribute("icon")}`
                                    : ""
                            }
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
