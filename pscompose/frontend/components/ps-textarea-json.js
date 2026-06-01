import { PSFormControl } from "./ps-form-control.js";

export class InputTextAreaJSON extends PSFormControl {
    constructor() {
        super();
        this.slotEl = `
            <div class='wrapper'>
                <textarea></textarea>
            </div>`;
        this.textAreaEl = null;
    }

    attachEventListener() {
        this.textAreaEl?.addEventListener("change", (e) => {
            e.preventDefault();
            this.markDirty();
            const raw = this.textAreaEl.value.trim();
            try {
                this.value = JSON.parse(raw);
            } catch (err) {
                // Not valid JSON, treat as plain string
                this.value = raw;
            }
            this.dispatchEvent(new Event("change", { bubbles: true }));
        });
        this.textAreaEl?.addEventListener("input", () => this.markDirty(), { once: true });
        this.textAreaEl?.addEventListener("blur", () => this.markDirty(), { once: true });
    }

    formatValue(value) {
        if (value === null || value === undefined) return "";
        if (typeof value === "string") return value;
        return JSON.stringify(value, null, 2);
    }

    render() {
        this.textAreaEl = this.querySelector("textarea");
        this.textAreaEl.placeholder = `Enter ${this.label}`;
        if (this.value) this.textAreaEl.value = this.formatValue(this.value);
        this.attachEventListener();
    }
}

customElements.define("ps-textarea-json", InputTextAreaJSON);
