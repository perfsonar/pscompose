// Download Template Json 
async function exportTemplateJSON(id, name="Template") {
    try {
        const response = await fetch(`${window.API_BASE_URL}/template/${id}/json/`, {
            method: "GET",
            headers: { "Content-Type": "application/json" },
        });

        if (!response.ok) {
            throw new Error(`HTTP error ${response.statusText}`);
        }
        const jsonData = await response.json();

        // Create and trigger the JSON file download
        const blob = new Blob([JSON.stringify(jsonData, null, 2)], {
            type: "application/json",
        });
        const url = URL.createObjectURL(blob);
        const a = document.createElement("a");
        a.href = url;
        a.download = `${name}.json`;
        a.click();
        URL.revokeObjectURL(url);

        newMessageBanner("JSON successfully downloaded", "Success", true)
        return true; 
    } catch (error) {
        console.error("Error exporting template JSON:", error);
        newMessageBanner("Failed to export template", "Error", true)
        return false; 
    }
}

// Copy Template Json
async function copyTemplateJSON(id) {
    try {
        const response = await fetch(`${window.API_BASE_URL}/template/${id}/json/`, {
            method: "GET",
            headers: { "Content-Type": "application/json" },
        });

        if (!response.ok) {
            throw new Error(`HTTP error ${response.statusText}`);
        }

        const jsonData = await response.json();
        const jsonString = JSON.stringify(jsonData, null, 2);

        await navigator.clipboard.writeText(jsonString);
        newMessageBanner("JSON copied to clipboard", "Success", true)

        return true; 
    } catch (error) {
        console.error("Error exporting template JSON:", error);
        newMessageBanner("Failed to export template", "Error", true)

        return false;
    }
}