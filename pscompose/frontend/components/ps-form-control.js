export class PSFormControl extends HTMLElement {
    static get observedAttributes() {
        return ["id", "class", "label", "value", "description", "error", "required", "disabled"];
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
    get id() {
        return this.getAttribute("id") ?? "";
    }
    set id(v) {
        this.setAttribute("id", v ?? "");
    }
    get class() {
        return this.getAttribute("class") ?? "";
    }
    set class(v) {
        this.setAttribute("class", v ?? "");
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
            <div class="form-container">
                <ps-input-label 
                    label="${this.label}" 
                    desc="${this.description}">
                </ps-input-label>
                ${this.slotEl || ""}
                <ps-input-message 
                    error='${this.dirty ? this.error : ""}'
                    ${this.required ? "required" : ""}>
                </ps-input-message>
            </div>
        `;
        this.containerEl = this.querySelector(".form-container");
    }

    render() {}
}

customElements.define("ps-form-control", PSFormControl);
