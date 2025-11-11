export class InputLabel extends HTMLElement {
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
                ${this.desc ? `<web-tooltip desc="${this.desc}"> </web-tooltip>` : ""}
            </label>`;
    }
}

customElements.define("input-label", InputLabel);
