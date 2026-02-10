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

    constructor() {
        super();
    }

    get label() {
        return this.getAttribute("label") ?? "";
    }
    set label(v) {
        this.setAttribute("label", v ?? "");
    }
    get id() {
        return this.getAttribute("id") ?? "";
    }
    set id(v) {
        this.setAttribute("id", v ?? "");
    }
    get type() {
        return this.getAttribute("type") ?? "";
    }
    set type(v) {
        this.setAttribute("type", v ?? "");
    }
    get theme() {
        return this.getAttribute("theme") ?? "";
    }
    set theme(v) {
        this.setAttribute("theme", v ?? "");
    }
    get lefticon() {
        return this.getAttribute("lefticon") ?? "";
    }
    set lefticon(v) {
        this.setAttribute("lefticon", v ?? "");
    }
    get righticon() {
        return this.getAttribute("righticon") ?? "";
    }
    set righticon(v) {
        this.setAttribute("righticon", v ?? "");
    }
    get link() {
        return this.getAttribute("link") ?? "";
    }
    set link(v) {
        this.setAttribute("link", v ?? "");
    }
    get disabled() {
        return this.hasAttribute("disabled");
    }
    set disabled(v) {
        v ? this.setAttribute("disabled", "") : this.removeAttribute("disabled");
    }

    connectedCallback() {
        this.render();
        lucide.createIcons();
    }

    attributeChangedCallback(name, oldValue, newValue) {
        if (oldValue === newValue) return;
        this.render();
        lucide.createIcons();
        this[name] = newValue;
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
                this.link
                    ? `<a href="${this.link}" style="text-decoration: none;">`
                    : ""
            }
            <button 
                ${this.type ? `type="${this.type}" ` : ""}
                >
                
                ${
                    this.lefticon
                        ? `<i data-lucide="${this.lefticon}"></i>`
                        : ""
                }
                ${this.label || ""}
                ${
                    this.righticon
                        ? `<i data-lucide="${this.righticon}"></i>`
                        : ""
                }
            </button>
            ${this.link ? `</a>` : ""}
        `;

        let btn = this.querySelector("button");
        if (this.getAttribute("confirm-modal")) {
            btn.addEventListener("click", () => this.openModal());
        }
    }
}

customElements.define("ps-button", PSButton);
