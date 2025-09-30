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
                ${this.getAttribute("required") == "true" ? `<required>Required<required>` : ""}
            </div>
        `;
        this.querySelector("textarea").addEventListener("change", () => {
            this.dispatchEvent(new Event("change", { bubbles: true }));
        });
        this.dispatchEvent(new Event("load", { bubbles: true }));
    }
}

customElements.define("input-text-area", TextInputArea);
