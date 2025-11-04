export class excludesDropdown extends HTMLElement {
    static observedAttributes = ["label", "options", "value"];

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
        return Array.from(containers).map((singledropdown) => singledropdown.value);
    }

    getAvailableLocalAddresses() {
        const selectedLocalAddresses = this.getSelectedLocalAddresses();
        return this.allAddresses.filter((obj) => !selectedLocalAddresses.includes(obj.const));
    }

    attachMinusListeners() {
        this.querySelectorAll("#excludes-minus-btn").forEach((btn) => {
            btn.addEventListener("click", (e) => {
                e.target.closest(".excludes-container").classList.add("removing");
                e.target.closest(".excludes-container").remove();
                this.updateLocalAddressesOptions();
                this.updateSelectedValues();
            });
        });
    }

    attachDropdownListeners() {
        this.querySelectorAll("dropdown-single-select").forEach((dropdown) =>
            dropdown.addEventListener("change", () => {
                this.updateLocalAddressesOptions();
                this.updateSelectedValues();
            }),
        );
        this.querySelectorAll("dropdown-multi-select").forEach((dropdown) =>
            dropdown.addEventListener("change", () => {
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
                    singledropdown.setAttribute("value", JSON.stringify(currentSelectionValue));
                }
            },
        );
    }

    selectedSetUp() {
        this.selectedValues = this.getAttribute("value")
            ? JSON.parse(this.getAttribute("value"))
            : [];
    }

    // Update this.selectedValues as {"local-address": {"name": id }, "target-addresses": [{"name": id}, ...]} objects
    updateSelectedValues() {
        const selectedValues = [];
        const containers = this.querySelectorAll(".excludes-container");
        for (const container of containers) {
            const localDropdown = container.querySelector("dropdown-single-select");
            const targetDropdown = container.querySelector("dropdown-multi-select");
            const localAddressValue = localDropdown.getAttribute("value")
                ? { name: JSON.parse(localDropdown.getAttribute("value")) }
                : {};
            const targetAddressValue = targetDropdown.getAttribute("value")
                ? JSON.parse(targetDropdown.getAttribute("value")).map((id) => ({ name: id }))
                : [];
            selectedValues.push({
                "local-address": localAddressValue,
                "target-addresses": targetAddressValue,
            });
        }
        this.selectedValues = selectedValues;
        this.setAttribute("value", JSON.stringify(this.selectedValues));
        this.dispatchEvent(new Event("change", { bubbles: true }));
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

        newContainer.offsetHeight;
        newContainer.classList.add("show");

        // Attach listeners
        this.attachMinusListeners();
        this.attachDropdownListeners();
    }

    render() {
        const options = this.getAttribute("options")
            ? JSON.parse(this.getAttribute("options"))
            : [];
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
            <div class="excludes-container show">
                <div class="dropdown-container">
                    <dropdown-single-select
                        label="Local Address" 
                        options='${this.getAttribute("options")}'
                        value='${JSON.stringify(selectedLocalAddress)}'
                        >
                    </dropdown-single-select>
                    <dropdown-multi-select
                        label="Target Addresses" 
                        options='${this.getAttribute("options")}'
                        value='${JSON.stringify(selectedTargetAddresses)}'
                        >
                    </dropdown-multi-select>
                </div>
                <web-button id="excludes-minus-btn" type="button" data-righticon="trash-2" data-theme="Icon"></web-button>
            </div>`;
                      })
                      .join("")
                : "";

        const tableSelectedHTML =
            this.selectedValues.length > 0
                ? `<table class="excludes-table">
                <thead>
                <tr>
                    <th>Local Address</th>
                    <th>Target Addresses</th>
                </tr>
                </thead>
                <tbody>
                ${this.selectedValues
                    .map((val, index) => {
                        const selectedLocalAddress =
                            Object.keys(val["local-address"]).length !== 0
                                ? options.find((opt) => opt.const === val["local-address"]["name"])
                                      ?.title || "Option Not Found"
                                : "";
                        const selectedTargetAddresses = val["target-addresses"]
                            ? val["target-addresses"]
                                  .map((val) => {
                                      const label =
                                          options.find((opt) => opt.const === val["name"])?.title ||
                                          "Option Not Found";
                                      return `<span class="tag">${label}</span>`;
                                  })
                                  .join("")
                            : "";
                        return `
                        <tr data-index="${index}">
                        <td>${selectedLocalAddress}</td>
                        <td class="tags">${selectedTargetAddresses}</td>
                        </tr>
                    `;
                    })
                    .join("")}
                </tbody>
             </table> `
                : "";

        const desc = this.getAttribute("description");
        const descAttr = desc != null ? ` desc='${desc}'` : "";

        this.innerHTML = `
        <div class="container">
            <input-label label='${this.getAttribute("label")}'${descAttr}></input-label>
            ${selectedHTML}
            ${tableSelectedHTML}
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
