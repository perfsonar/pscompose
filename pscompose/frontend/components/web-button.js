export class WebButton extends HTMLElement {
    static observedAttributes = ["link", "label", "theme", "backgroundcolor", "bordercolor", "textcolor", "lefticon", "righticon"];
    
    
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
            padding: 8px 16px;
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
        <a href="${this.link || '#'}" style="text-decoration: none;">
          <button style="background-color: ${backgroundColor}; color: ${textColor}; border: 2px solid ${borderColor};" >
            ${this.lefticon ? `<i style="color: ${textColor}; width: 24px;  height: 24px; " data-lucide="${this.lefticon}"></i>` : ''}
            ${this.label || ""}
            ${this.righticon ? `<i style="color: ${textColor}; width: 24px;  height: 24px;" data-lucide="${this.righticon}"></i>` : ''}
          </button>
        </a>
      `;
    }
  }
  
  customElements.define('web-button', WebButton);
  