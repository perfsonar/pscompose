import { PSFormControl } from "./ps-form-control.js";

// JSON specific ps-textarea
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
            const raw = this.textAreaEl.value;
            try {
                this.value = JSON.parse(raw);
            } catch (err) {
                this.value = raw;
            }
            this.dispatchEvent(new Event("change", { bubbles: true }));
        });
        this.textAreaEl?.addEventListener("input", () => this.markDirty(), { once: true });
        this.textAreaEl?.addEventListener("blur", () => this.markDirty(), { once: true });
    }

    render() {
        this.textAreaEl = this.querySelector("textarea");
        this.textAreaEl.placeholder = `Enter ${this.label}`;
        if (this.value) this.textAreaEl.value = JSON.stringify(this.value, null, 2);
        this.attachEventListener();
    }
}

customElements.define("ps-textarea-json", InputTextAreaJSON);
