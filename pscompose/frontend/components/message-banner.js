function processLastMessage(bannerSelector, displayDuration = 3000) {
    let key = "lastMessage";
    let lastMsg = sessionStorage.getItem(key);
    const banner = document.querySelector(bannerSelector);

    function showNext() {
        if (!lastMsg) {
            banner.classList.remove("show");
            return;
        }
        banner.textContent = lastMsg;
        banner.classList.add("show");
        sessionStorage.removeItem(key);
        setTimeout(() => {
            banner.classList.remove("show");
        }, displayDuration);
    }
    if (lastMsg) showNext();
}

window.addEventListener("load", () => {
    processLastMessage(".message-banner", 3000);
});
