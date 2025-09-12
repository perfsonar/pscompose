class SimpleCheckbox extends HTMLElement {
    static observedAttributes = ["label", "checked"];

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
        const label = this.getAttribute("label") || "";
        const checked = this.getAttribute("checked");

        const checkboxStyle = `
            <style>
                simple-checkbox {
                    display: flex;
                    height: 100%;
                }
                .checkbox-container {
                    display: flex;
                    align-items: center;
                    gap: 4px;
                    flex: 1 1 auto;
                }
                .checkbox-container-disabled {
                    display: none;
                }
                .checkbox-container label {
                    white-space: nowrap;
                    display: flex;
                    align-items: center;
                    font-weight: 600;
                }
                .checkbox-container .checkbox {
                    width: 24px;
                    height: 24px;
                    background: var(--surface1-color);
                    accent-color: var(--success-color);
                    border: 2px solid var(--copyAlt-color);
                    border-radius: 8px;
                    cursor: pointer;
                    -webkit-appearance: none;
                    appearance: none;
                    position: relative;
                    outline: none;
                }
                .checkbox-container .checkbox:checked {
                    background: var(--success-color);
                }
                .checkbox-container .checkbox:checked::after {
                    content: '';
                    position: absolute;
                    left: 6px;
                    top: 2px;
                    width: 7px;
                    height: 12px;
                    border: solid white;
                    border-width: 0 3px 3px 0;
                    transform: rotate(45deg);
                    pointer-events: none;
                    display: block;
                }
                simple-checkbox:has(input:disabled) {
                    display: flex;
                    height: 100%;
                    padding-top: 0;
                }
                .checkbox-container:has(input:disabled) {
                    display: none;
                }
                simple-checkbox:has(input:disabled) .checkbox-container-disabled {
                    display: flex;
                    flex-direction: column;
                    gap: 8px;
                    flex: 1 1 auto;
                }
                simple-checkbox:has(input:disabled) .checkbox-container-disabled label {
                    white-space: nowrap;
                    font-weight: 600;
                }
                simple-checkbox:has(input:disabled) .checkbox-container-disabled p {
                    font-family: "Source Code Pro";
                    color: var(--copyAlt-color);
                    height: 24px;
                }
            </style>
        `;

        this.innerHTML = `
            ${checkboxStyle}
            <div class="checkbox-container">
                <input type="checkbox" class="checkbox" ${
                    checked === "true" ? "checked" : ""
                }></input>
                <label>${label}</label>
            </div>

            <div class="checkbox-container-disabled">
                <label>${label}</label>        
                <p>${checked}</p>
            </div>
        `;

        this.querySelector("input").addEventListener("change", (event) => {
            this.setAttribute("checked", event.target.checked ? "true" : "false");
            this.dispatchEvent(new Event("change", { bubbles: true }));
        });
    }
}

customElements.define("simple-checkbox", SimpleCheckbox);
