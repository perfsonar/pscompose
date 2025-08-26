export class SingleSelectDropdown extends HTMLElement {
  static observedAttributes = ["label", "placeholder", "options", "selected"];

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
          font-weight: 600;
        }
        select {
          border: 1px solid #C3C7D9;
          background-color: var(--surface2-color);
          padding: 8px;
          color: var(--copy-color);
          font-size: 16px;
          flex: 1;
          width: 100%;
          min-height: 40px;
          max-height: 40px;
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
        <label for="myDropdown">${this.getAttribute("label")}</label>
        <select id="myDropdown">
          <option value="">${this.getAttribute("placeholder")}</option>
          ${optionsHTML}
        </select>
      </div>
    `;
  }
}

customElements.define('single-select-dropdown', SingleSelectDropdown);