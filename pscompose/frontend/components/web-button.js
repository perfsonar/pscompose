export class WebButton extends HTMLElement {
    static observedAttributes = ["link", "label", "backgroundcolor", "bordercolor", "textcolor", "lefticon", "righticon"];
  
    constructor() {
      super();
      this.shadow = this.attachShadow({ mode: 'open' }); // Attach a shadow DOM
    }
  
    connectedCallback() {
      this.render();
    }
  
    disconnectedCallback() {}
  
    adoptedCallback() {}
  
    someCallback() {
      return () => {
        console.log(`someCallback called for button with label '${this.label}'`);
      };
    }
  
    attributeChangedCallback(name, oldValue, newValue) {
      console.log(`Attribute ${name} changed from ${oldValue} to ${newValue}`);
      this[name] = newValue;
      this.render();
    }
  
    render() {
      const buttonStyle = `
        <style>

          button {
            background-color: '#31B63F';
            color: 'white';

            display: flex;
            flex-direction: row;
            justify-content: center;
            align-items: center;
            padding: 8px 20px;
            gap: 16px;

            border: 2px solid #31B63F;
            border-radius: 18px;

            /* Label */
            font-family: 'Source Sans 3';
            font-style: normal;
            font-weight: 700;
            font-size: 16px;
            text-align: center;
          }
  
          button:hover {
            opacity: 0.8;
          }
          
            
        </style>
      `;
  
      this.shadow.innerHTML = `
        ${buttonStyle}
        <a href="${this.link}" style="text-decoration: none;">
        
        <button id="myid" style="color: ${this.textcolor}; background-color: ${this.backgroundcolor}; border-color: ${this.bordercolor}" >
        ${this.lefticon || ''} 
        ${this.label || 'Click Me'} 
        ${this.righticon || ''} 
        </button> 
        </a>
      `;
      this.shadow.querySelector("#myid").onclick = this.someCallback();
    }
  }
  
  customElements.define('web-button', WebButton);
  