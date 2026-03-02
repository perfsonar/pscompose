export class PSInputLabel extends HTMLElement {
    static get observedAttributes() {
        ["label", "desc"];
    }

    get label() {
        return this.getAttribute("label") ?? "";
    }
    set label(v) {
        this.setAttribute("label", v ?? "");
    }

    get desc() {
        return this.getAttribute("desc") ?? "";
    }
    set desc(v) {
        this.setAttribute("desc", v ?? "");
    }

    constructor() {
        super();
    }

    connectedCallback() {
        this.render();
    }

    attributeChangedCallback(name, oldVal, newVal) {
        if (oldVal !== newVal) this.render();
    }

    render() {
        this.innerHTML = `                
            <label>
                ${this.label}
                ${this.desc ? `<ps-tooltip desc="${this.desc}"> </ps-tooltip>` : ""}
            </label>`;
    }
}

customElements.define("ps-input-label", PSInputLabel);
