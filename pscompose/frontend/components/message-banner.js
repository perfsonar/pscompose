function processLastMessage(responseContainer, displayDuration = 3000) {
    let key = "confirmMessage";
    let confirmMsg, confirmCss;
    if (sessionStorage.getItem(key)) {
        let confirm = JSON.parse(sessionStorage.getItem(key));
        confirmMsg = confirm[0];
        confirmCss = confirm[1];
    }
    const container = document.querySelector(responseContainer);

    function showNext() {
        if (!confirmMsg) {
            container.classList.remove("show");
            return;
        }
        container.innerHTML = `<i data-lucide="check-circle-2"></i> 
                                <h6>${confirmMsg}</h6>`;
        container.style.backgroundColor = confirmCss;
        container.classList.add("show");
        sessionStorage.removeItem(key);
        setTimeout(() => {
            container.classList.remove("show");
        }, displayDuration);
    }
    if (confirmMsg) showNext();
}

window.addEventListener("load", () => {
    processLastMessage("#response-container", 3000);
});
