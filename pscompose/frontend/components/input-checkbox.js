class TextInputCheckbox extends HTMLElement {
    static observedAttributes = ["label", "value"];

    constructor() {
        super();
    }

    connectedCallback() {
        this.render();
        lucide.createIcons();
    }

    attributeChangedCallback(name, oldValue, newValue) {
        this[name] = newValue;
        this.render();
        lucide.createIcons();
    }

    render() {
        this.innerHTML = `
            <div class="container">
                <div class="input-checkbox-wrapper">
                    <input type="checkbox" ${
                        this.getAttribute("value") === "true" ? "checked" : ""
                    } />
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
                </div>
                ${
                    this.getAttribute("required") == "true"
                        ? `<div class="required">Required</div>`
                        : ""
                }
            </div>

            <div class="checkbox-container-disabled">
                <label>${this.getAttribute("label")}</label>        
                <p> ${this.getAttribute("value")}</p>
            </div>
        `;

        const input = this.querySelector("input");
        input.addEventListener("change", (event) => {
            event.stopPropagation();
            this.setAttribute("value", event.target.checked ? "true" : "false");
            this.dispatchEvent(new Event("change", { bubbles: true }));
        });
    }
}

customElements.define("input-checkbox", TextInputCheckbox);
