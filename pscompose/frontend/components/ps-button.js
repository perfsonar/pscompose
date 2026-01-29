export class PSButton extends HTMLElement {
    static observedAttributes = [
        "id",
        "type",
        "label",
        "theme",
        "lefticon",
        "righticon",
        "link",
        "confirm-modal",
    ];
    passthroughAttributes = {};
    passthroughAttributeMatchers = [
        new RegExp(/aria-.*/),  
        new RegExp(/role$/),   
    ];

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
            this.passthroughAttributeMatchers.some((re) => {
                if (re.test(attr.name)) {
                    this.passthroughAttributes[attr.name] = this.getAttribute(attr.name);
                    return true; 
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
            document.removeEventListener("validated", handler);
        };
        document.addEventListener("validated", handler);
    }

    render() {
        this.innerHTML = `
            ${
                this.getAttribute("link")
                    ? `<a href="${this.getAttribute("link")}" style="text-decoration: none;">`
                    : ""
            }
            <button 
                ${this.getAttribute("type") ? `type="${this.getAttribute("type")}" ` : ""}
                >
                
                ${
                    this.getAttribute("lefticon")
                        ? `<i data-lucide="${this.getAttribute("lefticon")}"></i>`
                        : ""
                }
                ${this.getAttribute("label") || ""}
                ${
                    this.getAttribute("righticon")
                        ? `<i data-lucide="${this.getAttribute("righticon")}"></i>`
                        : ""
                }
            </button>
            ${this.getAttribute("link") ? `</a>` : ""}
        `;

        let btn = this.querySelector("button");
        Object.keys(this.passthroughAttributes).forEach((k) => {
            btn.setAttribute(k, this.passthroughAttributes[k]);
            this.removeAttribute(k);
        });

        if (this.getAttribute("confirm-modal")) {
            btn.addEventListener("click", () => this.openModal());
        }
    }
}

customElements.define("ps-button", PSButton);
