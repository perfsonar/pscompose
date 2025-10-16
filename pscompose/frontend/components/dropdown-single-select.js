export class SingleSelectDropdown extends HTMLElement {
    static observedAttributes = ["label", "options", "value"];

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

    attachDeselectHandler() {
        const deselectBtn = this.querySelector("#deselect-btn");
        if (deselectBtn) {
            deselectBtn.addEventListener("click", () => {
                this.removeAttribute("value");
                this.render();
                this.dispatchEvent(new Event("change", { bubbles: true }));
            });
        }
    }

    selectOption(value, title) {
        this.setAttribute("value", JSON.stringify(value));
        this.render();
        this.dispatchEvent(new Event("change", { bubbles: true }));
    }

    attachSearchHandler() {
        const searchInput = this.querySelector("#dropdown-search");
        const optionsList = this.querySelector(".options");
        if (!searchInput || !optionsList) return;

        searchInput.addEventListener("input", (event) => {
            const filter = event.target.value.toLowerCase();
            optionsList.querySelectorAll("li.option").forEach((option) => {
                const text = option.textContent.toLowerCase();
                option.style.display = text.includes(filter) ? "" : "none";
            });
        });
    }

    render() {
        const options = this.getAttribute("options")
            ? JSON.parse(this.getAttribute("options"))
            : [];
        const selectedValue = JSON.parse(this.getAttribute("value")) || "";
        const selectedOption = options ? options.find((opt) => opt.const === selectedValue) : null;

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
                <div class="dropdown">
                    <div class="select">
                        <input type="search" id="dropdown-search"
                        ${
                            selectedOption
                                ? `value="${selectedOption.title}"`
                                : `placeholder="Select ${this.getAttribute("label")}"`
                        }
                        />
                        <web-button id="down-btn" type="button" data-righticon="chevron-down" data-theme="Icon"></web-button>
                    </div>

                    <ul class="options">
                        ${
                            options
                                ? options
                                      .map(
                                          (option) => `
                            <li>
                                <div ${
                                    option.const == selectedValue
                                        ? 'class="option active"'
                                        : 'class="option"'
                                }
                                data-value="${option.const}"
                                >
                                ${option.title}
                                </div>
                                ${
                                    option.const == selectedValue
                                        ? '<web-button id="deselect-btn" type="button" data-righticon="x" data-theme="Icon-Small" />'
                                        : ""
                                }
                            </li>`,
                                      )
                                      .join("")
                                : ""
                        }
                    </ul>
                </div>
                ${
                    this.getAttribute("required") == "true"
                        ? `<div class="required">Required</div>`
                        : ""
                }
           </div>
        `;
        this.attachToggleDropdown();
        this.attachSearchHandler();
        this.attachDeselectHandler();
    }
}

customElements.define("dropdown-single-select", SingleSelectDropdown);
