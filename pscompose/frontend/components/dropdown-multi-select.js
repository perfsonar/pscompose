import { SingleSelectDropdown } from "./dropdown-single-select.js";

export class MultiSelectDropdown extends SingleSelectDropdown {
    get output() {
        return this.getAttribute("output") ?? "";
    }
    set output(v) {
        this.setAttribute("output", v ?? "");
    }

    sanitizeOutput(values) {
        return this.getAttribute("output") === "object"
            ? values.map((val) => ({ name: val }))
            : values;
    }

    handleOptionClick(e) {
        const target = e.target.closest("li");
        if (!target || !target.dataset.value) return;

        const value = this.parseValue(target.dataset.value);

        if (value && !this.selectedValues.includes(value)) {
            this.selectedValues.unshift(value);
            this.value = this.sanitizeOutput(this.selectedValues);
            this.dispatchEvent(new Event("change", { bubbles: true }));
        }
    }

    attachTagsListeners() {
        this.querySelectorAll("#remove-tag").forEach((btn) => {
            btn.addEventListener("click", () => {
                const value = this.parseValue(btn.dataset.value);
                this.selectedValues = this.selectedValues.filter((v) => v !== value);
                this.value = this.sanitizeOutput(this.selectedValues);
                this.dispatchEvent(new Event("change", { bubbles: true }));
            });
        });
    }

    attachOptionClickHandler() {
        this.optionsEl.replaceChildren();

        const availableOptions = this.options.filter(
            (opt) => !this.selectedValues.includes(opt.const),
        );
        availableOptions.forEach((option) => {
            const li = document.createElement("li");
            li.dataset.value = option.const;
            li.textContent = option.title;
            if (option.const === this.value) li.classList.add("active");
            li.addEventListener("click", (e) => this.handleOptionClick(e));
            this.optionsEl.appendChild(li);
        });
    }

    selectedValuesSetUp() {
        if (!this.value) return [];
        return this.value.map((item) =>
            this.output === "object" ? item.name : item.const ?? item,
        );
    }

    render() {
        if (!this.options) return;

        this.selectedValues = this.selectedValuesSetUp();
        this.inputEl = this.querySelector("input");

        const optionsMap = new Map(this.options.map((opt) => [opt.const, opt.title]));

        this.optionsEl = this.querySelector(".options");
        this.wrapperEl = this.querySelector(".wrapper");
        this.inputEl.placeholder = `Select ${this.label}`;

        if (this.selectedValues.length > 0) {
            const tagsHTML = this.selectedValues
                .map(
                    (val) =>
                        `<span class="tag">
                        ${optionsMap.get(val) || "Option Not Found"}
                        <web-button id="remove-tag" type="button" value="${val}" righticon="x" theme="Icon-Small" />
                    </span>`,
                )
                .join("");
            const tags = `<div class="tags">${tagsHTML}</div>`;
            this.querySelector(".container").insertAdjacentHTML("beforeend", tags);
        }

        this.attachOptionClickHandler();
        this.attachToggleDropdown();
        this.attachTagsListeners();
        this.attachSearchHandler();
        this.attachDeselectHandler();
        lucide.createIcons();
    }
}

customElements.define("dropdown-multi-select", MultiSelectDropdown);
