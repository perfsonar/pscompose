export class InputNum extends HTMLElement {
    static observedAttributes = ["label", "step", "min", "max", "description", "value", "errors"];

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

    onPlusClick = () => {
        const input = this.querySelector("input");
        if (!input) return;
        input.stepUp();
        input.dispatchEvent(new Event("change", { bubbles: true }));
    };

    onMinusClick = () => {
        const input = this.querySelector("input");
        if (!input) return;
        input.stepDown();
        input.dispatchEvent(new Event("change", { bubbles: true }));
    };

    render() {
        this.innerHTML = `
            <div class="container">
                <input-label label='${this.getAttribute("label")}' desc='${this.getAttribute(
                    "description",
                )}'></input-label>
                <div class="wrapper">
                    <input  type="number" 
                            placeholder="Enter ${this.getAttribute("label")}" 
                            value="${JSON.parse(this.getAttribute("value")) || ""}" 
                            step="${this.getAttribute("step") || 1}"
                            min="${this.getAttribute("min") || 0}"
                            max="${this.getAttribute("max") || 100}"
                            >
                    </input>
                    <div class="buttons">
                        <web-button type="button" id="plus-btn" data-theme="Icon" data-righticon="plus"></web-button>
                        <web-button type="button" id="minus-btn" data-theme="Icon" data-righticon="minus"></web-button>
                    </div>
                </div>
                <input-message errors='${this.getAttribute(
                    "errors",
                )}' required='${this.getAttribute("required")}'></input-message>
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

customElements.define("input-number", InputNum);
