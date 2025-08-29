export class TextInputArea extends HTMLElement {
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
      const textAreaStyle = `
        <style>
          .textArea-container {
            display: flex;
            flex-direction: column;
            gap: 8px;
            flex: 1;
          }
          .textArea-containerlabel {
            font-weight: 600;
          }
          .textArea-container textarea  {
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
          .textArea-container textarea:focus {
            outline: none;
            border-color: #31B63F;
          }   
          .textArea-container textarea:disabled {
            background-color: transparent;
            font-family: "Source Code Pro";
            color: var(--copyAlt-color);
            border: none;
            cursor: not-allowed;
            padding: 0;
            height: 24px;
          }
        </style>
      `;
  
      this.innerHTML = `
        ${textAreaStyle}
        <div class="textArea-container">
          <label>${this.getAttribute("label")}</label>
          <textarea type="text" placeholder="Enter ${this.getAttribute("label")}">${this.getAttribute("value") || ''}</textarea>
        </div>
      `;
      this.querySelector("textarea").addEventListener("change", ()=>{
        this.dispatchEvent(new Event("change", {bubbles: true}));
      });
    }
  }
  
  customElements.define('text-input-area', TextInputArea);
  