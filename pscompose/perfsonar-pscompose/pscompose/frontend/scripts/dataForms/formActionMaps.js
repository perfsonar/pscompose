const editActions = {
    address: () => addressMetaData(),
    task: () => {
        filterTools();
        taskReference();
    },
    test: () => mergeSchema(),
    archive: () => mergeSchema(),
    context: () => mergeSchema(),
};

const readonlyActions = {
    template: () => {
        document.querySelectorAll(".action-icon.template").forEach((icon) => {
            icon.style.display = "block";
        });
        document.getElementById("export-json-btn").addEventListener("click", async () => {
            await exportTemplateJSON(id, elem?.data?.name);
        });
        document.getElementById("copy-json-btn").addEventListener("click", async () => {
            await copyTemplateJSON(id, elem?.data?.name);
        });
        document
            .getElementById("url-json-btn")
            .setAttribute("link", `${window.API_BASE_URL}/${datatype}/${id}/json`);
    },
    address: () => {
        document.querySelector("ps-button[data-address-meta]")?.remove();
        document.getElementById("address-modal")?.remove();
        document.querySelectorAll(".action-icon.address").forEach((icon) => {
            icon.style.display = "block";
        });
        document
            .getElementById("address-template-btn")
            .setAttribute("link", `${window.API_BASE_URL}/template/address/${id}/`);
    },
    // test: () => mergedSchema(),
    // archive: () => mergedSchema(),
    // context: () => mergedSchema(),
    task: () => {
        document.querySelector("ps-button[data-task-ref]")?.remove();
        document.getElementById("task-modal")?.remove();
        filteredTools();
    },
};

function runReadonlyActions(datatype) {
    if (datatype != "template" && psCompose.activeMenuItem !== "wizard") refsetRender();
    readonlyActions[datatype]?.();
}

function runEditActions(datatype, currentName = null) {
    disableDeleteRefset();
    sameNameValidationEventListener(currentName);
    editActions[datatype]?.();
}
