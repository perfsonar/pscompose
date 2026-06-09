const SI_SUFFIXES = {
    "": 1,
    k: 1000,
    m: 1000000,
    g: 1000000000,
    t: 1000000000000,
    p: 1000000000000000,
    e: 1000000000000000000,
    z: 1000000000000000000000,
    y: 1000000000000000000000000,
    ki: 1024,
    mi: 1048576,
    gi: 1073741824,
    ti: 1099511627776,
    pi: 1125899906842624,
    ei: 1152921504606846976,
    zi: 1180591620717411303424,
    yi: 1208925819614629174706176,
};

export function parseSI(raw) {
    if (raw === null || raw === undefined) return NaN;
    const str = raw.toString().trim();
    if (str === "") return NaN;

    const match = str.match(/^([+-]?\d+(\.\d+)?)\s*([a-z]{1,2})?$/i);
    if (!match) return NaN;

    const numeric = parseFloat(match[1]);
    const suffix = (match[3] ?? "").toLowerCase();

    const multiplier = SI_SUFFIXES[suffix];
    if (multiplier === undefined) return NaN;

    return numeric * multiplier;
}

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
        this._siHandler = null;
    }

    disconnectedCallback() {
        super.disconnectedCallback?.();
        this._addBtn?.removeEventListener("click", this._onAdd);
        this._minusBtn?.removeEventListener("click", this._onMinus);
        if (this._siHandler) {
            this.inputEl?.removeEventListener("change", this._siHandler);
            this.inputEl?.removeEventListener("blur", this._siHandler);
        }
    }

    attachEventListener() {
        this.inputEl?.addEventListener("change", () => {
            this.markDirty();
            const resolved = parseSI(this.inputEl.value);
            this.value = isNaN(resolved) ? undefined : resolved;
            this.dispatchEvent(new Event("change", { bubbles: true }));
        });
    }

    _attachAdditionalListeners() {
        this._onAdd = () => this._changeValue(1);
        this._onMinus = () => this._changeValue(-1);
        this._addBtn.addEventListener("click", this._onAdd);
        this._minusBtn.addEventListener("click", this._onMinus);

        this._siHandler = () => this._resolveSI();
        this.inputEl.addEventListener("change", this._siHandler);
        this.inputEl.addEventListener("blur", this._siHandler);
    }

    _resolveSI() {
        const raw = this.inputEl.value.trim();
        if (raw === "" || /^[+-]?\d+(\.\d+)?$/.test(raw)) return;

        const resolved = parseSI(raw);
        if (isNaN(resolved)) return;

        this.inputEl.value = resolved;
        this.inputEl.dispatchEvent(new Event("change", { bubbles: true }));
    }

    _changeValue = (direction) => {
        this._resolveSI();

        const step = this.inputEl.hasAttribute("step") ? parseFloat(this.inputEl.step) : 1;
        const min = this.inputEl.hasAttribute("min") ? parseFloat(this.inputEl.min) : -Infinity;
        const max = this.inputEl.hasAttribute("max") ? parseFloat(this.inputEl.max) : Infinity;
        const currentValue = parseFloat(this.inputEl.value);

        if (isNaN(currentValue)) return;

        let newValue = currentValue + direction * step;
        newValue = Math.min(max, Math.max(min, newValue));
        const decimals = (step.toString().split(".")[1] || "").length;
        this.inputEl.value = parseFloat(newValue.toFixed(decimals));
        this.inputEl.dispatchEvent(new Event("change", { bubbles: true }));
    };

    render() {
        super.render();
        this.inputEl?.setAttribute("type", "text");
        this.inputEl?.setAttribute("inputmode", "decimal");

        if (this.min !== null) this.inputEl?.setAttribute("min", this.min);
        if (this.max !== null) this.inputEl?.setAttribute("max", this.max);
        if (this.step !== null) this.inputEl?.setAttribute("step", this.step);

        const actionBtns = `
            <div class="buttons">
                <ps-button type="button" id="addBtn" theme="Icon-Simple" righticon="plus"></ps-button>
                <ps-button type="button" id="minusBtn" theme="Icon-Simple" righticon="minus"></ps-button>
            </div>`;
        this.wrapperEl.insertAdjacentHTML("beforeend", actionBtns);

        this._addBtn = this.wrapperEl.querySelector("#addBtn");
        this._minusBtn = this.wrapperEl.querySelector("#minusBtn");
        this._attachAdditionalListeners();
    }
}

customElements.define("ps-input-number", PSInputNumber);
