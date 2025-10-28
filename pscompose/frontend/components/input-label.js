export class InputLabel extends HTMLElement {
    static observedAttributes = ["label", "desc"];

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
        this.innerHTML = `                
        <label>
            ${this.getAttribute("label")}
            ${
                this.getAttribute("desc")
                    ? `<web-tooltip desc="${this.getAttribute("desc")}"> </web-tooltip>`
                    : ""
            }
        </label>
    `;
    }
}

customElements.define("input-label", InputLabel);
