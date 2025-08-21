export class TextInputArea extends HTMLElement {
    static observedAttributes = ["label", "placeholder","backgroundcolor", "labelcolor", "textcolor", "value"];
  
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
      const inputStyle = `
        <style>
          .input-container {
            display: flex;
            flex-direction: column;
            gap: 8px;
            flex: 1;
          }
          label {
            color: ${this.labelcolor || '#FFFFFF'};
  
            /* packets/label/1/large */
            font-family: 'Source Sans 3';
            font-style: normal;
            font-weight: 400;
            font-size: 16px;
            line-height: 120%;
            display: flex;
            align-items: center;
          }
  
          textarea  {
            background-color: ${this.backgroundcolor || '#000000'};
            color: ${this.textcolor || '#FFFFFF'};
            box-sizing: border-box;
  
            display: flex;
            flex-direction: row;
            align-items: center;
            padding: 8px 64px 8px 8px;
            gap: 16px;
  
            width: 100%;
            max-width: 100%;
            min-height: 15vh;
            max-height: 35vh;
            resize: vertical;
  
            border: 1px solid #C3C7D9;
            border-radius: 0px;
          }
  
          textarea:focus {
            outline: none;
            border-color: #31B63F;
          }
            
        </style>
      `;
  
      this.shadow.innerHTML = `
        ${inputStyle}
        <div class="input-container">
          ${this.label ? `<label for="myInput">${this.label}</label>` : ''}
            <textarea type="text" id="myInput" placeholder="${this.placeholder || ''}">${this.value}</textarea>
        </div>
      `;
      this.shadow.querySelector("textarea").addEventListener("change", ()=>{
        this.dispatchEvent(new Event("change", {bubbles: true}));
      });
    }
  }
  
  customElements.define('text-input-area', TextInputArea);
  