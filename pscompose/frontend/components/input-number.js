export class TextInputNum extends HTMLElement {
    static observedAttributes = ["label", "value", "step", "min", "max", "description"];

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

    onPlusClick() {
        const input = document.querySelector('input[type="number"]');
        input.stepUp();
        input.dispatchEvent(new Event("change"));
    }

    onMinusClick() {
        const input = document.querySelector('input[type="number"]');
        input.stepDown();
        input.dispatchEvent(new Event("change"));
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
                    <input  type="number" 
                            placeholder="Enter ${this.getAttribute("label")}" 
                            value="${this.getAttribute("value") || ""}" 
                            step="${this.getAttribute("step") || 1}"
                            min="${this.getAttribute("min") || 0}"
                            max="${this.getAttribute("max") || 100}"
                            />
                    <div class="buttons">
                        <web-button type="button" id="plus-btn" data-theme="Icon" data-righticon="plus"></web-button>
                        <web-button type="button" id="minus-btn" data-theme="Icon" data-righticon="minus"></web-button>
                    </div>
                </div>
                ${
                    this.getAttribute("required") == "true"
                        ? `<div class="required">Required</div>`
                        : ""
                }
            </div>
        `;

        this.querySelector("#plus-btn").addEventListener("click", this.onPlusClick);
        this.querySelector("#minus-btn").addEventListener("click", this.onMinusClick);
        const input = this.querySelector("input");
        input.addEventListener("change", (event) => {
            event.stopPropagation();
            this.setAttribute("value", input.value);
            this.dispatchEvent(new Event("change", { bubbles: true }));
        });
    }
}

customElements.define("input-number", TextInputNum);
