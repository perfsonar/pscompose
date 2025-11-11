import { FormControl } from "./form-control.js";

export class InputTextArea extends FormControl {
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
            this.value = this.textAreaEl.value;
            this.dispatchEvent(new Event("change", { bubbles: true }));
        });
        this.textAreaEl?.addEventListener("input", () => this.markDirty(), { once: true });
        this.textAreaEl?.addEventListener("blur", () => this.markDirty(), { once: true });
    }

    render() {
        this.textAreaEl = this.querySelector("textarea");
        this.textAreaEl.placeholder = `Enter ${this.label}`;
        if (this.value) this.textAreaEl.value = this.value;
        this.attachEventListener();
    }
}

customElements.define("input-text-area", InputTextArea);
