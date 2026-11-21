function initJsonForm(endpoint, onMounted) {
    document.getElementById("content").setAttribute("hx-get", endpoint);
    document.addEventListener("json-form:mounted", onMounted, { once: true });
}

function initFormSubmit(formId) {
    document.getElementById(formId).addEventListener("submit", (e) => formValidation(e));
}

function refsetRender() {
    document.querySelector(".refset").style.display = "";
    loadSection(`${psCompose.activeRoute.list_endpoint}${id}/find/`, ".refset-container");
}

function disableDeleteRefset() {
    const refsetContainer = document.querySelector(".refset-container");
    if (!refsetContainer?.children.length) return;

    const allHaveIds = Array.from(refsetContainer.children).every((child) => child.id);
    if (!allHaveIds) return;

    document.querySelector("#delete-btn").disabled = true;
    const tooltip = document.createElement("ps-tooltip");
    tooltip.setAttribute("desc", "Delete blocked: This will break the parent template");
    document.querySelector(".refset h6").appendChild(tooltip);
}
