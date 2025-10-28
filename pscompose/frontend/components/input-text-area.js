export class InputTextArea extends HTMLElement {
    static observedAttributes = ["label", "value"];

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
            <div class="container">
                <label>          
                    ${this.getAttribute("label")}
                    ${
                        this.getAttribute("description")
                            ? `<web-tooltip description="${this.getAttribute(
                                  "description",
                              )}"> </web-tooltip>`
                            : ""
                    }
                </label>
                <div class="wrapper">
                    <textarea type="text" placeholder="Enter ${this.getAttribute("label")}">${
                        JSON.parse(this.getAttribute("value")) || ""
                    }</textarea>
                </div>
                <input-message errors="${this.getAttribute(
                    "errors",
                )}" required="${this.getAttribute("required")}"></input-message>
            </div>
        `;
        const textarea = this.querySelector("textarea");
        textarea.addEventListener("change", (event) => {
            event.stopPropagation();
            this.setAttribute("value", JSON.stringify(textarea.value));
            this.dispatchEvent(new Event("change", { bubbles: true }));
        });
    }
}

customElements.define("input-text-area", InputTextArea);
