import { attr } from "./ps-utils.js";

export class PSInputLabel extends HTMLElement {
    static get observedAttributes() {
        return ["label", "desc"];
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
            <label>
                ${this.label}
                ${
                    this.desc
                        ? `<ps-tooltip desc="${this.desc.replace(/"/g, "&quot;")}"> </ps-tooltip>`
                        : ""
                }
            </label>`;
    }
}

Object.defineProperties(PSInputLabel.prototype, {
    label: attr("label"),
    desc: attr("desc"),
});

customElements.define("ps-input-label", PSInputLabel);
