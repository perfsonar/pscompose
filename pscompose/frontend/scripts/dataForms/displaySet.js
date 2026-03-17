async function taskReference() {
    const refField = document.getElementById("#/properties/reference");

    // Create ps-button
    const button = document.createElement("ps-button");
    button.label = "Add Display Set";
    button.setAttribute("theme", "AddBtn");
    button.setAttribute("lefticon", "plus");
    button.setAttribute("type", "button");
    button.setAttribute("confirm-modal", "task-modal");
    button.addEventListener("click", async function (event) {
        document.dispatchEvent(new Event("validated"));
    });

    // Create modal
    const modal = document.createElement("ps-modal");
    modal.id = "task-modal";
    modal.setAttribute("question", "Add Display Set");
    modal.setAttribute("confirm-label", "Save");

    const msg = `
    <div class="confirm-message">
        <form class='task-ref-form'>
            <ps-input-text label="display-task-group"></ps-input-text>
            <ps-input-text label="display-task-name"></ps-input-text>
            <ps-input-text
                label="display-set-source"
                value='"{% jq .addresses[0]._meta.\\"display-set\\" %}"'
                disabled>
            </ps-input-text>
            <ps-input-text
                label="display-set-dest"
                value='"{% jq .addresses[1]._meta.\\"display-set\\" %}"'
                disabled>
            </ps-input-text>
        </form>
    </div>
    `;
    modal.setAttribute("message", msg);

    // Append button and modal
    document.body.appendChild(modal);
    refField.parentElement.appendChild(button);

    modal.addEventListener("confirm-yes-clicked", async function (event) {
        // Query the form inside the modal's message
        const form = modal.querySelector(".task-ref-form");

        // Helper to get ps-input-text value by label
        const getVal = (label) => {
            const el = form.querySelector(`ps-input-text[label="${label}"]`);
            return el ? el.value : null;
        };

        const formData = {
            "display-task-group": [getVal("display-task-group") ?? "REPLACE_ME"],
            "display-set-source":
                getVal("display-set-source") ?? `{% jq .addresses[0]._meta."display-set" %}`,
            "display-set-dest":
                getVal("display-set-dest") ?? `{% jq .addresses[1]._meta."display-set" %}`,
            "display-task-name": [getVal("display-task-name") ?? "REPLACE_ME"],
        };

        refField.value = formData;
    });
}

async function addressMetaData() {
    const metaField = document.getElementById("#/properties/_meta");

    // Create ps-button
    const button = document.createElement("ps-button");
    button.setAttribute("type", "button");
    button.label = "Add Display Set";
    button.setAttribute("theme", "AddBtn");
    button.setAttribute("lefticon", "plus");
    button.setAttribute("confirm-modal", "address-modal");
    button.addEventListener("click", async function (event) {
        document.dispatchEvent(new Event("validated"));
    });

    // Create modal
    const modal = document.createElement("ps-modal");
    modal.id = "address-modal";
    modal.setAttribute("question", "Add Display Set");
    modal.setAttribute("confirm-label", "Save");

    const msg = `
    <div class="confirm-message">
        <form class='address-meta-form'>
            <ps-input-text label="display-name"></ps-input-text>
            <ps-input-text label="display-set"></ps-input-text>
        </form>
    </div>
    `;
    modal.setAttribute("message", msg);

    // Append button and modal
    document.body.appendChild(modal);
    metaField.parentElement.appendChild(button);

    modal.addEventListener("confirm-yes-clicked", async function (event) {
        // Query the form inside the modal's message
        const form = modal.querySelector(".address-meta-form");

        // Helper to get ps-input-text value by label
        const getVal = (label) => {
            const el = form.querySelector(`ps-input-text[label="${label}"]`);
            return el ? el.value : null;
        };

        const formData = {
            "display-name": getVal("display-name") ?? "REPLACE_ME",
            "display-set": getVal("display-set") ?? "REPLACE_ME",
        };

        metaField.value = formData;
    });
}
