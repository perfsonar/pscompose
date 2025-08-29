export class TextInput extends HTMLElement {
  static observedAttributes = ["label", "value"];

  constructor() {
    super();
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
      .input-container label {
        font-weight: 600;
      }
      .input-container input {
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
      .input-container ::placeholder {
        color: var(--copyAlt-color);
      }
      .input-container input:focus {
        outline: none;
        border: 2px solid var(--success-color);
      }
      .input-container input:disabled {
        background-color: transparent;
        font-family: "Source Code Pro";
        color: var(--copyAlt-color);
        border: none;
        cursor: not-allowed;
        padding: 0;
        height: 24px;
      }
      </style>
    `;

    this.innerHTML = `
      ${inputStyle}
      <div class="input-container">
        <label>${this.getAttribute("label")}</label>
        <input type="text" placeholder="Enter ${this.getAttribute("label")}" value="${this.getAttribute("value") || ''}" />
      </div>
    `;
    this.querySelector("input").addEventListener("change", ()=>{
      this.dispatchEvent(new Event("change", {bubbles: true}));
    });
  }
}

customElements.define('text-input', TextInput);
