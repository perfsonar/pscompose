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
        const error = this.getAttribute("errors");
        const required = JSON.parse(this.getAttribute("required") || "false");

        const errorExist = error && error.trim() !== "";
        const errorRequired = error !== "is a required property";
        const errorState = errorExist && errorRequired;

        this.innerHTML = `                
        <div class="input-message ${errorState ? "error" : ""}">
            <div class="errors">${error || ""}</div>
            <div class="required">${required ? "Required" : ""}</div>
        </div>
    `;
    }
}

customElements.define("input-message", InputMessage);
