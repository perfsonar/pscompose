import { attr, boolAttr } from "./ps-utils.js";

export class PSInputSwitch extends HTMLElement {
    static get observedAttributes() {
        return ["checked", "icon"];
    }

    constructor() {
        super();
        this._onChange = null;
    }

    connectedCallback() {
        this.render();
    }

    disconnectedCallback() {
        if (this.inputEl && this._onChange) {
            this.inputEl.removeEventListener("change", this._onChange);
        }
    }

    attributeChangedCallback(name, oldValue, newValue) {
        if (oldValue !== newValue) this.render();
    }

    attachEventListener() {
        this._onChange = (e) => {
            e.preventDefault();
            this.checked = this.inputEl.checked;
            this.setAttribute("aria-checked", String(this.inputEl.checked));
            this.dispatchEvent(new Event("change", { bubbles: true }));
        };
        this.inputEl.addEventListener("change", this._onChange);
    }

    render() {
        this.innerHTML = `
            <div class="ps-input-switch-container" ${this.checked ? "checked" : ""}>
                <input
                    type="checkbox"
                    class="ps-input-switch-input"
                    role="switch"
                    aria-checked="${this.checked}"
                    ${this.checked ? "checked" : ""}
                />
                <span class="ps-input-switch-indicator">
                    <i class="ps-input-switch-icon" data-lucide="${this.icon || ""}"></i>
                </span>
            </div>
        `;
        this.inputEl = this.querySelector(".ps-input-switch-input");
        this.attachEventListener();
        lucide.createIcons();
    }
}

Object.defineProperties(PSInputSwitch.prototype, {
    icon: attr("icon"),
    checked: boolAttr("checked"),
});

customElements.define("ps-input-switch", PSInputSwitch);
