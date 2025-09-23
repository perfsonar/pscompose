function processLastMessage(responseContainer, displayDuration = 3000) {
    let key = "lastMessage";
    let lastMsg = sessionStorage.getItem(key);
    const container = document.querySelector(responseContainer);

    function showNext() {
        if (!lastMsg) {
            container.classList.remove("show");
            return;
        }
        container.textContent = lastMsg;
        container.classList.add("show");
        sessionStorage.removeItem(key);
        setTimeout(() => {
            container.classList.remove("show");
        }, displayDuration);
    }
    if (lastMsg) showNext();
}

window.addEventListener("load", () => {
    processLastMessage("#response-container", 3000);
});
