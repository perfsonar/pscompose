async function taskReference() {
    const refField = document.getElementById("#/properties/reference");
    const metaField = document.getElementById("#/properties/_meta");

    if (refField.parentElement.querySelector("ps-button[data-task-ref]")) return;

    const ref_data =
        typeof refField.value === "string" ? JSON.parse(refField.value) : refField.value;
    const meta_data =
        typeof metaField.value === "string" ? JSON.parse(metaField.value) : metaField.value;

    // Create ps-button
    const button = document.createElement("ps-button");
    button.label =
        "display-task-group" in ref_data || "display-name" in meta_data
            ? "Edit Display Set"
            : "Add Display Set";
    button.setAttribute("theme", "AddBtn");
    button.setAttribute("lefticon", "plus");
    button.setAttribute("type", "button");
    button.setAttribute("confirm-modal", "task-modal");
    button.addEventListener("click", async function () {
        document.dispatchEvent(new Event("validated"));
    });

    // Create modal
    const modal = document.createElement("ps-modal");
    modal.id = "task-modal";
    modal.setAttribute("question", button.label);
    modal.setAttribute("confirm-label", "Save");

    const taskGroup =
        "display-task-group" in ref_data ? JSON.stringify(ref_data["display-task-group"]) : "";
    const taskName = "display-name" in meta_data ? JSON.stringify(meta_data["display-name"]) : "";

    const msg = `
    <div class="confirm-message">
        <form class='task-ref-form'>
            <ps-input-text 
                label="display-task-name" 
                value='${taskName}'>
            </ps-input-text>
            <ps-input-text-multi 
                label="display-task-group" 
                value='${taskGroup}'>
            </ps-input-text-multi>
        </form>
    </div>
    `;

    modal.setAttribute("message", msg);

    // Append button and modal
    button.setAttribute("data-task-ref", "true");
    document.body.appendChild(modal);
    refField.parentElement.appendChild(button);

    modal.addEventListener("confirm-yes-clicked", async function (event) {
        // Query the form inside the modal's message
        const form = modal.querySelector(".task-ref-form");

        ref_data["display-set-source"] =
            ref_data["display-set-source"] || '{% jq .addresses[0]._meta."display-set" %}';
        ref_data["display-set-dest"] =
            ref_data["display-set-dest"] || '{% jq .addresses[1]._meta."display-set" %}';
        ref_data["display-task-name"] =
            ref_data["display-task-name"] || '{% jq .task._meta."display-name" %}';
        ref_data["display-task-group"] = form.querySelector("ps-input-text-multi").value;

        meta_data["display-name"] = form.querySelector("ps-input-text").value;
        metaField.value = meta_data;
        metaField.dispatchEvent(new Event("change", { bubbles: true }));

        refField.value = ref_data;
        refField.dispatchEvent(new Event("change", { bubbles: true }));
    });
}

async function addressMetaData() {
    const metaField = document.getElementById("#/properties/_meta");
    const data = metaField.value;

    if (metaField.parentElement.querySelector("ps-button[data-address-meta]")) return;

    // Create ps-button
    const button = document.createElement("ps-button");
    button.label =
        "display-name" in data || "display-set" in data ? "Edit Display Set" : "Add Display Set";
    button.setAttribute("type", "button");
    button.setAttribute("theme", "AddBtn");
    button.setAttribute("lefticon", "plus");
    button.setAttribute("confirm-modal", "address-modal");
    button.addEventListener("click", async function (event) {
        document.dispatchEvent(new Event("validated"));
    });

    // Create modal
    const modal = document.createElement("ps-modal");
    const displaySet =
        "display-name" in data || "display-set" in data
            ? JSON.stringify(data["display-set"] || data["display-name"])
            : "";
    modal.id = "address-modal";
    modal.setAttribute("question", button.label);
    modal.setAttribute("confirm-label", "Save");

    const msg = `
    <div class="confirm-message">
        <form class='address-meta-form'>
            <ps-input-text label="display-set" value='${displaySet}'></ps-input-text>
        </form>
    </div>
    `;
    modal.setAttribute("message", msg);

    // Append button and modal
    button.setAttribute("data-address-meta", "true");
    document.body.appendChild(modal);
    metaField.parentElement.appendChild(button);

    modal.addEventListener("confirm-yes-clicked", async function () {
        const form = modal.querySelector(".address-meta-form");
        data["display-set"] = form.querySelector("ps-input-text").value;
        metaField.value = data;
        metaField.dispatchEvent(new Event("change", { bubbles: true }));
    });
}
