export class WebButton extends HTMLElement {
    static observedAttributes = [
        "id",
        "type",
        "data-label",
        "data-theme",
        "data-lefticon",
        "data-righticon",
        "data-link",
        "data-modalconfirm",
    ];
    passthroughAttributes = {};
    passthroughAttributeMatchers = [new RegExp(/hx-.*/), new RegExp(/data-.*/)];

    constructor() {
        super();
    }

    connectedCallback() {
        this.render();
        lucide.createIcons();
    }

    attributeChangedCallback(name, oldValue, newValue) {
        if (oldValue === newValue) return;
        Array.from(this.attributes).forEach((attr) => {
            this.passthroughAttributeMatchers.forEach((re) => {
                if (re.test(attr.name)) {
                    this.passthroughAttributes[attr.name] = this.getAttribute(attr.name);
                }
            });
        });
        this[name] = newValue;
        this.render();
        lucide.createIcons();
    }

    render() {
        const hasModalConfirm = !!this.getAttribute("data-modalconfirm");
        const hxAttrs = Array.from(this.attributes)
            .filter((attr) => attr.name.startsWith("hx-"))
            .map((attr) => `${attr.name}="${attr.value}"`)
            .join(" ");

        this.innerHTML = `
            ${
                this.getAttribute("data-link") && !hasModalConfirm
                    ? `<a href="${this.getAttribute("data-link")}" style="text-decoration: none;">`
                    : ""
            }
            <button 
                ${this.getAttribute("type") ? `type="${this.getAttribute("type")}" ` : ""}
                ${this.getAttribute("id") ? `id="${this.getAttribute("id")}" ` : ""} >
                
                ${
                    this.getAttribute("data-lefticon")
                        ? `<i data-lucide="${this.getAttribute("data-lefticon")}"></i>`
                        : ""
                }
                ${this.getAttribute("data-label") || ""}
                ${
                    this.getAttribute("data-righticon")
                        ? `<i data-lucide="${this.getAttribute("data-righticon")}"></i>`
                        : ""
                }
            </button>
            ${this.getAttribute("data-link") ? `</a>` : ""}
        `;

        let btn = this.querySelector("button");
        Object.keys(this.passthroughAttributes).forEach((k) => {
            if (k.startsWith("hx-")) {
                if (!hasModalConfirm) {
                    btn.setAttribute(k, this.passthroughAttributes[k]);
                }
                this.removeAttribute(k);
            }
        });

        if (this.getAttribute("data-modalconfirm")) {
            btn.addEventListener("click", () => {
                this.modalInnerHTML = `<web-modal
                        ${
                            this.getAttribute("data-link")
                                ? `link=${this.getAttribute("data-link")}`
                                : ""
                        }
                        ${
                            this.getAttribute("data-righticon")
                                ? `icon=${this.getAttribute("data-righticon")}`
                                : ""
                        }
                        ${
                            this.getAttribute("data-lefticon")
                                ? `icon=${this.getAttribute("data-lefticon")}`
                                : ""
                        }

                        theme="${this.getAttribute("data-theme")}"
                        message="${this.getAttribute("data-modalconfirm")}"
                        confirm-label = "${this.getAttribute("data-label")}"
                        ${this.hxAttrs}
                    ></web-modal>`;

                const responseContainer = document.getElementById("response-container");
                if (responseContainer) {
                    responseContainer.innerHTML = this.modalInnerHTML;
                }
            });
        }
    }
}

customElements.define("web-button", WebButton);
