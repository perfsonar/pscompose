import { PSInputText } from "./ps-input-text.js";

class PSInputTextAutocomplete extends PSInputText {
    constructor() {
        super();
        this.slotEl = `
            <div class="dropdown">
                <div class="wrapper">
                    <input type="search" />
                </div>
                <ul class="options"></ul>
            </div>
        `;
        this.inputEl = null;
        this.wrapperEl = null;
        this.optionsEl = null;
        this.actionBtn = null;
        this.autocompleteOptions = [
            "{% address[0] %}",
            "{% address[1] %}",
            "{% pscheduler_address[0] %}",
            "{% pscheduler_address[1] %}",
            "{% flip %}",
            "{% localhost %}",
            "{% scheduled_by_address %}",
            "{% lead_bind_address[0] %}",
            "{% lead_bind_address[1] %}",
        ];
    }

    attachAutocompleteEventListener() {
        this.inputEl.addEventListener("input", (e) => this.handleInput(e));
        document.addEventListener("click", (e) => this.closeDropdownOutside(e));
    }

    handleInput(e) {
        const value = e.target.value;
        const cursorPos = e.target.selectionStart;

        const beforeCursor = value.slice(0, cursorPos);
        if (!beforeCursor.trim().startsWith("{%")) {
            this.closeDropdown();
            return;
        }

        const typed = beforeCursor.replace("{%", "").trim().toLowerCase();
        this.showAutocompleteDropdown(typed);
    }

    showAutocompleteDropdown(filterText = "") {
        this.optionsEl.innerHTML = "";
        this.optionsEl.classList.add("open");

        const filtered = this.autocompleteOptions.filter((opt) =>
            opt.toLowerCase().includes(filterText),
        );

        if (filtered.length === 0) {
            this.closeDropdown();
            return;
        }

        filtered.forEach((option) => {
            const li = document.createElement("li");
            li.textContent = option;
            li.dataset.value = option;

            li.addEventListener("mousedown", (e) => {
                e.preventDefault(); // prevents blur
                this.insertAutocompleteValue(option);
            });

            this.optionsEl.appendChild(li);
        });
    }

    insertAutocompleteValue(value) {
        this.inputEl.value = value;
        this.inputEl.dispatchEvent(new Event("change", { bubbles: true }));
        this.closeDropdown();
    }

    closeDropdownOutside(e) {
        if (!this.contains(e.target)) {
            this.closeDropdown();
        }
    }

    closeDropdown() {
        this.optionsEl.classList.remove("open");
        this.optionsEl.innerHTML = "";
    }

    render() {
        super.render();

        this.inputEl = this.querySelector("input");
        this.wrapperEl = this.querySelector(".wrapper");
        this.optionsEl = this.querySelector(".options");

        this.attachAutocompleteEventListener();
    }
}

customElements.define("ps-input-text-autocomplete", PSInputTextAutocomplete);