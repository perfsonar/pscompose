import { InputText } from "./input-text.js";

export class InputCheckbox extends InputText {
    render() {
        super.render();
        this.inputEl.checked = this.value === "true" || this.value === true;
        if (!this.disabled) {
            this.inputEl?.setAttribute("type", "checkbox");
            this.inputEl?.removeAttribute("value");
        } else {
            this.inputEl.value = this.value;
        }
    }
}

customElements.define("input-checkbox", InputCheckbox);
