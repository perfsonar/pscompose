// Favorites Set Up
const USERNAME = "ssbaveja"; // TODO: REPLACE HARD CODE
const PASSWORD = "password"; // TODO: REPLACE HARD CODE
const AUTH_HEADER = `Basic ${btoa(`${USERNAME}:${PASSWORD}`)}`; 

async function fetchFavoriteIDs() {
    const response = await fetch(
        `${window.API_BASE_URL}/favorites/ssbaveja/id/`,
        {
            method: "GET",
            headers: { 'Authorization': `${AUTH_HEADER}`},        
        });
    
    if (!response.ok) {
        throw new Error(`Favorites fetch failed: ${response.status}`);
    }
    
    return await response.json();
}

async function setUpFavorites(id) {
    const starEl = document.querySelector("ps-input-checkbox-star");

    try {
        const response = await fetch(`${window.API_BASE_URL}/favorites/${USERNAME}/${id}/`, {
            method: "GET",
            headers: { 'Authorization': `${AUTH_HEADER}`},
        });
        
        if (!response.ok) {
            throw new Error(`HTTP ${response.status}: ${response.statusText}`);
        }
        
        const data = await response.json();
        starEl.value = data;
    } catch (error) {
        console.error('Failed to fetch user favorites:', error);
    }
}

async function updateFavorite(id, isFavorite) {
    const method = isFavorite ? "PUT" : "DELETE";
    
    const response = await fetch(`${window.API_BASE_URL}/favorites/${USERNAME}/${id}/`, {
        method: method,
        headers: { 'Authorization': AUTH_HEADER },
    });
    
    if (!response.ok) throw new Error(`HTTP error ${response.status}: ${response.statusText}`);
    if (document.querySelector(".subnav-container").classList.contains("open")) await updateSubnav();
    
    return response;
}

function attachFavoritesHandler(id) {
    const starEl = document.querySelector("ps-input-checkbox-star");
    
    starEl.addEventListener('change', async () => {
        try {
            await updateFavorite(id, starEl.value);
        } catch (error) {
            console.error('Failed to update favorites:', error);
        }
    });
}

