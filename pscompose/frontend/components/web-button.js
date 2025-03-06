export class WebButton extends HTMLElement {
    static observedAttributes = ["link", "label", "backgroundcolor", "bordercolor", "textcolor", "lefticon", "righticon"];

    constructor() {
        super();
        this.shadow = this.attachShadow({ mode: 'open' });
    }

    connectedCallback() {
        this.render();
        this.initializeIcons(); // Initialize Lucide icons after rendering
    }

    attributeChangedCallback(name, oldValue, newValue) {
        this[name] = newValue;
        this.render();
        this.initializeIcons(); // Re-initialize icons if attributes change
    }

    render() {
        const buttonStyle = `
            <style>
                button {
                    background-color: ${this.backgroundcolor || '#31B63F'};
                    color: ${this.textcolor || 'white'};
                    display: flex;
                    align-items: center;
                    gap: 8px;
                    padding: 8px 16px;
                    border: 2px solid ${this.bordercolor || '#31B63F'};
                    border-radius: 12px;
                    font-family: 'Arial', sans-serif;
                    font-size: 16px;
                }
                i[data-lucide] {
                    width: 24px;
                    height: 24px;
                    color: white;
                }
            </style>
        `;

        this.shadow.innerHTML = `
            ${buttonStyle}
            <a href="${this.link || '#'}" style="text-decoration: none;">
                <button>
                    <i data-lucide="${this.lefticon || ''}"></i> 
                    ${this.label || ""} 
                    <i data-lucide="${this.righticon || ''}"></i>
                </button>
            </a>
        `;
    }

    initializeIcons() {
        if (this.shadowRoot) {
            lucide.createIcons(); // Initialize Lucide icons in shadow DOM
        }
    }
}

customElements.define('web-button', WebButton);
