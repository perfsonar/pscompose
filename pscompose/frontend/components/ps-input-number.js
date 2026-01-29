import { PSInputText } from "./ps-input-text.js";

export class PSInputNumber extends PSInputText {
    static get observedAttributes() {
        return [
            "class",
            "value",
            "placeholder",
            "description",
            "disabled",
            "error",
            "required",
            "step",
            "min",
            "max",
        ];
    }

    get min() {
        return this.getAttribute("min") ?? null;
    }
    set min(v) {
        this.setAttribute("min", v ?? "");
    }

    get max() {
        return this.getAttribute("max") ?? null;
    }
    set max(v) {
        this.setAttribute("max", v ?? "");
    }

    get step() {
        return this.getAttribute("step") ?? null;
    }
    set step(v) {
        this.setAttribute("step", v ?? "");
    }

    constructor() {
        super();
        this._addBtn = null;
        this._minusBtn = null;
    }

    disconnectedCallback() {
        this._addBtn.removeEventListener("click", () => this._changeValue(1));
        this._minusBtn.removeEventListener("click", () => this._changeValue(-1));
    }

    _attachAdditionalListeners() {
        this._addBtn.addEventListener("click", () => this._changeValue(1));
        this._minusBtn.addEventListener("click", () => this._changeValue(-1));
    }

    _changeValue = (direction) => {
        const step = this.inputEl.hasAttribute("step") ? parseFloat(this.inputEl.step) : 1;
        const min = this.inputEl.hasAttribute("min") ? parseFloat(this.inputEl.min) : -Infinity;
        const max = this.inputEl.hasAttribute("max") ? parseFloat(this.inputEl.max) : Infinity;
        let currentValue = parseFloat(this.inputEl.value);

        if (isNaN(currentValue)) currentValue = 0;

        let newValue = currentValue + direction * step;
        newValue = Math.min(max, Math.max(min, newValue));
        this.inputEl.value = newValue;
    };

    render() {
        super.render();
        this.inputEl?.setAttribute("type", "number");
        if (this.min !== null) this.inputEl?.setAttribute("min", this.min);
        if (this.max !== null) this.inputEl?.setAttribute("max", this.max);
        if (this.step !== null) this.inputEl?.setAttribute("step", this.step);

        const actionBtns = ` 
            <div class="buttons">
                <ps-button type="button" id="addBtn" theme="Icon" righticon="plus"></ps-button>
                <ps-button type="button" id="minusBtn" theme="Icon" righticon="minus"></ps-button>
            </div>`;
        this.wrapperEl.insertAdjacentHTML("beforeend", actionBtns);

        this._addBtn = this.wrapperEl.querySelector("#addBtn");
        this._minusBtn = this.wrapperEl.querySelector("#minusBtn");
        this._attachAdditionalListeners();
    }
}

customElements.define("ps-input-number", PSInputNumber);
