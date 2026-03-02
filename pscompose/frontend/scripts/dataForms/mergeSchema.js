var selectedType = '';
var additionalSchema = null;
var baseSchemaPropertiesEdit = null;

async function getAdditionalSchema(type) {
    try {
        const url = `${psCompose.activeRoute.list_endpoint}new/${type}/form`;
        const res = await fetch(url, {
            method: "GET",
            headers: { "Content-Type": "application/json" },
        });
        if (!res.ok) throw new Error(`Failed to fetch schema: ${res.status}`);
        return await res.json();
    } catch (err) {
        console.error("Error fetching schema:", err);
        return null;
    }
}

function findGroup(layout) {
    return layout.elements.find(
        (el) => el.type === "Group" && el.rule?.condition?.scope === "#/properties/type",
    );
}

function mergeSchema(baseSchema, versionData) {
    if (!baseSchemaPropertiesEdit) {
        baseSchemaPropertiesEdit = new Set(Object.keys(baseSchema.properties));
    }
    const keysToRemove = Object.keys(baseSchema.properties).filter(
        (key) => !baseSchemaPropertiesEdit.has(key),
    );
    keysToRemove.forEach((key) => delete baseSchema.properties[key]);
    Object.assign(baseSchema.properties, versionData.properties);
    const baseRequired = ["name", "type"];
    baseSchema.required = [...new Set([...baseRequired, ...(versionData.required || [])])];
}

function mergeLayout(group, uiVersionData) {
    group.elements = group.elements.slice(0, 1).concat(uiVersionData.elements);
}

function ensureVersionDropdown(group) {
    group.elements = Array.isArray(group.elements) ? group.elements : [];
    if (!group.elements.some((e) => e.scope === "#/properties/version")) {
        group.elements.unshift({
            type: "Control",
            scope: "#/properties/version",
            customComponent: "ps-select",
        });
    }
}

async function handleTypeChange(selectedType, additionalSchema) {
    console.log("Selected type ", selectedType, additionalSchema);
    const versions = (additionalSchema?.spec?.versions || []).filter(v => v !== null);
    if (!versions.length) return;

    const highestVersion = Number(versions.sort((a, b) => Number(b) - Number(a))[0]);
    console.log("Highest version:", highestVersion);

    const elem = document.querySelector("json-form");
    const baseSchema = JSON.parse(elem.schemaData);
    const baseLayout = JSON.parse(elem.layoutData);

    const group = findGroup(baseLayout);
    if (!group) return;

    group.rule.condition.schema.const = selectedType;
    ensureVersionDropdown(group);

    baseSchema.properties.version = {
        type: "string",
        title: "Version",
        oneOf: versions.map((v) => ({ const: v, title: `Version ${v}` })),
        default: highestVersion,
    };

    const versionData = additionalSchema.spec.jsonschema.versions[highestVersion];
    const uiVersionData = additionalSchema.spec.uischema.versions[highestVersion];

    mergeSchema(baseSchema, versionData);
    mergeLayout(group, uiVersionData);

    const currentFormData = JSON.parse(elem.serializeForm());
    Object.keys(versionData.properties).forEach((key) => {
        const property = versionData.properties[key];
        if (property.default !== undefined) {
            currentFormData[key] = property.default;
        } else {
            delete currentFormData[key];
        }
    });

    currentFormData.version = String(highestVersion);
    currentFormData.schema = highestVersion;

    elem.setAttribute("schema-data", JSON.stringify(baseSchema));
    elem.setAttribute("layout-data", JSON.stringify(baseLayout));
    elem.setAttribute("form-data", JSON.stringify(currentFormData));

    console.log("Schema:", baseSchema);
    console.log("UI Schema:", baseLayout);
    console.log("Form Data:", currentFormData);
}

function updateIdleVersion(selectedVersion, additionalSchema) {
    console.log("Updating to version:", selectedVersion, additionalSchema);
    const elem = document.querySelector("json-form");
    const currentSchema = JSON.parse(elem.schemaData);
    const currentLayout = JSON.parse(elem.layoutData);
    const currentFormData = JSON.parse(elem.serializeForm());

    const versionData = additionalSchema.spec.jsonschema.versions[selectedVersion];
    const uiVersionData = additionalSchema.spec.uischema.versions[selectedVersion];

    if (!versionData || !uiVersionData) return;

    mergeSchema(currentSchema, versionData);

    const group = findGroup(currentLayout);
    if (!group) return;

    mergeLayout(group, uiVersionData);

    const newSchemaProperties = new Set(Object.keys(versionData.properties));
    if (baseSchemaPropertiesEdit) {
        baseSchemaPropertiesEdit.forEach((key) => newSchemaProperties.add(key));
    }
    newSchemaProperties.add("version");

    Object.keys(currentFormData).forEach((key) => {
        if (!newSchemaProperties.has(key)) {
            delete currentFormData[key];
        }
    });

    Object.keys(versionData.properties).forEach((key) => {
        const property = versionData.properties[key];
        if (property.default !== undefined) {
            currentFormData[key] = property.default;
        } else {
            delete currentFormData[key];
        }
    });

    currentFormData.version = String(selectedVersion);

    elem.setAttribute("schema-data", JSON.stringify(currentSchema));
    elem.setAttribute("layout-data", JSON.stringify(currentLayout));
    elem.setAttribute("form-data", JSON.stringify(currentFormData));

    console.log("New Schema:", currentSchema);
    console.log("New UI Schema:", currentLayout);
    console.log("New Form Data:", currentFormData);
}

async function mergeSchema(event) {
    if (event.target?.label === "Type") {
        selectedType = event.target.value;
        additionalSchema = await getAdditionalSchema(selectedType);
        if (additionalSchema) {
            handleTypeChange(selectedType, additionalSchema);
        }
    }

    if (event.target?.label === "Version") {
        const newVersion = JSON.parse(event.target.value);
        if (additionalSchema) {
            updateIdleVersion(newVersion, additionalSchema);
        }
    }
}
