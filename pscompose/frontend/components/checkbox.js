class SimpleCheckbox extends HTMLElement {
  static observedAttributes = ['label', 'checked'];

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
    const label = this.getAttribute('label') || '';
    const checked = this.getAttribute('checked');

    const checkboxStyle = `
      <style>
        :host {
          display: flex;
          height: 100%;
          padding-top: 24px;
        }
        .checkbox-container {
          display: flex;
          align-items: center;
          gap: 4px;
          flex: 1;
        }
        span {
          white-space: nowrap;
          display: flex;
          align-items: center;
          font-weight: 600;
        }
        .checkbox {
          width: 24px;
          height: 24px;
          background: var(--surface1-color);
          accent-color: var(--success-color);
          border: 2px solid var(--copyAlt-color);
          border-radius: 8px;
          cursor: pointer;
          -webkit-appearance: none;
          appearance: none;
          position: relative;
          outline: none;
        }
        .checkbox:checked {
          background: var(--success-color);
        }
        .checkbox:checked::after {
          content: '';
          position: absolute;
          left: 5px;
          top: 0px;
          width: 7px;
          height: 12px;
          border: solid white;
          border-width: 0 3px 3px 0;
          transform: rotate(45deg);
          pointer-events: none;
          display: block;
        }
      </style>
    `;

    this.shadow.innerHTML = `
      ${checkboxStyle}
      <div class="checkbox-container">
        <input type="checkbox" class="checkbox" ${checked === 'true' ? 'checked' : ''}>
        <span>${label}</span>
      </div>
    `;
    this.shadow.querySelector("input").addEventListener("change", ()=>{
      this.dispatchEvent(new Event("change", {bubbles: true}));
    });
  }

}

customElements.define('simple-checkbox', SimpleCheckbox);