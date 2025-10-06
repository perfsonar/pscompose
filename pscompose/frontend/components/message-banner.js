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

        if (confirmTheme == "Success") {
            container.innerHTML = `<i data-lucide="check-circle-2"></i> 
                                    <h6>${confirmMsg}</h6>`;
            container.style.backgroundColor = `rgba(var(--success-color-rgb), 0.5)`;
        } else if (confirmTheme == "Warning") {
            container.innerHTML = `<i data-lucide="alert-triangle"></i> 
                                    <h6>${confirmMsg}</h6>`;
            container.style.backgroundColor = `rgba(var(--warning-color-rgb), 0.5)`;
        } else if (confirmTheme == "Error") {
            container.innerHTML = `<i data-lucide="circle-x"></i> 
                                    <h6>${confirmMsg}</h6>`;
            container.style.backgroundColor = `rgba(var(--error-color-rgb), 0.5)`;
        }
        container.classList.add("show");
        sessionStorage.removeItem(key);
        setTimeout(() => {
            container.classList.remove("show");
        }, 3000);
    }
    if (confirmMsg) showNext();
}

window.addEventListener("load", () => {
    processLastMessage();
});
