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
      <div class="container">
        <label>
          ${this.getAttribute("label")}
          ${this.getAttribute("description") ?
          `<i data-lucide="info"></i>
          <div class="tool-tip"> ${this.getAttribute("description")} </div>
          ` : ""}
        </label>
        <select>
          <option>Choose ${this.getAttribute("label")}</option>
          ${optionsHTML}
        </select>
        ${this.getAttribute("required") == 'true' ? `<required>Required<required>` : ""}
        <div class="tags">${tagsHTML}</div>
      </div>
    `;
  }
}

customElements.define('multi-select-dropdown', MultiSelectDropdown);
