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
                ${this.getAttribute("required") == "true" ? `<required>Required<required>` : ""}
            </div>
        `;
        this.querySelector("input").addEventListener("change", () => {
            this.dispatchEvent(new Event("change", { bubbles: true }));
        });
    }
}

customElements.define("input-text", TextInput);
