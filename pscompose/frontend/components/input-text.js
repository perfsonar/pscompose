export class TextInput extends HTMLElement {
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
                <div class="input-wrapper">
                    <input type="text" placeholder="Enter ${this.getAttribute("label")}" value="${
                        this.getAttribute("value") || ""
                    }" />
                </div>
                ${
                    this.getAttribute("required") == "true"
                        ? `<div class="required">Required</div>`
                        : ""
                }
            </div>
        `;
        const input = this.querySelector("input");
        input.addEventListener("change", (event) => {
            event.stopPropagation();
            this.setAttribute("value", input.value);
            this.dispatchEvent(new Event("change", { bubbles: true }));
        });
    }
}

customElements.define("input-text", TextInput);
