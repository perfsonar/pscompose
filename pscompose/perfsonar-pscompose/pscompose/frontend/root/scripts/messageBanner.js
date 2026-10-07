function processLastMessage() {
    let key = "confirmMessage";
    let confirmMsg, confirmTheme;
    if (sessionStorage.getItem(key)) {
        let confirm = JSON.parse(sessionStorage.getItem(key));
        confirmMsg = confirm[0];
        confirmTheme = confirm[1];
    }
    const container = document.querySelector("#response-container");

    function showNext() {
        if (!confirmMsg) {
            container.classList.remove("show");
            return;
        }

        window.scrollTo({ top: 0, left: 0, behavior: "smooth" });

        if (confirmTheme == "Success") {
            container.innerHTML = `<i data-lucide="check-circle-2"></i> 
                                    <h6>${confirmMsg}</h6>`;
            container.style.backgroundColor = `rgba(var(--success)/ 0.8)`;
        } else if (confirmTheme == "Warning") {
            container.innerHTML = `<i data-lucide="alert-triangle"></i> 
                                    <h6>${confirmMsg}</h6>`;
            container.style.backgroundColor = `rgba(var(--warning)/ 0.8)`;
        } else if (confirmTheme == "Error") {
            container.innerHTML = `<i data-lucide="circle-x"></i> 
                                    <h6>${confirmMsg}</h6>`;
            container.style.backgroundColor = `rgba(var(--error)/ 0.8)`;
        }

        lucide.createIcons({ root: container });

        container.classList.add("show");
        sessionStorage.removeItem(key);
        setTimeout(() => {
            container.classList.remove("show");
        }, 3000);
    }
    if (confirmMsg) showNext();
}

function newMessageBanner(confirmMsg, confirmTheme, renderNow) {
    sessionStorage.setItem(
        "confirmMessage",
        JSON.stringify([confirmMsg, confirmTheme]),
    );
    if (renderNow) processLastMessage();
}

window.addEventListener("load", () => {
    processLastMessage();
});
