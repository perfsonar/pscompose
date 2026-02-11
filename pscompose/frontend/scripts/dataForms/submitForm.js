async function submit(mode, formData) {
    // 1. Retrieve jsonform data
    const { name, ...rest } = formData; // Need to remove name from the form

    // TODO: Do we need to set "url" to something here? Is url going to always remain the same?
    const data = {
        ref_set: [],
        type: datatype,
        json: rest,
        name: name,
        created_by: "ssbaveja", // TODO: this will not be needed since it'll be parsed from user object
        last_edited_by: "ssbaveja", // TODO: this will not be needed since it'll be parsed from user object
        // url: ""
        last_edited_at: new Date().toISOString(),
    };

    // 1.1 Additional properties added according to datatype
    if (datatype == "group") {
        data.schema = JSON.parse(document.querySelector("json-form").schemaData);
        data.group_type = rest.type;
    }

    // Map "type" back to "archiver" for archives
    if (datatype == "archive") {
        data.json.archiver = rest.type;
        delete data.json.type;
    }

    let api_endpoint = psCompose.activeRoute.list_endpoint;
    let api_method = "POST";
    console.log("mode: ", mode);
    if (mode == "edit") {
        api_endpoint = `${window.API_BASE_URL}/${datatype}/${id}/`;
        api_method = "PUT";
    }

    // 2. Post request to api
    try {
        const response = await fetch(`${api_endpoint}`, {
            method: api_method,
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(data),
        });

        if (!response.ok) throw new Error(`HTTP error ${response.statusText}`);
        const result = await response.json();
        savemsg = psCompose.activeRoute.singular + " saved successfully!";
        newMessageBanner(savemsg, "Success", false);

        // 3. Redirect
        const path = window.location.pathname;
        const marker = "/" + datatype + "/";
        const index = path.indexOf(marker);

        let newPath = path;
        if (index !== -1) {
            newPath = path.substring(0, index + marker.length);
        }

        // 3.1 Saving favorites
        updateFavorite(result.id, document.querySelector("ps-input-checkbox-star").value);

        window.location = newPath + "?id=" + result.id;
    } catch (error) {
        console.error("Error:", error);
        newMessageBanner(error.message, "Error", true);
    }
}

async function formValidation(event) {
    event.preventDefault();
    var mode = "new";
    if (event.target == "#data-edit-form") mode = "edit";

    const elem = document.querySelector("json-form");
    const form_data = JSON.parse(elem.serializeForm());
    const isFormEmpty = Object.keys(form_data).length === 0;
    const isValid = elem.validate();
    const group_with_excludes = Boolean(datatype == "group" && !!form_data["excludes"]);

    document.querySelectorAll("ps-modal").forEach((modal) => {
        modal.setAttribute("confirm-data-name", form_data.name || "");
    });

    if ((!isValid || isFormEmpty) && !group_with_excludes) {
        document.dispatchEvent(new CustomEvent("markAllDirty"));
    } else {
        document.dispatchEvent(new Event("validated"));
        saveModal.addEventListener("confirm-yes-clicked", () => submit(mode, form_data));
    }
}
