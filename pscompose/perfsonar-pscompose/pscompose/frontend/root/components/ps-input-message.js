import { attr, boolAttr } from "./ps-utils.js";

export class PSInputMessage extends HTMLElement {
    static get observedAttributes() {
        return ["required", "error"];
    }

    constructor() {
        super();
    }

    connectedCallback() {
        this.render();
    }

    attributeChangedCallback(name, oldVal, newVal) {
        if (oldVal !== newVal) this.render();
    }

    render() {
        this.innerHTML = `
            <div class='error ${this.error ? "show" : ""}'>${this.error}</div>
            <div class="required">${this.required ? "Required" : ""}</div>
    `;
    }
}

Object.defineProperties(PSInputMessage.prototype, {
    error: attr("error"),
    required: boolAttr("required"),
});

customElements.define("ps-input-message", PSInputMessage);
