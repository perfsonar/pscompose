import { PSFormControl } from "./ps-form-control.js";

export class PSInputTextMulti extends PSFormControl {
    constructor() {
        super();
        this.slotEl = `
            <div class="inputs-container">
                <ps-button id="input-text-add-btn" type="button" label="Add" lefticon="plus" theme="Small"></ps-button>
            </div>
        `;
        this.inputEls = [];
    }

    syncValue() {
        const inputs = Array.from(this.containerEl.querySelectorAll("input"));
        const ar = inputs.map((i) => i.value).filter(Boolean);
        this.value = ar;
        this.dispatchEvent(new Event("change", { bubbles: true }));
    }

    addInput(value = "") {
        const input = document.createElement("input");
        input.type = "text";
        input.placeholder = `Enter ${this.label}`;
        if (value) input.value = value;

        input.addEventListener("change", () => {
            this.syncValue();
        });

        const row = document.createElement("div");
        row.classList.add("wrapper");

        const removeBtn = document.createElement("ps-button");
        removeBtn.setAttribute("type", "button");
        removeBtn.setAttribute("righticon", "x");
        removeBtn.setAttribute("theme", "Icon-Small");
        removeBtn.addEventListener("click", () => {
            row.remove();
            this.syncValue();
        });

        row.appendChild(input);
        row.appendChild(removeBtn);

        const addBtn = this.querySelector("#input-text-add-btn");
        this.containerEl.insertBefore(row, addBtn);
    }

    render() {
        this.containerEl = this.querySelector(".inputs-container");

        const initialValues = this.value.length > 0 ? this.value : [""];
        initialValues.forEach((v) => this.addInput(v));

        this.querySelector("#input-text-add-btn").addEventListener("click", () => {
            this.addInput();
        });
    }
}

customElements.define("ps-input-text-multi", PSInputTextMulti);
