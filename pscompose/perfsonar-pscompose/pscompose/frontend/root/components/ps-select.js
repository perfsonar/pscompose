import { PSFormControl } from "./ps-form-control.js";

export class PSSelect extends PSFormControl {
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
        try {
            const options = JSON.parse(this.getAttribute("options")) || [];
            return options.length && typeof options[0] !== "object"
                ? options.map((opt) => ({ const: opt, title: opt }))
                : options;
        } catch {
            return [];
        }
    }
    set options(v) {
        this.setAttribute("options", v ?? "");
    }

    constructor() {
        super();
        this.slotEl = `
            <div class="ps-dropdown">
                <div class="ps-wrapper">
                    <input type="search" />
                    <ps-button id="down-btn" type="button" righticon="chevron-down" theme="Icon-Simple"></ps-button>
                </div>
                <ul class="ps-options" role="listbox"></ul>
            </div>
        `;
        this.inputEl = null;
        this.wrapperEl = null;
        this.optionsEl = null;
        this.actionBtn = null;
        this._closeDropdownBound = null;
        this._keydownBound = null;
    }

    connectedCallback() {
        super.connectedCallback();
        this._keydownBound = (e) => this._handleKeydown(e);
        this.addEventListener("keydown", this._keydownBound);
    }

    disconnectedCallback() {
        if (this._closeDropdownBound) {
            document.removeEventListener("click", this._closeDropdownBound);
            this._closeDropdownBound = null;
        }
        if (this._keydownBound) {
            this.removeEventListener("keydown", this._keydownBound);
            this._keydownBound = null;
        }
    }

    _handleKeydown(e) {
        const isOpen = this.optionsEl?.classList.contains("open");
        if (!isOpen && (e.key === "ArrowDown" || e.key === "ArrowUp")) {
            e.preventDefault();
            this.optionsEl?.classList.add("open");
            this._updateAriaExpanded(true);
            this.optionsEl?.querySelector("li")?.focus();
            return;
        }
        if (!isOpen) return;

        const items = [...(this.optionsEl?.querySelectorAll("li:not([style*='none'])") ?? [])];
        const focused = this.optionsEl?.querySelector("li:focus");
        const idx = focused ? items.indexOf(focused) : -1;

        if (e.key === "ArrowDown") {
            e.preventDefault();
            items[(idx + 1) % items.length]?.focus();
        } else if (e.key === "ArrowUp") {
            e.preventDefault();
            items[(idx - 1 + items.length) % items.length]?.focus();
        } else if (e.key === "Enter" && focused) {
            e.preventDefault();
            focused.click();
        } else if (e.key === "Escape") {
            e.preventDefault();
            this.optionsEl?.classList.remove("open");
            this._updateAriaExpanded(false);
            this.inputEl?.focus();
        }
    }

    _updateAriaExpanded(expanded) {
        this.wrapperEl?.setAttribute("aria-expanded", String(expanded));
    }

    attachToggleDropdown() {
        if (this.querySelector("#deselect-btn")) return;
        this.wrapperEl.addEventListener("click", () => {
            const willOpen = !this.optionsEl.classList.contains("open");
            this.optionsEl.classList.toggle("open");
            this._updateAriaExpanded(willOpen);
            if (!willOpen) this.markDirty();
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
            const willOpen = !this.optionsEl.classList.contains("open");
            this.optionsEl.classList.toggle("open");
            this._updateAriaExpanded(willOpen);
        });
        this.querySelector("#deselect-btn")?.addEventListener("click", () => {
            this.markDirty();
            this.removeAttribute("value");
            this.optionsEl.classList.remove("open");
            this._updateAriaExpanded(false);
            this.dispatchEvent(new Event("change", { bubbles: true }));
        });
    }

    attachSearchHandler() {
        this.inputEl.addEventListener("input", (event) => {
            this.optionsEl.classList.add("open");
            this._updateAriaExpanded(true);
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
        this.optionsEl.classList.remove("open");
        this._updateAriaExpanded(false);
        this.dispatchEvent(new Event("change", { bubbles: true }));
    }

    attachOptionClickHandler() {
        this.optionsEl.replaceChildren();
        if (this.options.length === 0) {
            const li = document.createElement("li");
            li.className = "no-options";
            li.textContent = "No options available";
            li.style.opacity = "0.5";
            li.style.cursor = "not-allowed";
            li.style.pointerEvents = "none";
            this.optionsEl.appendChild(li);
        } else {
            this.options.forEach((option) => {
                const li = document.createElement("li");
                li.dataset.value = option.const;
                li.textContent = option.title;
                li.setAttribute("tabindex", "-1");
                li.setAttribute("role", "option");
                li.setAttribute("aria-selected", String(option.const === this.value));
                if (option.const === this.value) li.classList.add("active");
                li.addEventListener("click", (e) => this.handleOptionClick(e));
                this.optionsEl.appendChild(li);
            });
        }
        if (!this._closeDropdownBound) {
            this._closeDropdownBound = (e) => this.closeDropdownOutside(e);
            document.addEventListener("click", this._closeDropdownBound);
        }
    }

    closeDropdownOutside(e) {
        if (!this.contains(e.target)) {
            this.optionsEl?.classList.remove("open");
            this._updateAriaExpanded(false);
        }
    }

    render() {
        if (!this.options) return;
        this.inputEl = this.querySelector("input");
        this.wrapperEl = this.querySelector(".ps-wrapper");
        this.optionsEl = this.querySelector(".ps-options");
        this.actionBtn = this.querySelector("ps-button");

        this.wrapperEl.setAttribute("aria-expanded", "false");

        const selectedOption = this.options.find((opt) => opt.const === this.value);
        if (selectedOption) {
            this.inputEl.value = selectedOption.title;
            this.actionBtn.setAttribute("id", "deselect-btn");
            this.actionBtn.setAttribute("righticon", "x");
        } else {
            this.inputEl.value = "";
            const ex = this.examples?.[0];
            this.inputEl.placeholder =
                ex != null
                    ? typeof ex === "string"
                        ? ex
                        : JSON.stringify(ex)
                    : `Select ${this.label}`;
        }

        this.attachOptionClickHandler();
        this.attachToggleDropdown();
        this.attachSearchHandler();
        this.attachDeselectHandler();
        lucide.createIcons();
    }
}

customElements.define("ps-select", PSSelect);
