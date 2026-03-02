async function filterTools() {
    const formData = JSON.parse(elem.serializeForm());
    const testId = formData.test;
    if (!testId) return;

    try {
        // Fetch the selected test to get its type
        const testResponse = await fetch(
            `${window.API_BASE_URL}/test/${testId}/`,
            {
                method: "GET",
                headers: { "Content-Type": "application/json" },
            },
        );

        if (testResponse.ok) {
            const testData = await testResponse.json();
            const testType = testData.json?.type;

            if (testType) {
                // Fetch available tools for this test type
                const toolsResponse = await fetch(
                    `${window.API_BASE_URL}/task/tools/${testType}/`,
                    {
                        method: "GET",
                        headers: { "Content-Type": "application/json" },
                    },
                );

                if (toolsResponse.ok) {
                    const toolsData = await toolsResponse.json();
                    const availableTools = toolsData.tools;

                    // Update the schema to populate tools dropdown with only compatible tools
                    const currentSchema = JSON.parse(elem.schemaData);

                    // Build oneOf array from available tools
                    const toolsOneOf = availableTools.map((toolName) => ({
                        const: toolName,
                        title: toolName,
                    }));

                    if (currentSchema.properties.tools?.items) {
                        currentSchema.properties.tools.items.oneOf = toolsOneOf;
                    }

                    elem.setAttribute(
                        "schema-data",
                        JSON.stringify(currentSchema),
                    );
                    console.log(
                        `Populated tools on initial load: ${toolsOneOf.length} compatible tools for test type ${testType}`,
                    );
                }
            }
        }
    } catch (error) {
        console.error("Error populating tools on initial load:", error);
    }
}

async function updateToolsDropdown(testId) {
    if (!testId) return;

    try {
        // Fetch the selected test to get its type
        const testResponse = await fetch(`${window.API_BASE_URL}/test/${testId}/`, {
            method: "GET",
            headers: { "Content-Type": "application/json" },
        });

        if (!testResponse.ok) {
            console.error("Failed to fetch test details");
            return;
        }

        const testData = await testResponse.json();
        const testType = testData.json?.type;

        if (!testType) {
            console.error("Test type not found in test data");
            return;
        }

        // Fetch available tools for this test type
        const toolsResponse = await fetch(
            `${window.API_BASE_URL}/task/tools/${testType}/`,
            {
                method: "GET",
                headers: { "Content-Type": "application/json" },
            },
        );

        if (!toolsResponse.ok) {
            console.error(`No tools found for test type: ${testType}`);
            return;
        }

        const toolsData = await toolsResponse.json();
        const availableTools = toolsData.tools;

        console.log(`Test type: ${testType}, Available tools:`, availableTools);

        // Update the schema to populate tools dropdown with only compatible tools
        const elem = document.querySelector("json-form");
        const currentSchema = JSON.parse(elem.schemaData);

        // Build oneOf array from available tools
        const toolsOneOf = availableTools.map((toolName) => ({
            const: toolName,
            title: toolName,
        }));

        // Update the schema
        if (currentSchema.properties.tools?.items) {
            currentSchema.properties.tools.items.oneOf = toolsOneOf;
        }

        // Clear existing tool selections to avoid render errors
        const currentFormData = JSON.parse(elem.serializeForm());
        currentFormData.tools = [];

        // Apply updated schema
        elem.setAttribute("schema-data", JSON.stringify(currentSchema));
        elem.setAttribute("form-data", JSON.stringify(currentFormData));

        console.log(
            `Updated tools dropdown: ${toolsOneOf.length} compatible tools for test type ${testType}`,
        );
    } catch (error) {
        console.error("Error updating tools dropdown:", error);
    }
}

async function renderTools(event) {
    if (event.target.label === "Test") {
        await updateToolsDropdown(event.target.value);
    }
}