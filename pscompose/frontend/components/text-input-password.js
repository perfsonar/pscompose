export class TextInputPW extends HTMLElement {
  static observedAttributes = ["label", "placeholder", "backgroundcolor", "labelcolor", "textcolor"];

  constructor() {
    super(); // Call the parent constructor
    this.eyeOff = false; // Flag to track eye icon state
  }

  connectedCallback() {
    this.render();
    lucide.createIcons(); 
    this.addEventListeners();
  }

  attributeChangedCallback(name, oldValue, newValue) {
    this[name] = newValue;
    this.render();
    lucide.createIcons(); 
    this.addEventListeners();
  }

  render() {
    const inputStyle = `
      <style>
        .input-container {
          display: flex;
          flex-direction: column;
          gap: 8px;
          flex: 1;
        }

        label {
          color: ${this.labelcolor || 'var(--copy-color)'};

          font-family: 'Source Sans 3';
          font-style: normal;
          font-weight: 400;
          font-size: 16px;
          line-height: 120%;
          display: flex;
          align-items: center;
        }

        .input-field-container {
          position: relative;
        }

        input {
          background-color: ${this.backgroundcolor || '#000000'};
          color: ${this.textcolor || '#FFFFFF'};
          box-sizing: border-box;

          display: flex;
          flex-direction: row;
          align-items: center;
          padding: 8px 80px 8px 8px; /* Adjust padding for icons */
          gap: 16px;
          font-family: 'Source Sans 3';

          width: 100%;
          height: 40px;

          border: 1px solid #C3C7D9;
          border-radius: 0px;
          font-size: 16px;
        }

        ::placeholder {
          font-size: 16px;
        }

        input:focus {
          outline: none;
          border-color: 'var(--success-color)';
        }

        .icon {
          position: absolute;
          top: 50%;
          transform: translateY(-50%);
        }

        .icon-eye {
          right: 50px;
        }

        .icon-x {
          right: 10px;
        }
      </style>
    `;

    this.innerHTML = `
      ${inputStyle}
      <div class="input-container">
        ${this.label ? `<label for="myInput">${this.label}</label>` : ''}
        <div class="input-field-container">
          <input type="${this.eyeOff ? 'password' : 'text'}" id="myInput" placeholder="${this.placeholder || ''}" />
          <i class="icon icon-eye" style="width: 24px;  height: 24px; color: white;" data-lucide="${this.eyeOff ? 'eye-off' : 'eye'}"></i>
          <i class="icon icon-x" style="width: 24px;  height: 24px; color: white;" data-lucide="x"></i>
        </div>
      </div>
    `;
  }

  addEventListeners() {
    const eyeIcon = this.shadowRoot.querySelector('.icon-eye');
    if (eyeIcon) {
      eyeIcon.addEventListener('click', () => {
        this.eyeOff = !this.eyeOff;
        this.render();
      });
    }
  }
}

customElements.define('text-input-pw', TextInputPW);
