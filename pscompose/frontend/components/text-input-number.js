export class TextInputNum extends HTMLElement {
  static observedAttributes = ["label", "placeholder", "backgroundcolor", "labelcolor", "textcolor"];


  connectedCallback() {
    this.render();
    lucide.createIcons(); 
  }

  attributeChangedCallback(name, oldValue, newValue) {
    this[name] = newValue;
    this.render();
    lucide.createIcons(); 
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

        input {
          background-color: ${this.backgroundcolor || '#000000'};
          color: ${this.textcolor || '#FFFFFF'};
          box-sizing: border-box;

          display: flex;
          flex-direction: row;
          align-items: center;
          padding: 8px 64px 8px 8px;
          gap: 16px;

          width: 100%;
          height: 40px;

          border: 1px solid #C3C7D9;
          border-radius: 0px;
          font-size: 16px;
        }

        ::placeholder {
          font-size: 16px;
          padding: 8px 64px 8px 8px;
        }

        input:focus {
          outline: none;
          border-color: 'var(--success-color)';
        }

        .icon {
          position: absolute;
          right: 16px;
          top: 50%;
          transform: translateY(-50%);
        }
      </style>
    `;

    this.innerHTML = `
      ${inputStyle}
      <div class="input-container">
        ${this.label ? `<label for="myInput">${this.label}</label>` : ''}
        <input type="text" id="myInput" placeholder="${this.placeholder || ''}" />
        <i style="width: 24px;  height: 24px;" data-lucide="plus"></i>
        <i style="width: 24px;  height: 24px;" data-lucide="minus"></i>
      </div>
    `;
  }
}

customElements.define('text-input-num', TextInputNum);
