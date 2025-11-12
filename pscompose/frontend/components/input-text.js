import { FormControl } from "./form-control.js";

export class InputText extends FormControl {
    constructor() {
        super();
        this.slotEl = `
            <div class="wrapper">
                <input type='text' />
            </div>
        `;
        this.inputEl = null;
        this.wrapperEl = null;
    }

    attachEventListener() {
        this.inputEl?.addEventListener("change", (e) => {
            e.preventDefault();
            this.markDirty();
            switch (this.inputEl.type) {
                case "number":
                    this.value = this.inputEl.value === "" ? undefined : Number(this.inputEl.value);
                    break;
                case "checkbox":
                    this.value = Boolean(this.inputEl.checked);
                    break;
                default:
                    this.value = this.inputEl.value === "" ? undefined : this.inputEl.value;
            }
            this.dispatchEvent(new Event("change", { bubbles: true }));
        });
        // this.inputEl?.addEventListener("input", () => this.markDirty(), { once: true });
        // this.inputEl?.addEventListener("blur", () => this.markDirty(), { once: true });
    }

    render() {
        this.inputEl = this.querySelector("input");
        this.wrapperEl = this.querySelector(".wrapper");
        this.inputEl.placeholder = `Enter ${this.label}`;
        if (this.value) this.inputEl.value = this.value;
        this.attachEventListener();
    }
}

customElements.define("input-text", InputText);
