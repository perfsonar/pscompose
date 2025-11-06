export class InputText extends HTMLElement {
    static observedAttributes = ["label", "value", "description", "required", "errors"];

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
        const desc = this.getAttribute("description");
        const descAttr = desc != null ? ` desc='${desc}'` : "";

        this.innerHTML = `
            <div class="container">
                <input-label label='${this.getAttribute("label")}'${descAttr}></input-label>
                <div class="wrapper">
                    <input type="text" placeholder="Enter ${this.getAttribute("label")}" value="${
                        JSON.parse(this.getAttribute("value")) || ""
                    }" >
                    </input>
                </div>
                <input-message errors='${this.getAttribute(
                    "errors",
                )}' required='${this.getAttribute("required")}'></input-message>
            </div>
        `;
        const input = this.querySelector("input");
        input.addEventListener("change", (event) => {
            event.stopPropagation();
            this.setAttribute("value", JSON.stringify(input.value));
            this.dispatchEvent(new Event("change", { bubbles: true }));
        });
    }
}

customElements.define("input-text", InputText);
