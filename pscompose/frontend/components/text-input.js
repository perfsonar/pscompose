export class TextInput extends HTMLElement {
  static observedAttributes = ["label", "placeholder", "value"];

  constructor() {
    super();
    this.shadow = this.attachShadow({ mode: 'open' });
  }

  connectedCallback() {
    this.render();
  }

  attributeChangedCallback(name, oldValue, newValue) {
    this[name] = newValue;
    this.render();
  }

  render() {
    const inputStyle = `
      <style>
      .input-container {
        display: flex;
        flex-direction: column;
        gap: 8px;
        flex: 1 1 auto;
      }
      label {
        font-weight: 600;
      }
      input {
        background-color: var(--surface2-color);
        color: var(--copy-color);
        box-sizing: border-box;

        display: flex;
        flex-direction: row;
        padding: 8px;

        width: 100%;
        height: 40px;

        border: 1px solid #C3C7D9;
        font-size: 16px;
      }
      ::placeholder {
        color: var(--copyAlt-color);
      }
      input:focus {
        outline: none;
        border: 2px solid var(--success-color);
      }
      </style>
    `;

    this.shadow.innerHTML = `
      ${inputStyle}
      <div class="input-container">
        ${this.getAttribute("label") ? `<label> ${this.getAttribute("label")} </label>` : ''}
        <input type="text" placeholder="${this.getAttribute("placeholder") || ''}" value="${this.getAttribute("value") || ''}" />
      </div>
    `;
    this.shadow.querySelector("textarea").addEventListener("change", ()=>{
      this.dispatchEvent(new Event("change", {bubbles: true}));
    });
  }
}

customElements.define('text-input', TextInput);
