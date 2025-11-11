// Set list of existing data to select dropdown
try {
    fetch(psCompose.activeRoute.list_endpoint)
        .then((response) => {
            if (!response.ok) {
                let errorMsg = "Something went wrong.";
                alert(errorMsg);
                console.error("Error:", errorMsg);
            }
            return response.json();
        })
        .then((data) => {
            const dataList = data.map((item) => ({
                const: item.id,
                title: item.name,
            }));
            document
                .querySelector("dropdown-single-select")
                .setAttribute("options", JSON.stringify(dataList));
        });
} catch (error) {
    console.error("Error:", error);
}

/* RENDER JSON FORM */
// 1. set param and redirect
document.querySelector("dropdown-single-select").addEventListener("change", (evt) => {
    let newUrlParam = new URLSearchParams();
    newUrlParam.set("id", evt.target.value);
    window.location = window.location.pathname + "?" + newUrlParam;
});

document.querySelector("#new-btn").addEventListener("click", () => {
    let newUrlParam = new URLSearchParams();
    newUrlParam.set("new", true);
    window.location = window.location.pathname + "?" + newUrlParam;
});

// 2 take param and render existing/new data json form
let urlParam = new URLSearchParams(window.location.search);
let container = document.querySelector(".step-box-right");

if (urlParam.size > 0) {
    if (!!urlParam.get("id")) {
        document
            .querySelector("dropdown-single-select")
            .setAttribute("value", JSON.stringify(urlParam.get("id")));

        container.innerHTML = `<div class="w-full" 
                                    hx-get="/partials/edit_form.html" 
                                    hx-trigger="load"></div>`;
    }
    if (!!urlParam.get("new")) {
        container.innerHTML = `<div class="w-full" 
                        hx-get="/partials/new_form.html" 
                        hx-trigger="load"></div>`;
    }
    htmx.process(container);
}
