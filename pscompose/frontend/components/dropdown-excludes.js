import { FormControl } from "./form-control.js";

export class excludesDropdown extends FormControl {
    static get observedAttributes() {
        return [
            "class",
            "label",
            "options",
            "value",
            "description",
            "disabled",
            "error",
            "required",
        ];
    }

    get options() {
        return JSON.parse(this.getAttribute("options")) || [];
    }
    set options(v) {
        this.setAttribute("options", v ?? "");
    }

    constructor() {
        super();
        this.slotEl = `
            <web-button id="excludes-add-btn" type="button" label="Add" lefticon="plus" theme="Small"></web-button>
        `;
    }

    getSelectedLocalAddresses() {
        return Array.from(this.querySelectorAll("dropdown-single-select")).map(
            (dropdown) => dropdown.value,
        );
    }

    getAvailableLocalAddresses() {
        const selected = this.getSelectedLocalAddresses();
        return this.options.filter((opt) => !selected.includes(opt.const));
    }

    attachMinusListeners() {
        this.querySelectorAll("#excludes-minus-btn").forEach((btn) => {
            btn.onclick = (e) => {
                const container = e.target.closest(".excludes-container");
                if (!container) return;
                container.classList.add("removing");
                container.remove();
                this.updateLocalAddressesOptions();
                this.updateSelectedValues();
            };
        });
    }

    attachDropdownListeners() {
        this.querySelectorAll("dropdown-single-select").forEach((dropdown) => {
            dropdown.onchange = () => {
                this.updateLocalAddressesOptions();
                this.updateSelectedValues();
            };
        });

        this.querySelectorAll("dropdown-multi-select").forEach((dropdown) => {
            dropdown.onchange = () => this.updateSelectedValues();
        });
    }

    updateLocalAddressesOptions() {
        this.querySelectorAll("dropdown-single-select").forEach((dropdown) => {
            const currentValue = dropdown.value;
            const currentSelection = this.options.find((opt) => opt.const === currentValue);
            const available = [...this.getAvailableLocalAddresses()];

            if (currentSelection) {
                available.push(currentSelection);
                available.sort((a, b) => a.title.localeCompare(b.title));
                dropdown.options = JSON.stringify(available);
                dropdown.value = currentSelection.const;
            }
        });
    }

    // Update this.selectedValues as {"local-address": {"name": id }, "target-addresses": [{"name": id}, ...]} objects
    updateSelectedValues() {
        const selectedValues = Array.from(this.querySelectorAll(".excludes-container")).map(
            (container) => {
                const localDropdown = container.querySelector("dropdown-single-select");
                const targetDropdown = container.querySelector("dropdown-multi-select");

                const localValue = localDropdown?.getAttribute("value");
                const targetValue = targetDropdown?.getAttribute("value");

                return {
                    "local-address": localValue ? { name: JSON.parse(localValue) } : {},
                    "target-addresses": targetValue
                        ? JSON.parse(targetValue).map((id) => ({ name: id }))
                        : [],
                };
            },
        );

        this.selectedValues = selectedValues;
        this.setAttribute("value", JSON.stringify(selectedValues));
        this.dispatchEvent(new Event("change", { bubbles: true }));
    }

    addExcludesContainer() {
        const newContainer = document.createElement("div");
        newContainer.classList.add("excludes-container");
        newContainer.innerHTML = `
            <div class="dropdown-container">
                <dropdown-single-select label="Local Address" options='${JSON.stringify(
                    this.getAvailableLocalAddresses(),
                )}'>
                </dropdown-single-select>
                <dropdown-multi-select label="Target Addresses" options='${JSON.stringify(
                    this.options,
                )}'>
                </dropdown-multi-select>
            </div>
            <web-button id="excludes-minus-btn" type="button" righticon="trash-2" theme="Icon"></web-button>
        `;

        const container = this.querySelector(".form-container");
        const children = container.children;

        container.insertBefore(newContainer, children[children.length - 2]);

        newContainer.offsetHeight;
        newContainer.classList.add("show");

        // Attach listeners
        this.attachMinusListeners();
        this.attachDropdownListeners();
    }

    attachAddBtn() {
        this.querySelector("#excludes-add-btn")?.addEventListener(
            "click",
            this.addExcludesContainer.bind(this),
        );
    }

    render() {
        const container = this.querySelector(".form-container");
        if (!container) return;

        const options = this.options;
        const selectedValues = Array.isArray(this.value) ? this.value : [];

        const optionsMap = new Map(options.map((opt) => [opt.const, opt.title]));
        const labelElement = container.querySelector("input-label");

        container
            .querySelectorAll(".excludes-container, .excludes-table")
            .forEach((el) => el.remove());

        if (!this.disabled && selectedValues.length) {
            const selectedHTML = selectedValues
                .map((val) => {
                    const localAddress = val["local-address"]?.name || "";
                    const targetAddresses = val["target-addresses"]?.map((t) => t.name) || [];

                    return `
                    <div class="excludes-container show">
                        <div class="dropdown-container">
                            <dropdown-single-select
                                label="Local Address"
                                options='${JSON.stringify(options)}'
                                value='${JSON.stringify(localAddress)}'>
                            </dropdown-single-select>
                            <dropdown-multi-select
                                label="Target Addresses"
                                options='${JSON.stringify(options)}'
                                value='${JSON.stringify(targetAddresses)}'>
                            </dropdown-multi-select>
                        </div>
                        <web-button
                            id="excludes-minus-btn"
                            type="button"
                            righticon="trash-2"
                            theme="Icon">
                        </web-button>
                    </div>`;
                })
                .join("");

            labelElement.insertAdjacentHTML("afterend", selectedHTML);
        }

        if (this.disabled && selectedValues.length) {
            const tableRows = selectedValues
                .map((val, index) => {
                    const localAddress =
                        optionsMap.get(val["local-address"]?.name) || "Option Not Found";
                    const targetHTML = val["target-addresses"]
                        .map(
                            (t) =>
                                `<span class="tag">${
                                    optionsMap.get(t.name) || "Option Not Found"
                                }</span>`,
                        )
                        .join("");

                    return `
                    <tr data-index="${index}">
                        <td>${localAddress}</td>
                        <td class="tags">${targetHTML}</td>
                    </tr>`;
                })
                .join("");

            const tableHTML = `
                <table class="excludes-table">
                    <thead>
                        <tr>
                            <th>Local Address</th>
                            <th>Target Addresses</th>
                        </tr>
                    </thead>
                    <tbody>${tableRows}</tbody>
                </table>
            `;
            labelElement.insertAdjacentHTML("afterend", tableHTML);
        }

        this.attachAddBtn();
        this.updateLocalAddressesOptions();
        this.attachDropdownListeners();
        this.attachMinusListeners();
    }
}

customElements.define("dropdown-excludes", excludesDropdown);
