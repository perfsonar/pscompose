export class TextInputArea extends HTMLElement {
    static observedAttributes = ["label", "value"];
  
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
            font-weight: 600;
          }
          textarea  {
            background-color: var(--surface2-color);
            color: var(--copy-color);
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
          <label>${this.getAttribute("label")}</label>
          <textarea type="text" placeholder="Enter ${this.getAttribute("label")}">${this.getAttribute("value") || ''}</textarea>
        </div>
      `;
      this.shadow.querySelector("textarea").addEventListener("change", ()=>{
        this.dispatchEvent(new Event("change", {bubbles: true}));
      });
    }
  }
  
  customElements.define('text-input-area', TextInputArea);
  