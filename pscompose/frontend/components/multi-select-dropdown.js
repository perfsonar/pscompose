export class MultiSelectDropdown extends HTMLElement {
  static observedAttributes = ["label", "options", "selected"];

  constructor() {
    super();
    this.selectedValues = [];
  }

  connectedCallback() {
    this.selectedSetUp();
    this.render();
    this.attachListeners();
    lucide.createIcons();
  }

  attributeChangedCallback(name, oldValue, newValue) {
    this[name] = newValue;
    this.render();
    this.attachListeners();
    lucide.createIcons();
  }

  selectedSetUp() {
    const selected = this.getAttribute("selected") ? JSON.parse(this.getAttribute("selected")) : [];
    this.selectedValues = selected.map(item => (typeof item === 'object' ? item.const : item));
  }

  attachListeners() {
    const select = this.querySelector('select');

    if (select) {
      select.addEventListener('change', () => {
        const value = select.value.trim();
        if (value && !this.selectedValues.includes(value)) {
          this.selectedValues.unshift(value);
          this.setAttribute("selected", JSON.stringify(this.selectedValues));
          this.render();
          this.attachListeners();
          lucide.createIcons();
        }
        select.value = '';
      });
    }

    this.querySelectorAll('.tag .remove-tag').forEach(btn => {
      btn.addEventListener('click', () => {
        const value = btn.getAttribute('data-value');
        this.selectedValues = this.selectedValues.filter(v => v !== value);
        this.setAttribute("selected", JSON.stringify(this.selectedValues));
        this.render();
        this.attachListeners();
        lucide.createIcons();
      });
    });
    this.dispatchEvent(new Event("change", {bubbles: true}));
  }

  render() {
    const dropdownStyle = `
      <style>
      .dropdown-container {
        display: flex;
        flex-direction: column;
        gap: 8px;
        flex: 1 1 auto;
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
        border-color: var(--success-color);
      }
      .tags {
        display: flex;
        flex-wrap: wrap;
        gap: 6px;
      }
      .tag {
        display: flex;
        align-items: center;
        gap: 8px;
        border-radius: 16px;
        padding: 4px 8px 4px 12px;
        border: 1px solid #454547;
        background: var(--success-color);
        color: var(--copy-color);
        font-size: 14px;
        font-weight: 600;
      }
      .remove-tag {
        display: flex;
        cursor: pointer;
        background: transparent;
        border: none;
        padding: 0;
      }
      select:disabled {
        display: none;
      }
      .dropdown-container:has(select:disabled) .tag {
        padding: 4px 12px 4px 12px;
      }
      .dropdown-container:has(select:disabled) .remove-tag {
        display: none;
      }
      </style>
    `;

    const options = this.getAttribute("options") ? JSON.parse(this.getAttribute("options")) : [];
    const availableOptions = options.filter(opt => !this.selectedValues.includes(opt.const));

    const optionsHTML = availableOptions.map(option =>
      `<option value="${option.const}">${option.title}</option>`
    ).join('');

    const tagsHTML = this.selectedValues.map(val => {
      const label = options.find(opt => opt.const === val)?.title || val;
      return `<span class="tag">
                ${label}
                <button class="remove-tag" data-value="${val}">
                  <i style="width: 16px; height: 16px; color: white;" data-lucide="x"></i>
                </button>
              </span>`;
    }).join('');

    this.innerHTML = `
      ${dropdownStyle}
      <div class="dropdown-container">
        <label>${this.getAttribute("label")}</label>
          <select>
            <option>Choose ${this.getAttribute("label")}</option>
            ${optionsHTML}
          </select>
        <div class="tags">${tagsHTML}</div>
      </div>
    `;
  }
}

customElements.define('multi-select-dropdown', MultiSelectDropdown);
