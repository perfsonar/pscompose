export class InputMessage extends HTMLElement {
    static observedAttributes = ["required", "errors"];

    constructor() {
        super();
    }

    connectedCallback() {
        this.render();
    }

    attributeChangedCallback(name, oldValue, newValue) {
        this[name] = newValue;
        this.render();
    }

    render() {
        const required = JSON.parse(this.getAttribute("required") || "false");

        const errorExist =
            this.getAttribute("errors") != "null" ? this.getAttribute("errors") : false;
        const errorRequired = this.getAttribute("errors") !== "is a required property";
        const errorState = errorExist && errorRequired;

        this.innerHTML = `                
        <div class="input-message ${errorState ? "error" : ""}">
            <div class="errors">${
                this.getAttribute("errors") ? this.getAttribute("errors") : ""
            }</div>
            <div class="required">${required ? "Required" : ""}</div>
        </div>
    `;
    }
}

customElements.define("input-message", InputMessage);
