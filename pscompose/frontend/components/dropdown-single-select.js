import { FormControl } from "./form-control.js";

export class SingleSelectDropdown extends FormControl {
    static get observedAttributes() {
        return [
            "class",
            "label",
            "options",
            "value",
            "placeholder",
            "description",
            "disabled",
            "error",
            "required",
        ];
    }

    get options() {
        const options = JSON.parse(this.getAttribute("options")) || [];
        return options.length && typeof options[0] !== "object"
            ? options.map((opt) => ({ const: opt, title: opt }))
            : options;
    }
    set options(v) {
        this.setAttribute("options", v ?? "");
    }

    constructor() {
        super();
        this.slotEl = `
            <div class="dropdown">
                <div class="wrapper">
                    <input type="search" />
                    <web-button id="down-btn" type="button" data-righticon="chevron-down" data-theme="Icon"></web-button>
                </div>
                <ul class="options"></ul>
            </div>
        `;
        this.inputEl = null;
        this.wrapperEl = null;
        this.optionsEl = null;
        this.actionBtn = null;
    }

    attachToggleDropdown() {
        if (this.querySelector("#deselect-btn")) return;
        this.wrapperEl.addEventListener("click", () => {
            if (this.optionsEl.classList.contains("open")) {
                this.optionsEl.classList.toggle("open");
                this.markDirty();
                return;
            }
            this.optionsEl.classList.toggle("open");
        });
    }

    parseValue(value) {
        if (value === "true") return true;
        if (value === "false") return false;
        if (!isNaN(value) && value.trim() !== "") return Number(value);
        return value;
    }

    attachDeselectHandler() {
        if (this.querySelector("#down-btn")) return;
        this.inputEl.addEventListener("click", () => {
            this.optionsEl.classList.toggle("open");
        });
        this.querySelector("#deselect-btn")?.addEventListener("click", () => {
            this.markDirty();
            this.removeAttribute("value");
            this.optionsEl.classList.remove("open");
            this.dispatchEvent(new Event("change", { bubbles: true }));
        });
    }

    attachSearchHandler() {
        this.inputEl.addEventListener("input", (event) => {
            this.optionsEl.classList.toggle("open");
            const filter = event.target.value.toLowerCase();
            this.optionsEl.querySelectorAll("li").forEach((li) => {
                li.style.display = li.textContent.toLowerCase().includes(filter) ? "" : "none";
            });
        });
    }

    handleOptionClick(e) {
        const target = e.target.closest("li");
        if (!target || !target.dataset.value) return;

        this.value = this.parseValue(target.dataset.value);
        this.dispatchEvent(new Event("change", { bubbles: true }));
    }

    attachOptionClickHandler() {
        this.optionsEl.replaceChildren();
        this.options.forEach((option) => {
            const li = document.createElement("li");
            li.dataset.value = option.const;
            li.textContent = option.title;
            if (option.const === this.value) li.classList.add("active");
            li.addEventListener("click", (e) => this.handleOptionClick(e));
            this.optionsEl.appendChild(li);
        });
    }

    render() {
        if (!this.options) return;
        this.inputEl = this.querySelector("input");
        this.wrapperEl = this.querySelector(".wrapper");
        this.optionsEl = this.querySelector(".options");
        this.actionBtn = this.querySelector("web-button");

        const selectedOption = this.options.find((opt) => opt.const === this.value);
        if (selectedOption) {
            this.inputEl.value = selectedOption.title;
            this.actionBtn.setAttribute("id", "deselect-btn");
            this.actionBtn.setAttribute("data-righticon", "x");
        } else {
            this.inputEl.value = "";
            this.inputEl.placeholder = `Select ${this.label}`;
        }

        this.attachOptionClickHandler();
        this.attachToggleDropdown();
        this.attachSearchHandler();
        this.attachDeselectHandler();
        lucide.createIcons();
    }
}

customElements.define("dropdown-single-select", SingleSelectDropdown);
