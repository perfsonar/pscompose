export class TextInputArea extends HTMLElement {
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
                <textarea type="text" placeholder="Enter ${this.getAttribute("label")}">${
                    this.getAttribute("value") || ""
                }</textarea>
                ${
                    this.getAttribute("required") == "true"
                        ? `<div class="required">Required</div>`
                        : ""
                }
            </div>
        `;
        const textarea = this.querySelector("textarea");
        textarea.addEventListener("change", (event) => {
            event.stopPropagation();
            this.setAttribute("value", textarea.value);
            this.dispatchEvent(new Event("change", { bubbles: true }));
        });
    }
}

customElements.define("input-text-area", TextInputArea);
