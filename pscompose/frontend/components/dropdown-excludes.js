export class excludesDropdown extends HTMLElement {
    static observedAttributes = ["label", "options", "selected"];

    constructor() {
        super();
        this.selectedValues = [];
        this.allAddresses = this.getAttribute("options")
            ? JSON.parse(this.getAttribute("options"))
            : [];
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

    getSelectedLocalAddresses() {
        const containers = this.querySelectorAll(
            ".container .excludes-container dropdown-single-select",
        );
        return Array.from(containers).map((singledropdown) => singledropdown.selected);
    }

    getAvailableLocalAddresses() {
        const selectedLocalAddresses = this.getSelectedLocalAddresses();
        return this.allAddresses.filter((obj) => !selectedLocalAddresses.includes(obj.const));
    }

    attachMinusListeners() {
        this.querySelectorAll("#excludes-minus-btn").forEach((btn) => {
            btn.addEventListener("click", (e) => {
                const container = e.target.closest(".excludes-container");
                if (this.querySelectorAll(".excludes-container").length > 1) {
                    container.remove();
                    this.updateLocalAddressesOptions();
                    this.updateSelectedValues();
                }
            });
        });
    }

    attachDropdownListeners() {
        this.querySelectorAll("dropdown-single-select, dropdown-multi-select").forEach((dropdown) =>
            dropdown.addEventListener("change", () => {
                this.updateLocalAddressesOptions();
                this.updateSelectedValues();
            }),
        );
    }

    // Update local address dropdown options to exclude already selected local addresses
    updateLocalAddressesOptions() {
        this.querySelectorAll(".container .excludes-container dropdown-single-select").forEach(
            (singledropdown) => {
                const currentSelectionValue = singledropdown.selected; // "const" value
                const currentSelection = this.allAddresses.find(
                    (opt) => opt.const === currentSelectionValue,
                ); // {const, title} object

                if (currentSelection) {
                    const newOptions = [...this.getAvailableLocalAddresses(), currentSelection]; // Include current selection
                    newOptions.sort((a, b) => a.title.localeCompare(b.title)); // Sort options alphabetically to keep order consistent
                    singledropdown.setAttribute("options", JSON.stringify(newOptions));
                    singledropdown.setAttribute("selected", currentSelectionValue);
                }
            },
        );
    }

    // Update this.selectedValues as {"local-address": {"name": "..."}, "target-addresses": [{"name": "..."}, ...]} objects
    updateSelectedValues() {
        this.selectedValues = Array.from(this.querySelectorAll(".excludes-container")).map(
            (container) => {
                const localDropdown = container.querySelector("dropdown-single-select");
                const targetDropdown = container.querySelector("dropdown-multi-select");
                const localAddressName = localDropdown.hasAttribute("selected")
                    ? this.allAddresses.find(
                          (opt) => opt.const === localDropdown.getAttribute("selected"),
                      )["title"]
                    : null;

                let targetAddressValue = [];
                let targetAddressName = [];
                if (targetDropdown.getAttribute("selected") && localAddressName) {
                    // only return if both local and target addresses are selected
                    targetAddressValue = JSON.parse(targetDropdown.getAttribute("selected"));
                    targetAddressName = this.allAddresses
                        .filter((opt) => targetAddressValue.includes(opt.const))
                        .map((opt) => opt.title);
                    return {
                        "local-address": { name: localAddressName },
                        "target-addresses": targetAddressName.map((name) => ({ name: name })),
                    };
                }
            },
        );
    }

    addExcludesContainer() {
        const newContainer = document.createElement("div");
        newContainer.classList.add("excludes-container");
        newContainer.innerHTML = `
            <div class="dropdown-container">
                <dropdown-single-select
                    label="Local Addresses" 
                    options=${JSON.stringify(this.getAvailableLocalAddresses())}
                    >
                </dropdown-single-select>
                <dropdown-multi-select
                    label="Target Addresses" 
                    options=${this.getAttribute("options")}
                    >
                </dropdown-multi-select>
            </div>
            <web-button id="excludes-minus-btn" type="button" data-righticon="trash-2" data-theme="Icon"></web-button>
        `;
        this.querySelector(".container").appendChild(newContainer);

        // Attach listeners
        this.attachMinusListeners();
        this.attachDropdownListeners();
    }

    render() {
        this.innerHTML = `
        <div class="container">
            <label>
                ${this.getAttribute("label")}
                ${
                    this.getAttribute("description")
                        ? `<i data-lucide="info"></i>
                <div class="tool-tip"> ${this.getAttribute("description")} </div> `
                        : ""
                }
            </label>
            <div class="excludes-container">
                <div class="dropdown-container">
                    <dropdown-single-select
                        label="Local Addresses" 
                        options='${this.getAttribute("options")}'
                        >
                    </dropdown-single-select>
                    <dropdown-multi-select
                        label="Target Addresses" 
                        options='${this.getAttribute("options")}'
                    >
                    </dropdown-multi-select>
                </div>
                <web-button id="excludes-minus-btn" type="button" data-righticon="trash-2" data-theme="Icon"></web-button>
            </div>
        </div>
        <web-button id="excludes-add-btn" type="button" data-label="Add" data-lefticon="plus" data-theme="Small"></web-button>
    `;
        this.querySelector("#excludes-add-btn").addEventListener(
            "click",
            this.addExcludesContainer.bind(this),
        );

        this.attachDropdownListeners();
        this.attachMinusListeners();
    }
}

customElements.define("dropdown-excludes", excludesDropdown);
