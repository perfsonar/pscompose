export class SingleSelectDropdown extends HTMLElement {
    static observedAttributes = ["label", "options", "selected"];

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
        const options = this.options ? JSON.parse(this.options) : [];
        const optionsHTML = options
            .map((option) => `<option value="${option.const}">${option.title}</option>`)
            .join("");

        this.innerHTML = `
            <div class="container">
                <label>
                    ${this.getAttribute("label")}
                    ${
                        this.getAttribute("description")
                            ? `<i data-lucide="info"></i><div class="tool-tip"> ${this.getAttribute(
                                  "description",
                              )} </div>`
                            : ""
                    }
                </label>
                <select>
                    <option>Choose ${this.getAttribute("label")}</option>
                    ${optionsHTML}
                </select>
                ${this.getAttribute("required") == "true" ? `<required>Required<required>` : ""}
            </div>
        `;

        if (this.getAttribute("selected") != null) {
            this.shadow.querySelector("select").value = this.getAttribute("selected");
        }

        this.querySelector("select").addEventListener("change", (event) => {
            this.selected = event.target.value;
            this.dispatchEvent(new Event("change", { bubbless: true }));
        });
    }
}

customElements.define("single-select-dropdown", SingleSelectDropdown);
