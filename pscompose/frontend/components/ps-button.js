import { attr, boolAttr } from "./ps-utils.js";

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
        "newtab",
        "aria-label",
    ];

    constructor() {
        super();
    }

    connectedCallback() {
        this.render();
        lucide.createIcons();
        // Attach once at component level — survives innerHTML re-renders
        this._onConfirmClick = () => {
            if (this.getAttribute("confirm-modal")) this.openModal();
        };
        this.addEventListener("click", this._onConfirmClick);
    }

    disconnectedCallback() {
        this.removeEventListener("click", this._onConfirmClick);
    }

    attributeChangedCallback(name, oldValue, newValue) {
        if (oldValue === newValue) return;
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
                this.link
                    ? `<a href="${this.link}" ${
                          this.newtab ? `target="_blank"` : ""
                      } style="text-decoration: none;">`
                    : ""
            }
            <button
                ${this.type ? `type="${this.type}"` : ""}
                ${
                    this.getAttribute("aria-label")
                        ? `aria-label="${this.getAttribute("aria-label")}"`
                        : ""
                }
            >
                ${this.lefticon ? `<i data-lucide="${this.lefticon}"></i>` : ""}
                ${this.label || ""}
                ${this.righticon ? `<i data-lucide="${this.righticon}"></i>` : ""}
            </button>
            ${this.link ? `</a>` : ""}
        `;
    }
}

Object.defineProperties(PSButton.prototype, {
    label: attr("label"),
    id: attr("id"),
    type: attr("type"),
    theme: attr("theme"),
    lefticon: attr("lefticon"),
    righticon: attr("righticon"),
    link: attr("link"),
    disabled: boolAttr("disabled"),
    newtab: boolAttr("newtab"),
});

customElements.define("ps-button", PSButton);
