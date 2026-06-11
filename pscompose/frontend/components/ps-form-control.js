import { attr, boolAttr } from "./ps-utils.js";

export class PSFormControl extends HTMLElement {
    static get observedAttributes() {
        return [
            "id",
            "class",
            "theme",
            "label",
            "value",
            "description",
            "error",
            "required",
            "disabled",
            "examples",
        ];
    }

    constructor() {
        super();
        this.slotEl = "";
        this._dirty = false;
    }

    get value() {
        try {
            return this.getAttribute("value") ? JSON.parse(this.getAttribute("value")) : undefined;
        } catch {
            return this.getAttribute("value");
        }
    }
    set value(v) {
        this.setAttribute("value", JSON.stringify(v) ?? "");
    }

    get examples() {
        try {
            return this.getAttribute("examples")
                ? JSON.parse(this.getAttribute("examples"))
                : undefined;
        } catch {
            return undefined;
        }
    }
    set examples(v) {
        this.setAttribute("examples", JSON.stringify(v) ?? "");
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
                    desc="${this.description.replace(/"/g, "&quot;")}">
                </ps-input-label>
                ${this.slotEl || ""}
                <ps-input-message
                    error="${this.dirty ? this.error.replace(/"/g, "&quot;") : ""}"
                    ${this.required ? "required" : ""}>
                </ps-input-message>
            </div>
        `;
        this.containerEl = this.querySelector(".form-container");
    }

    render() {}
}

Object.defineProperties(PSFormControl.prototype, {
    label: attr("label"),
    id: attr("id"),
    class: attr("class"),
    description: attr("description"),
    error: attr("error"),
    disabled: boolAttr("disabled"),
    required: boolAttr("required"),
});

customElements.define("ps-form-control", PSFormControl);
