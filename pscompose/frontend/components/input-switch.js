export class InputSwitch extends HTMLElement {
    static get observedAttributes() {
        return ["checked"];
    }
    
    get checked() {
        return this.hasAttribute("checked");
    }
    set checked(v) {
        v ? this.setAttribute("checked", "") : this.removeAttribute("checked");
    }
    
    constructor() {
        super();
    }

    connectedCallback() {
        this.render();
    }

    attributeChangedCallback(name, oldValue, newValue) {
        if (oldValue !== newValue) this.render();
    }


    attachEventListener() {
        this.inputEl.addEventListener("change", (e) => {
            e.preventDefault();
            this.checked = this.inputEl.checked;
            this.dispatchEvent(new Event("change", { bubbles: true }));
        });
    }

    render() {
        this.innerHTML = `
            <div class="input-switch-container" ${this.checked ? 'checked' : ''}>
                <input type="checkbox" class="input-switch-input" ${this.checked ? 'checked' : ''}/>
                <span class="input-switch-indicator"></span>
            </div>
        `;
        this.inputEl = this.querySelector(".input-switch-input");
        this.attachEventListener();
    }
}

customElements.define("input-switch", InputSwitch);
