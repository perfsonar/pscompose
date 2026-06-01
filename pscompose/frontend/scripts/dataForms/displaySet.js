async function taskReference() {
    const refField = document.getElementById("#/properties/reference");
    let ref_data = refField.value || undefined;

    if (refField.parentElement.querySelector("ps-button[data-task-ref]")) return;

    // Create ps-button
    const button = document.createElement("ps-button");
    button.label =
        ref_data !== undefined && "display-task-group" in ref_data
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
    modal.setAttribute("icon", "save");
    modal.setAttribute("theme", "Success");

    const setSource =
        ref_data !== undefined && "display-set-source" in ref_data
            ? JSON.stringify(ref_data["display-set-source"])
            : JSON.stringify('{% jq .addresses[0]._meta."display-set" %}');
    const setDest =
        ref_data !== undefined && "display-set-dest" in ref_data
            ? JSON.stringify(ref_data["display-set-dest"])
            : JSON.stringify('{% jq .addresses[1]._meta."display-set" %}');
    const taskName =
        ref_data !== undefined && "display-task-name" in ref_data
            ? JSON.stringify(ref_data["display-task-name"])
            : "";
    const taskGroup =
        ref_data !== undefined && "display-task-group" in ref_data
            ? JSON.stringify(ref_data["display-task-group"])
            : "[]";

    const msg = `
    <div class="confirm-message">
        <form class='task-ref-form'>
            <ps-input-text 
                id="display-set-source" 
                label="display-set-source" 
                value='${setSource}'>
            </ps-input-text>
            <ps-input-text 
                id="display-set-dest" 
                label="display-set-dest" 
                value='${setDest}'>
            </ps-input-text>
            <ps-input-text 
                id="display-task-name" 
                label="display-task-name" 
                value='${taskName}'>
            </ps-input-text>
            <ps-input-text-multi 
                id="display-task-group" 
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
        const form = modal.querySelector(".task-ref-form");

        if (ref_data == undefined || typeof ref_data !== "object") ref_data = {};
        ref_data["display-set-source"] = form.querySelector("#display-set-source").value;
        ref_data["display-set-dest"] = form.querySelector("#display-set-dest").value;
        ref_data["display-task-name"] = form.querySelector("#display-task-name").value;
        ref_data["display-task-group"] = form.querySelector("#display-task-group").value;

        refField.value = ref_data;
        refField.dispatchEvent(new Event("change", { bubbles: true }));
    });
}

async function addressMetaData() {
    const metaField = document.getElementById("#/properties/_meta");
    let data = metaField.value || undefined;

    if (metaField.parentElement.querySelector("ps-button[data-address-meta]")) return;

    // Create ps-button
    const button = document.createElement("ps-button");
    button.label =
        data !== undefined && "display-set" in data ? "Edit Display Set" : "Add Display Set";
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
        data !== undefined && "display-set" in data
            ? JSON.stringify(data["display-set"] || data["display-name"])
            : "";
    modal.id = "address-modal";
    modal.setAttribute("question", button.label);
    modal.setAttribute("confirm-label", "Save");
    modal.setAttribute("icon", "save");
    modal.setAttribute("theme", "Success");

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

        if (data == undefined || typeof data !== "object") data = {};
        data["display-set"] = form.querySelector("ps-input-text").value;
        metaField.value = data;
        metaField.dispatchEvent(new Event("change", { bubbles: true }));
    });
}
