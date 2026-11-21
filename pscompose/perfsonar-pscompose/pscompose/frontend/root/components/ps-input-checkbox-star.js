import { boolAttr } from "./ps-utils.js";

class PSInputCheckboxStar extends HTMLElement {
    static get observedAttributes() {
        return ["value", "disabled"];
    }

    get value() {
        return this._value === true;
    }
    set value(v) {
        this._value = Boolean(v);
        this.setAttribute("value", this._value);
    }

    constructor() {
        super();
        this._onClick = null;
    }

    connectedCallback() {
        this.render();
        lucide.createIcons();
    }

    disconnectedCallback() {
        if (this.starEl && this._onClick) {
            this.starEl.removeEventListener("click", this._onClick);
        }
    }

    attributeChangedCallback(name, oldValue, newValue) {
        if (oldValue == newValue) return;
        this.render();
        lucide.createIcons();
    }

    toggle() {
        if (this.hasAttribute("disabled")) return;
        this.value = !this.value;
        this.dispatchEvent(new Event("change", { bubbles: true }));
    }

    attachEventListener() {
        this._onClick = () => this.toggle();
        this.starEl.addEventListener("click", this._onClick);
    }

    render() {
        const disabled = this.hasAttribute("disabled");
        this.innerHTML = `<button class="star ${this.value ? "checked" : ""}" ${
            disabled ? "disabled" : ""
        }>
            <i data-lucide="star"></i>
        </button>`;
        this.starEl = this.querySelector("button");
        this.attachEventListener();
    }
}

Object.defineProperties(PSInputCheckboxStar.prototype, {
    disabled: boolAttr("disabled"),
});

customElements.define("ps-input-checkbox-star", PSInputCheckboxStar);
