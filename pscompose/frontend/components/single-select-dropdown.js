export class SingleSelectDropdown extends HTMLElement {
  static observedAttributes = ["label", "options", "selected"];

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
      `<option value="${option.const}">${option.title}</option>`
    ).join('');

    this.innerHTML = `
      ${dropdownStyle}
      <div class="dropdown-container">
        <label>${this.getAttribute("label")}</label>
        <select>
          <option>Choose ${this.getAttribute("label")}</option>
          ${optionsHTML}
        </select>
      </div>
    `;

    if (this.getAttribute("selected") != null) { this.shadow.querySelector("select").value = this.getAttribute("selected") }

    this.querySelector("select").addEventListener("change", (event) => {
      this.selected = event.target.value;
      this.dispatchEvent(new Event("change", {bubbless: true}));
    });
  }
}

customElements.define('single-select-dropdown', SingleSelectDropdown);
