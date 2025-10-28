class InputCheckbox extends HTMLElement {
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
                        JSON.parse(this.getAttribute("value")) === true ? "checked" : ""
                    } >
                    </input>
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
                <input-message errors="${this.getAttribute(
                    "errors",
                )}" required="${this.getAttribute("required")}"></input-message>
            </div>

            <div class="checkbox-container-disabled">
                <label>${this.getAttribute("label")}</label> 
                <div class="wrapper">       
                    <p> ${JSON.parse(this.getAttribute("value"))}</p>
                </div>
            </div>
        `;

        const input = this.querySelector("input");
        input.addEventListener("change", (event) => {
            event.stopPropagation();
            const boolVal = event.target.checked ? true : false;
            this.setAttribute("value", JSON.stringify(boolVal));
            this.dispatchEvent(new Event("change", { bubbles: true }));
        });
    }
}

customElements.define("input-checkbox", InputCheckbox);
