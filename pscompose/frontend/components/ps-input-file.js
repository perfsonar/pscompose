import { PSInputText } from "./ps-input-text.js";

export class PSInputFile extends PSInputText {
    static get observedAttributes() {
        return [
            "class",
            "value",
            "placeholder",
            "description",
            "disabled",
            "error",
            "required",
            "accept",
            "subdesc",
        ];
    }

    constructor() {
        super();
        this.uploadArea = null;
        this._files = null;
    }

    connectedCallback() {
        super.connectedCallback();
    }

    get files() {
        return this._files || null;
    }

    set files(fileList) {
        this._files = fileList;  
        if (fileList && fileList.length) {
            this.value = Array.from(fileList).map(f => f.name).join(', ');
        } else {
            this.value = "";
        }
    }

    get accept() {
        return this.getAttribute("accept") ?? null;
    }
    set accept(v) {
        this.setAttribute("accept", v ?? "");
    }

    // TODO: Take on multiple files
    // get multiple() {
    //     return this.hasAttribute("multiple");
    // }
    // set multiple(v) {
    //     v ? this.setAttribute("multiple", "") : this.removeAttribute("multiple");
    // }

    get subdesc() {
        return this.getAttribute("subdesc") ?? null;
    }
    set subdesc(v) {
        this.setAttribute("subdesc", v ?? "");
    }

    _attachAdditionalListeners() {
        if (!this.uploadArea || !this.inputEl) return;

        this.uploadArea.addEventListener("click", (e) => {
            this.inputEl.click();
        });

        this.uploadArea.addEventListener("dragover", (e) => {
            e.preventDefault();
            this.uploadArea.classList.add("dragover");
        });

        this.uploadArea.addEventListener("dragleave", (e) => {
            e.preventDefault();
            this.uploadArea.classList.remove("dragover");
        });

        this.uploadArea.addEventListener("drop", (e) => {
            e.preventDefault();
            this.uploadArea.classList.remove("dragover");

            if (this.hasAttribute("disabled")) return;
            this.files = e.dataTransfer.files
            this.dispatchEvent(new Event("change", { bubbles: true }));
        });
    }

    render() {
        super.render();
        this.inputEl?.setAttribute("type", "file");
        if (this.accept !== null) this.inputEl?.setAttribute("accept", this.accept);


        const uploadArea = ` 
        <div class="upload-area">  
            <i data-lucide="upload" aria-hidden="true"></i>
            <div class="upload-text">
                <p>Click to select files or drag and drop files here</p>
                ${
                    this.subdesc
                        ? `<p class="subdesc">${this.subdesc}</p>`
                        : ""
                }
            </div>
        </div>
        `;
        this.wrapperEl.insertAdjacentHTML("beforeBegin", uploadArea);

        const selectedFile = `
            <p class="selected-files ${this.value ? '' : 'none'} ">
                ${this.value ?  this.value : `No Files Chosen`}
            </p>`
        this.wrapperEl.insertAdjacentHTML("beforeend", selectedFile);

        this.uploadArea = this.querySelector(".upload-area");
        this._attachAdditionalListeners();
        lucide.createIcons();
    }
}

customElements.define("ps-input-file", PSInputFile);
