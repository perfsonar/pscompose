import { PSInputText } from "./ps-input-text.js";

export class PSInputCheckbox extends PSInputText {
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

customElements.define("ps-input-checkbox", PSInputCheckbox);
