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

    attachToggleDropdown() {
        const options = this.querySelector(".options");
        if (!options) return;
        this.querySelector(".select").addEventListener("click", () => {
            options.classList.toggle("open");
            this.querySelector(".dropdown").classList.toggle("active");
            this.attachOptionListeners();
        });
    }

    attachOptionListeners() {
        document.querySelectorAll(".option").forEach((item) => {
            item.onclick = () =>
                this.selectOption(item.getAttribute("data-value"), item.textContent);
        });
    }

    selectOption(value, title) {
        this.setAttribute("selected", value);
        this.render();
        this.dispatchEvent(new Event("change", { bubbles: true }));
    }

    render() {
        const options = this.getAttribute("options")
            ? JSON.parse(this.getAttribute("options"))
            : [];
        const selectedValue = this.getAttribute("selected") || "";
        const selectedOption = options ? options.find((opt) => opt.const === selectedValue) : null;

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
                <div class="dropdown">
                    <div class="select">
                        ${
                            selectedOption
                                ? selectedOption.title
                                : `<p style="color: var(--copyAlt-color)">Select ${this.getAttribute(
                                      "label",
                                  )}</p>`
                        }
                        <web-button id="down-btn" type="button" data-righticon="chevron-down" data-theme="Icon"></web-button>
                    </div>
                    <ul class="options">
                        ${
                            options
                                ? options
                                      .map(
                                          (option) => `
                            <li ${
                                option.const == selectedValue
                                    ? 'class="option active"'
                                    : 'class="option"'
                            }
                            data-value="${option.const}">
                            ${option.title}
                            </li>
                        `,
                                      )
                                      .join("")
                                : ""
                        }
                    </ul>
                </div>
                ${this.getAttribute("required") == "true" ? `<required>Required<required>` : ""}
            </div>
        `;
        this.attachToggleDropdown();
    }
}

customElements.define("dropdown-single-select", SingleSelectDropdown);
