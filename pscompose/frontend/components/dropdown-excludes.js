export class excludesDropdown extends HTMLElement {
    static observedAttributes = ["label", "options", "selected"];

    constructor() {
        super();
        this.selectedValues = [];
    }

    connectedCallback() {
        this.allAddresses = this.getAttribute("options")
            ? JSON.parse(this.getAttribute("options"))
            : [];
        this.selectedSetUp();
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
                e.target.closest(".excludes-container").remove();
                this.updateLocalAddressesOptions();
                this.updateSelectedValues();
            });
        });
    }

    attachDropdownListeners() {
        this.querySelectorAll("dropdown-single-select").forEach((dropdown) =>
            dropdown.addEventListener("select", () => {
                this.updateLocalAddressesOptions();
                this.updateSelectedValues();
            }),
        );
        this.querySelectorAll("dropdown-multi-select").forEach((dropdown) =>
            dropdown.addEventListener("select", () => {
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

    selectedSetUp() {
        this.selectedValues = this.getAttribute("selected")
            ? JSON.parse(this.getAttribute("selected"))
            : [];
    }

    // Update this.selectedValues as {"local-address": {"name": id }, "target-addresses": [{"name": id}, ...]} objects
    updateSelectedValues() {
        const selectedValues = [];
        const containers = this.querySelectorAll(".excludes-container");
        for (const container of containers) {
            const localDropdown = container.querySelector("dropdown-single-select");
            const targetDropdown = container.querySelector("dropdown-multi-select");
            const localAddressValue = localDropdown.getAttribute("selected")
                ? { name: localDropdown.getAttribute("selected") }
                : {};
            const targetAddressValue = targetDropdown.getAttribute("selected")
                ? JSON.parse(targetDropdown.getAttribute("selected")).map((id) => ({ name: id }))
                : [];
            selectedValues.push({
                "local-address": localAddressValue,
                "target-addresses": targetAddressValue,
            });
        }
        this.selectedValues = selectedValues;
        this.setAttribute("selected", JSON.stringify(this.selectedValues));
        this.dispatchEvent(new Event("select", { bubbles: true }));
    }

    addExcludesContainer() {
        const newContainer = document.createElement("div");
        newContainer.classList.add("excludes-container");
        newContainer.innerHTML = `
            <div class="dropdown-container">
                <dropdown-single-select
                    label="Local Address" 
                    options='${JSON.stringify(this.getAvailableLocalAddresses())}'
                    >
                </dropdown-single-select>
                <dropdown-multi-select
                    label="Target Addresses" 
                    options='${this.getAttribute("options")}'
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
        const selectedHTML =
            this.selectedValues.length > 0
                ? this.selectedValues
                      .map((val) => {
                          const selectedLocalAddress =
                              Object.keys(val["local-address"]).length != 0
                                  ? val["local-address"]["name"]
                                  : "";
                          const selectedTargetAddresses = val["target-addresses"]
                              ? val["target-addresses"].map((targetAdd) => targetAdd["name"])
                              : "";
                          return `
            <div class="excludes-container">
                <div class="dropdown-container">
                    <dropdown-single-select
                        label="Local Address" 
                        options='${this.getAttribute("options")}'
                        selected=${selectedLocalAddress}
                        >
                    </dropdown-single-select>
                    <dropdown-multi-select
                        label="Target Addresses" 
                        options='${this.getAttribute("options")}'
                        selected=${JSON.stringify(selectedTargetAddresses)}
                        >
                    </dropdown-multi-select>
                </div>
                <web-button id="excludes-minus-btn" type="button" data-righticon="trash-2" data-theme="Icon"></web-button>
            </div>`;
                      })
                      .join("")
                : "";

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
            ${selectedHTML}
        </div>
        <web-button id="excludes-add-btn" type="button" data-label="Add" data-lefticon="plus" data-theme="Small"></web-button>
    `;
        this.querySelector("#excludes-add-btn").addEventListener(
            "click",
            this.addExcludesContainer.bind(this),
        );

        this.updateLocalAddressesOptions();
        this.attachDropdownListeners();
        this.attachMinusListeners();
    }
}

customElements.define("dropdown-excludes", excludesDropdown);
