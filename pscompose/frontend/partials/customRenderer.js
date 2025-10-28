const HIGH_RANK = 6;
const LOW_RANK = -1;

function toAllCaps(str) {
    return str.replace(/.*/g, (match) => match.toUpperCase());
}

const webComponents = [
    "input-text",
    "input-text-area",
    "input-number",
    "input-checkbox",
    "dropdown-single-select",
    "dropdown-multi-select",
    "dropdown-excludes",
];

/* CREATE TESTER AND RENDERERS */

function createCustomTester(componentName) {
    return function (uischema, schema, context) {
        if (!uischema.scope) return LOW_RANK;
        if (uischema.customComponent === componentName) return HIGH_RANK;
        return LOW_RANK;
    };
}

function createCustomRenderer(componentName) {
    return function (data, handleChange, schema_path, schema) {
        const props = {
            id: schema?.uischema?.scope || "",
            path: schema_path,
            label: schema?.schema?.title || "",
            required:
                schema?.required ||
                schema?.rootSchema?.allOf?.some((obj) =>
                    obj?.then?.required.includes(schema_path),
                ) ||
                false,
            errors: schema?.errors || [],
            description: schema.schema?.description || undefined,
            value: JSON.stringify(data) || JSON.stringify(schema.schema.default) || undefined,
        };

        // onChange
        props.onChange = (event) => {
            if (event.target.tagName == toAllCaps(schema.uischema.customComponent)) {
                let value = JSON.parse(event.target.getAttribute("value"));
                let validValue =
                    typeof value === "string" && value.trim() === "" ? undefined : value;
                handleChange(schema_path, validValue);
            }
        };

        // Input Number
        if (schema?.schema?.minimum) props.min = schema.schema.minimum;
        if (schema?.schema?.maximum) props.max = schema.schema.maximum;
        if (schema?.schema?.multipleOf) props.step = schema.schema.multipleOf;

        // Single Select Dropdown
        if (schema?.schema?.oneOf) props.options = JSON.stringify(schema.schema.oneOf);

        // Multi Select Dropdown & Exclude Dropdown
        if (schema?.schema?.items?.oneOf) props.options = JSON.stringify(schema.schema.items.oneOf);
        if (schema.uischema?.output) props.output = schema.uischema.output;

        return { tag: componentName, props };
    };
}

/* REGISTER RENDERERS */

document.body.addEventListener("json-form:beforeMount", (event) => {
    let elem = event.detail[0].target;
    if (!elem) return;

    webComponents.forEach((component) => {
        let renderer = {
            tester: createCustomTester(component),
            renderer: createCustomRenderer(component),
        };
        elem.appendRenderer(renderer);
    });
});

/* READONLY MODE */

document.body.addEventListener("json-form:mounted", (event) => {
    if (event.detail[0].target.readonly == "true") {
        webComponents.forEach((compoenent) => {
            document
                .querySelector("form")
                .querySelectorAll(compoenent)
                .forEach((comp) => {
                    comp.classList.add("disabled");
                });
        });
    }
});

document.body.addEventListener("json-form:updated", (event) => {
    webComponents.forEach((compoenent) => {
        document
            .querySelector("form")
            .querySelectorAll(compoenent)
            .forEach((comp) => {
                if (event.detail[0].target.readonly == "true") {
                    comp.classList.add("disabled");
                } else {
                    comp.classList.remove("disabled");
                }
            });
    });
});
