class InputCheckboxStar extends HTMLElement {
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

    get disabled() {
        return this.hasAttribute("disabled");
    }

    set disabled(v) {
        v ? this.setAttribute("disabled", "") : this.removeAttribute("disabled");
    }

    constructor() {
        super();
    }

    connectedCallback() {
        this.render();
        lucide.createIcons();
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
        this.starEl.addEventListener("click", () => this.toggle());
    }

    render() {
        const disabled = this.hasAttribute("disabled");

        this.innerHTML = `<button class="star ${this.value ? "checked" : ""}" ${
            disabled ? "disabled" : ""
        }>
                <i data-lucide='star'></i>
            </button>`;
        this.starEl = this.querySelector("button");
        this.attachEventListener();
    }
}

customElements.define("input-checkbox-star", InputCheckboxStar);