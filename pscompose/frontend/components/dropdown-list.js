export class DropDownList extends HTMLElement {
  static observedAttributes = ["label", "placeholder", "backgroundcolor", "labelcolor", "textcolor", "options"];

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
    const dropdownStyle = `
      <style>
        .dropdown-container {
          display: flex;
          flex-direction: column;
          gap: 8px;
          flex: 1;
        }
        label {
          color: ${this.labelcolor || '#FFFFFF'};
          font-family: 'Source Sans 3';
          font-style: normal;
          font-weight: 400;
          font-size: 16px;
          line-height: 120%;
          display: flex;
          align-items: center;
        }

        select {
          background-color: ${this.backgroundcolor || '#000000'};
          color: ${this.textcolor || '#FFFFFF'};
          box-sizing: border-box;
          display: flex;
          flex-direction: row;
          align-items: center;
          padding: 8px 64px 8px 8px;
          width: 100%;
          height: 40px;
          min-height: 34px;
          border: 1px solid #C3C7D9;
          border-radius: 0px;
          font-family: 'Source Sans 3';
          font-size: 16px;
        }
        select:focus {
          outline: none;
          border-color: #31B63F;
        }

      </style>
    `;

    const options = this.options ? JSON.parse(this.options) : [];
    const optionsHTML = options.map(option => 
      `<option value="${option.value}">${option.label}</option>`
    ).join('');

    this.shadow.innerHTML = `
      ${dropdownStyle}
      <div class="dropdown-container">
        ${this.label ? `<label for="myDropdown">${this.label}</label>` : ''}
        <select id="myDropdown">
          <option value="">${this.placeholder}</option>
          ${optionsHTML}
        </select>
      </div>
    `;
  }
}

customElements.define('dropdown-list', DropDownList);
