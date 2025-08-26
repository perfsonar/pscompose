export class WebButton extends HTMLElement {
  static observedAttributes = ["link", "label", "theme", "backgroundcolor", "bordercolor", "textcolor", "lefticon", "righticon", "id"];
  passthroughAttributes = {};
  passthroughAttributeMatchers = [new RegExp(/hx-.*/), new RegExp(/data-.*/),]

  connectedCallback() {
    Array.from(this.attributes).forEach((attr)=> {
        this.passthroughAttributeMatchers.forEach((re)=>{
            if(re.test(attr.name)){
                this.passthroughAttributes[attr.name] = this.getAttribute(attr.name);
            }
        })
    })

    this.render();
    lucide.createIcons();
  }

  attributeChangedCallback(name, oldValue, newValue) {
    this[name] = newValue;
    this.render();
    lucide.createIcons();
  }

  render() {
    const theme = this.theme || 'primary'; // Default theme
    let backgroundColor, textColor, borderColor;
    switch (theme) {
      case "primary":
          // Green border, Black background, White text
        backgroundColor = 'var(--surface1-color)';
        textColor = 'var(--copy-color)';
        borderColor = 'var(--success-color)';
        break;
      case "secondary":
          // Green border, green background, White text
        backgroundColor = 'var(--success-color)';
        textColor = 'var(--copy-color)';
        borderColor = 'var(--success-color)';
        break;
      case "tertiary":
          // Copyalt border, green background, White text
        backgroundColor = 'var(--success-color)';
        textColor = 'var(--copy-color)';
        borderColor = 'var(--copyAlt-color)';
        break;
      case "shadow":
          // Copyalt border, green background, White text
        backgroundColor = 'var(--shadow-color)';
        textColor = 'var(--copy-color)';
        borderColor = 'var(--shadow-color)';
        break;
      case "error":
          // red border, red background, White text
        backgroundColor = 'var(--error-color)';
        textColor = 'var(--copy-color)';
        borderColor = 'var(--error-color)';
        break;
      case "warning":
          // no border, yellow background, dark text
        backgroundColor = 'var(--warning-color)';
        textColor = 'var(--surface2-color)';
        borderColor = 'var(--warning-color)';
        break;
      case "custom":
        backgroundColor = this.backgroundcolor || 'var(--primary-color)';
        textColor = this.textcolor || 'white';
        borderColor = this.bordercolor || 'var(--primary-color)';
    }
    const buttonStyle = `
      <style>
        button {
          display: flex;
          align-items: center;
          justify-content: center;
          gap: 8px;
          padding: 0.5rem 1rem;
          border-radius: 18px;
          /* packets/button/1/sans */
          font-family: 'Source Sans 3';
          font-style: normal;
          font-weight: 700;
          font-size: 16px;
          text-align: center;
        }
      </style>
    `;

    this.innerHTML = `
      ${buttonStyle}
      ${this.link ? `<a href="${this.link}" style="text-decoration: none;">` : ''}
        <button 
        ${this.id ? `id="${this.id}"` : ''}
        style="background-color: ${backgroundColor}; color: ${textColor}; border: 2px solid ${borderColor};" hx-ignore>
          ${this.lefticon ? `<i style="color: ${textColor}; width: 1.5rem;  height: 1.5rem; " data-lucide="${this.lefticon}"></i>` : ''}
          ${this.label || ""}
          ${this.righticon ? `<i style="color: ${textColor}; width: 1.5rem;  height: 1.5rem;" data-lucide="${this.righticon}"></i>` : ''}
        </button>
      ${this.link ? `</a>` : ''}
    `;

    let btn = this.querySelector("button");
    Object.keys(this.passthroughAttributes).forEach((k)=>{
        btn.setAttribute(k, this.passthroughAttributes[k]);
        this.removeAttribute(k);
    });
  }
}

customElements.define('web-button', WebButton);