class SimpleCheckbox extends HTMLElement {
  static observedAttributes = ['label', 'checked'];

  constructor() {
    super();
    this.attachShadow({ mode: 'open' });
  }

  connectedCallback() {
    this.render();
    this.shadowRoot.querySelector('input').addEventListener('change', (e) => {
      this.dispatchEvent(new CustomEvent('on-check', {
        detail: { checked: e.target.checked }
      }));
    });
  }

  attributeChangedCallback() {
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
        label {
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

    this.shadowRoot.innerHTML = `
      ${checkboxStyle}
      <label class="checkbox-container">
      <input type="checkbox" class="checkbox" ${checked === 'true' ? 'checked' : ''}>
      <span>${label}</span>
      </label>
    `;
  }

}

customElements.define('simple-checkbox', SimpleCheckbox);
