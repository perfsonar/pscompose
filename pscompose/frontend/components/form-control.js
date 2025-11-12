export class FormControl extends HTMLElement {
    static get observedAttributes() {
        return ["class", "label", "value", "description", "error", "required", "disabled"];
    }

    constructor() {
        super();
        this.slotEl = "";
        this._dirty = false;
    }

    get value() {
        return this.getAttribute("value") ? JSON.parse(this.getAttribute("value")) : undefined;
    }
    set value(v) {
        this.setAttribute("value", JSON.stringify(v) ?? "");
    }

    get label() {
        return this.getAttribute("label") ?? "";
    }
    set label(v) {
        this.setAttribute("label", v ?? "");
    }

    get description() {
        return this.getAttribute("description") ?? "";
    }
    set description(v) {
        this.setAttribute("description", v ?? "");
    }

    get error() {
        return this.getAttribute("error") ?? "";
    }
    set error(v) {
        this.setAttribute("error", v ?? "");
    }

    get disabled() {
        return this.hasAttribute("disabled");
    }
    set disabled(v) {
        v ? this.setAttribute("disabled", "") : this.removeAttribute("disabled");
    }

    get required() {
        return this.hasAttribute("required");
    }
    set required(v) {
        v ? this.setAttribute("required", "") : this.removeAttribute("required");
    }

    get dirty() {
        return this._dirty;
    }

    markDirty() {
        if (!this._dirty) {
            this._dirty = true;
        }
    }

    connectedCallback() {
        this.renderControl();
        this.render();
    }

    attributeChangedCallback(name, oldValue, newValue) {
        if (oldValue == newValue) return;
        this.renderControl();
        this.render();
    }

    renderControl() {
        this.innerHTML = `
            <div class="container">
                <input-label 
                    label="${this.label}" 
                    desc="${this.description}">
                </input-label>
                ${this.slotEl || ""}
                <input-message 
                    error='${this.dirty ? this.error : ""}'
                    ${this.required ? "required" : ""}>
                </input-message>
            </div>
        `;
        this.containerEl = this.querySelector(".container");
    }

    render() {}
}

customElements.define("form-control", FormControl);
