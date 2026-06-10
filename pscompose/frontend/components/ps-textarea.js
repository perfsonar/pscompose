import { PSFormControl } from "./ps-form-control.js";

export class PSTextArea extends PSFormControl {
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
            this.value = this.textAreaEl.value === undefined ? "" : this.textAreaEl.value;
            this.dispatchEvent(new Event("change", { bubbles: true }));
        });
        this.textAreaEl?.addEventListener("input", () => this.markDirty(), { once: true });
        this.textAreaEl?.addEventListener("blur", () => this.markDirty(), { once: true });
    }

    render() {
        this.textAreaEl = this.querySelector("textarea");
        const ex = this.examples?.[0];
        this.textAreaEl.placeholder =
            ex != null ? (typeof ex === "string" ? ex : JSON.stringify(ex)) : `Enter ${this.label}`;

        if (this.value) this.textAreaEl.value = this.value;
        this.attachEventListener();
    }
}

customElements.define("ps-textarea", PSTextArea);
