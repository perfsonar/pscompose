export class MultiSelectDropdown extends HTMLElement {
    static observedAttributes = ["label", "options", "selected", "output"];

    constructor() {
        super();
        this.selectedValues = [];
    }

    connectedCallback() {
        this.selectedSetUp();
        this.render();
        lucide.createIcons();
    }

    attributeChangedCallback(name, oldValue, newValue) {
        this[name] = newValue;
        this.render();
        lucide.createIcons();
    }

    sanitizeOutput(sv) {
        if (this.getAttribute("output") == "object") {
            let mapping = sv.map((val) => {
                return { name: val };
            });
            return mapping;
        }
        return sv;
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
            item.onclick = () => {
                const value = item.getAttribute("data-value");
                if (value && !this.selectedValues.includes(value)) {
                    this.selectedValues.unshift(value); // Value to selectedValue array
                    this.setAttribute(
                        "selected",
                        JSON.stringify(this.sanitizeOutput(this.selectedValues)),
                    ); // set Attribute
                    this.dispatchEvent(new Event("select", { bubbles: true }));
                    this.render();
                    lucide.createIcons();
                }
            };
        });
    }

    attachTagsListeners() {
        this.querySelectorAll(".tag .remove-tag").forEach((btn) => {
            btn.addEventListener("click", () => {
                const value = btn.getAttribute("data-value");
                this.selectedValues = this.selectedValues.filter((v) => v !== value);
                this.setAttribute(
                    "selected",
                    JSON.stringify(this.sanitizeOutput(this.selectedValues)),
                ); // set Attribute
                this.dispatchEvent(new Event("select", { bubbles: true }));
                this.render();
                lucide.createIcons();
            });
        });
    }

    selectedSetUp() {
        const selected = this.getAttribute("selected")
            ? JSON.parse(this.getAttribute("selected"))
            : [];
        if (this.getAttribute("output") == "object") {
            this.selectedValues = selected.map((item) =>
                typeof item === "object" ? item.name : item,
            );
        } else {
            this.selectedValues = selected.map((item) =>
                typeof item === "object" ? item.const : item,
            );
        }
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
        const availableOptions = options
            ? options.filter((opt) => !this.selectedValues.includes(opt.const))
            : [];

        const tagsHTML = this.selectedValues
            .map((val) => {
                const label = options.find((opt) => opt.const === val)?.title || val;
                return `
                    <span class="tag">
                        ${label}
                        <button class="remove-tag" data-value="${val}">
                            <i style="width: 16px; height: 16px; color: white;" data-lucide="x"></i>
                        </button>
                    </span>`;
            })
            .join("");

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
                        <input type="search" id="dropdown-search" placeholder='Select ${this.getAttribute(
                            "label",
                        )}'/>
                        <web-button id="down-btn" type="button" data-righticon="chevron-down" data-theme="Icon"></web-button>
                    </div>
                    <ul class="options">
                        ${
                            availableOptions
                                ? availableOptions
                                      .map(
                                          (option) => `
                            <li class="option"
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
                <div class="tags">${tagsHTML}</div>
            </div>
        `;
        this.attachToggleDropdown();
        this.attachOptionListeners();
        this.attachTagsListeners();
        this.attachSearchHandler();
    }
}

customElements.define("dropdown-multi-select", MultiSelectDropdown);
