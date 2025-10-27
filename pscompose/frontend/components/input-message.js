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
        const errorExist = this.getAttribute("errors") ? true : false;
        const errorRequired = this.getAttribute("errors") == "is a required property";
        const errorState = errorExist & !errorRequired;
        const required = JSON.parse(this.getAttribute("required")) ? true : false;

        this.innerHTML = `                
            <div class="input-message ${errorState ? "error" : ""}" >
                <div class="errors">${errorExist ? `${this.getAttribute("errors")}` : ""}</div>
                <div class="required">${required ? `Required` : ""}</div>
            </div>
        `;
    }
}

customElements.define("input-message", InputMessage);
