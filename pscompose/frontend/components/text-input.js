export class TextInput extends HTMLElement {
  static observedAttributes = ["label", "value"];

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
    this.innerHTML = `
      <div class="container">
        <label>
          ${this.getAttribute("label")}
          ${this.getAttribute("description") ?
          `<i data-lucide="info"></i>
          <div class="tool-tip"> ${this.getAttribute("description")} </div>
          ` : ""}
        </label>
        <input type="text" placeholder="Enter ${this.getAttribute("label")}" value="${this.getAttribute("value") || ''}" />
        ${this.getAttribute("required") == 'true' ? `<required>Required<required>` : ""}
      </div>
    `;
    this.querySelector("input").addEventListener("change", ()=>{
      this.dispatchEvent(new Event("change", {bubbles: true}));
    });
  }
}

customElements.define('text-input', TextInput);
