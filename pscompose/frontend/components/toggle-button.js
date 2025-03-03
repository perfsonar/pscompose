export class ToggleButton extends HTMLElement {
  static observedAttributes = ["checked", "label", "backgroundcolor", "bordercolor", "textcolor"];

  constructor() {
    super();
    this.shadow = this.attachShadow({ mode: 'open' });
    this.checked = false; 
  }

  connectedCallback() {
    this.render();
  }

  attributeChangedCallback(name, oldValue, newValue) {
    if (name === 'checked') {
      this.checked = newValue === 'true';
    }
    this.render();
  }

  toggle = () => {
    this.checked = !this.checked; 
    this.setAttribute('checked', this.checked);
    this.dispatchEvent(new CustomEvent('change', {
      detail: { checked: this.checked }
    }));
    this.render(); 
  }

  render() {
    const backgroundColor = this.getAttribute('backgroundcolor') || '#31B63F';
    const borderColor = this.getAttribute('bordercolor') || '#31B63F';
    const textColor = this.getAttribute('textcolor') || 'white';
    const label = this.getAttribute('label') || '';

    const style = `
      <style>
        .toggle {
        display: flex;
        flex-direction: column;
        aligned-items: center;
        justify-content: center;
        flex: 1;
        }

        .switch {
          position: relative;
          display: inline-block;
          width: 60px;
          height: 34px;
        }
        
        .switch input {
          opacity: 0;
          width: 0;
          height: 0;
        }
        
        .slider {
          position: absolute;
          cursor: pointer;
          top: 0;
          left: 0;
          right: 0;
          bottom: 0;
          background-color: #ccc;
          transition: .4s;
          border-radius: 34px;
        }
        
        .slider:before {
          position: absolute;
          content: "";
          height: 34px;
          width: 34px;
          background-color: white;
          transition: .4s;
          border-radius: 50%;
        }
        
        input:checked + .slider {
          background-color: ${backgroundColor};
        }
        
        input:checked + .slider:before {
          transform: translateX(26px);
        }
        
        .label {
          font-family: 'Source Sans 3', sans-serif;
          font-style: normal;
          font-weight: 400;
          font-size: 16px;
          color: ${textColor};
        }
      </style>
    `;

    this.shadow.innerHTML = `
      ${style}
      <div class="toggle">
        <span class="label">${label}</span>
        <label class="switch">
          <input type="checkbox" ${this.checked ? 'checked' : ''}>
          <span class="slider"></span>
        </label>
      </div>
    `;
    
    this.shadow.querySelector('input').addEventListener('click', this.toggle);
  }
}

customElements.define('toggle-button', ToggleButton);
