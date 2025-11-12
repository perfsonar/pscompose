export class InputMessage extends HTMLElement {
    static get observedAttributes() {
        return ["required", "error"];
    }

    get error() {
        return this.getAttribute("error") ?? "";
    }
    set error(v) {
        this.setAttribute("error", v ?? "");
    }

    get required() {
        return this.hasAttribute("required");
    }
    set required(v) {
        v ? this.setAttribute("required", "") : this.removeAttribute("required");
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
            <div class='error ${this.error ? "show" : ""}'>${this.error}</div>
            <div class="required">${this.required ? "Required" : ""}</div>
    `;
    }
}

customElements.define("input-message", InputMessage);
