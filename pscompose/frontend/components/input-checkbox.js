class TextInputCheckbox extends HTMLElement {
    static observedAttributes = ["label", "checked"];

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
                        this.getAttribute("checked") === "true" ? "checked" : ""
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
                <p> ${this.getAttribute("checked")}</p>
            </div>
        `;

        this.querySelector('input[type="checkbox"]').addEventListener("change", (event) => {
            this.setAttribute("checked", event.target.checked ? "true" : "false");
            this.dispatchEvent(new Event("change", { bubbles: true }));
        });
    }
}

customElements.define("input-checkbox", TextInputCheckbox);
