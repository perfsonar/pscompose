import { PSSelect } from "./ps-select.js";

export class PSSelectChip extends PSSelect {
    render() {
        super.render();
        const optionsMap = new Map(this.options.map((opt) => [opt.const, opt.title]));

        if (this.disabled && this.value) {
            const tagHTML = `<span class="tag">
                ${optionsMap.get(this.value) || "Option Not Found"}
            </span>
            `;
            const tagDiv = `<div class="tags">${tagHTML}</div>`;
            this.querySelector(".form-container").insertAdjacentHTML("beforeend", tagDiv);
        }
    }
}

customElements.define("ps-select-chip", PSSelectChip);
