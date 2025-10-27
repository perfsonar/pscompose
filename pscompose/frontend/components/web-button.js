export class WebButton extends HTMLElement {
    static observedAttributes = [
        "id",
        "type",
        "data-label",
        "data-theme",
        "data-lefticon",
        "data-righticon",
        "data-link",
        "confirm-modal",
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

    openModal() {
        const handler = () => {
            document.getElementById(this.getAttribute("confirm-modal")).style.display = "block";
            document.querySelector("json-form").removeEventListener("validated", handler);
        };
        document.querySelector("json-form").addEventListener("validated", handler);
    }

    render() {
        this.innerHTML = `
            ${
                this.getAttribute("data-link")
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
                    this.removeAttribute(k);
                }
            }
        });

        if (this.getAttribute("confirm-modal")) {
            btn.addEventListener("click", () => this.openModal());
        }
    }
}

customElements.define("web-button", WebButton);
