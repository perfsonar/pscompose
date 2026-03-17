import { PSInputText } from "./ps-input-text.js";

export class PSInputCopy extends PSInputText {
    constructor() {
        super();
        this.slotEl = `
      <div class="wrapper">
        <input type="text" disabled />
        <ps-button type="button" id="copyBtn" theme="Icon-Simple" righticon="copy"></ps-button>
      </div>
    `;
        this.copyBtnEl = null;
    }

    attachCopyListener() {
        if (!this.copyBtnEl || !this.inputEl) return;

        this.copyBtnEl.addEventListener("click", async () => {
            try {
                await navigator.clipboard.writeText(this.value);
                this.dispatchEvent(
                    new CustomEvent("copied", {
                        detail: { value },
                        bubbles: true,
                    }),
                );
            } catch (err) {
                console.error("Failed to copy:", err);
                this.dispatchEvent(
                    new CustomEvent("copy-error", {
                        detail: { error: err },
                        bubbles: true,
                    }),
                );
            }
        });
    }

    render() {
        super.render();
        this.copyBtnEl = this.querySelector(".copy-btn");
        this.attachCopyListener();
    }
}

customElements.define("ps-input-copy", PSInputCopy);
