async function fetchToolsForTest(testId) {
    const testResponse = await fetch(`${window.API_BASE_URL}/test/${testId}/`, {
        headers: { "Content-Type": "application/json" },
    });
    if (!testResponse.ok) throw new Error("Failed to fetch test details");

    const testData = await testResponse.json();
    const testType = testData.json?.type;
    if (!testType) throw new Error("Test type not found");

    const toolsResponse = await fetch(`${window.API_BASE_URL}/task/tools/${testType}/`, {
        headers: { "Content-Type": "application/json" },
    });
    if (!toolsResponse.ok) throw new Error(`No tools found for test type: ${testType}`);

    const toolsData = await toolsResponse.json();
    return { testType, tools: toolsData.tools };
}

async function applyToolsToSchema(testId, clearExisting = false) {
    if (!testId) return;

    try {
        const { testType, tools } = await fetchToolsForTest(testId);
        const elem = document.querySelector("json-form");
        const currentSchema = JSON.parse(elem.schemaData);

        const toolsOneOf = tools.map((tool) => ({ const: tool.name, title: tool.label }));

        if (currentSchema.properties.tools?.items) {
            currentSchema.properties.tools.items.oneOf = toolsOneOf;
        }

        elem.setAttribute("schema-data", JSON.stringify(currentSchema));

        if (clearExisting) {
            const currentFormData = JSON.parse(elem.serializeForm());
            currentFormData.tools = [];
            elem.setAttribute("form-data", JSON.stringify(currentFormData));
        }

        console.log(`${tools.length} compatible tools loaded for test type ${testType}`);
    } catch (error) {
        console.error("Error loading tools:", error);
    }
}

async function filterTools() {
    document.getElementById("#/properties/test").addEventListener("change", async function (event) {
        await applyToolsToSchema(event.target.value, true);
    });
}

async function filteredTools() {
    const form = document.querySelector("json-form");
    const form_data = JSON.parse(form.getAttribute("form-data"));
    await applyToolsToSchema(form_data.test, false);
}
