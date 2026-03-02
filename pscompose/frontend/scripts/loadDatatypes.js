// const USERNAME = "ssbaveja"; // TODO: REPLACE HARD CODE
// const PASSWORD = "password"; // TODO: REPLACE HARD CODE
// const AUTH_HEADER = `Basic ${btoa(`${USERNAME}:${PASSWORD}`)}`; 

async function loadSection(apiEndpoint, containerSelector) {
    const container = document.querySelector(containerSelector);
    if (!container) return;

    try {
        // TODO: FETCH USER DATA 
        const response = await fetch(apiEndpoint,
            {
                method: 'GET',
                headers: { 'Authorization': `${AUTH_HEADER}` },
            }
        );
        const data = await response.json();
        data.forEach((item) => {
            item.formatted_date = formatDate(item.last_edited_at);
            item.icon = psCompose.metadata[item.type].icon;
            item.link = psCompose.metadata[item.type].page_url + '?id=' + item.id;
        });

        const template = `
                {% if data.length > 0 %}
                    {% for item in data %}
                    <a class="list-box" href="{{ item.link }}" id={{item.id}}>
                        <div class="box-header" id="shortcut-{{ item.id }}">
                            <i
                                data-lucide="{{ item.icon }}"
                                id="shortcut-icon"
                                aria-hidden="true"
                            ></i>
                            <div class="box-info">
                                <span>{{ item.type | capitalize }}</span>
                                <h4 class="box-name">{{ item.name }}</h4>
                            </div>
                        </div>
                        <p class="box-text">
                            <span class="visually-hidden">Last edited </span>
                            {{ item.formatted_date }}
                        </p>
                    </a>
                    {% endfor %}
                {% else %}
                    <p>No items found.</p>
                {% endif %}
            `;
        container.innerHTML = nunjucks.renderString(template, { data, psCompose });
        lucide.createIcons();
    } catch (err) {
        console.error(`Error loading ${apiEndpoint}:`, err);
        container.innerHTML = "<p role='alert'>Failed to load items. Please try again later.</p>";
    }
}
