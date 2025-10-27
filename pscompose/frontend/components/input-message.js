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
        const error = this.getAttribute("errors") ? true : false;
        const required = JSON.parse(this.getAttribute("required")) ? true : false;

        this.innerHTML = `                
            <div class="input-message ${error ? "error" : ""}" >
                <div class="errors">${error ? `${this.getAttribute("errors")}` : ""}</div>
                <div class="required">${required ? `Required` : ""}</div>
            </div>
        `;
    }
}

customElements.define("input-message", InputMessage);
