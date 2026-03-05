async function sameNameValidationEventListener() {
    var names;

    try {
        const response = await fetch(`${psCompose.activeRoute.list_endpoint}`, {
            method: "GET",
            headers: { "Content-Type": "application/json" },
        });
        const dts = await response.json();
        names = dts.map((dt) => dt.name);
    } catch (error) {
        console.error("Error:", error);
    }
    const nameInput = document.getElementById("#/properties/name");
    nameInput.addEventListener("change", (e) => {
        if (names.includes(e.target.value)) {
            nameInput.error = "Name already exists";
        } else {
            nameInput.error = "";
        }
    });
}

async function validateSameName() {
    const nameInput = document.getElementById("#/properties/name");
    if (nameInput.error) return false;
    return True;
}
