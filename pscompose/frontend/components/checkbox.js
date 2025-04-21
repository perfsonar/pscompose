export class CheckboxComponent extends HTMLElement {
    static observedAttributes = ["label", "checked", "color", "size", "labelcolor"];
  
    constructor() {
      super();
      this.shadow = this.attachShadow({ mode: 'open' });
      this._checked = false;
    }
  
    connectedCallback() {
      this.render();
      this.shadow.querySelector('input').addEventListener('change', (e) => {
        this._checked = e.target.checked;
        this.dispatchEvent(new CustomEvent('on-check', {
          detail: { checked: this._checked }
        }));
      });
    }
  
    attributeChangedCallback(name, oldValue, newValue) {
      if (name === 'checked') {
        this._checked = newValue !== null;
      }
      this[name] = newValue;
      this.render();
    }
  
    get checked() {
      return this._checked;
    }
  
    set checked(value) {
      this._checked = Boolean(value);
      this.render();
    }
  
    render() {
      const checkboxSize = this.size || '20px';
      const checkmarkColor = this.color || '#000000';
      const labelColor = this.labelcolor || 'var(--copy-color)';
  
      const style = `
        <style>
          .checkbox-container {
            display: flex;
            align-items: center;
            gap: 12px;
            position: relative;
          }
  
          .custom-checkbox {
            width: ${checkboxSize};
            height: ${checkboxSize};
            border: 2px solid ${checkmarkColor};
            position: relative;
            cursor: pointer;
            appearance: none;
            -webkit-appearance: none;
          }
  
          .custom-checkbox:checked {
            background: ${checkmarkColor}20;
          }
  
          .custom-checkbox:checked::before {
            content: "✓";
            position: absolute;
            left: 50%;
            top: 50%;
            transform: translate(-50%, -50%);
            color: ${checkmarkColor};
            font-size: calc(${checkboxSize} * 0.8);
          }
  
          label {
            color: ${labelColor};
            font-family: 'Source Sans 3';
            font-size: 16px;
            cursor: pointer;
            user-select: none;
          }
        </style>
      `;
  
      this.shadow.innerHTML = `
        ${style}
        <label class="checkbox-container">
          <input 
            type="checkbox" 
            class="custom-checkbox"
            ${this._checked ? 'checked' : ''}
          />
          ${this.label ? `<span>${this.label}</span>` : ''}
        </label>
      `;
    }
  }
  
  customElements.define('custom-checkbox', CheckboxComponent);
  