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
    return function (data, handleChange, path, schema) {
        console.log("Custom Renderer Invoked for ", componentName);
        console.log("Custom Renderer title ", schema.schema.title, schema);
        let elemToReturn = { tag: componentName, props: {} };
        elemToReturn.props.id = schema.uischema.scope;
        elemToReturn.props.value = data == null ? schema.schema.default : JSON.stringify(data);
        elemToReturn.props.path = path;
        elemToReturn.props.label = schema.schema.title;
        elemToReturn.props.required = schema.required;
        elemToReturn.props.errors = schema.errors;
        elemToReturn.props.onChange = (event) => {
            if (event.target.tagName == toAllCaps(schema.uischema.customComponent)) {
                handleChange(path, JSON.parse(event.target.getAttribute("value")));
            }
        };
        if (schema?.schema?.description) elemToReturn.props.description = schema.schema.description;

        // Input Number
        if (schema?.schema?.minimum) elemToReturn.props.min = schema.schema.minimum;
        if (schema?.schema?.maximum) elemToReturn.props.max = schema.schema.maximum;
        if (schema?.schema?.multipleOf) elemToReturn.props.step = schema.schema.multipleOf;

        // Single Select Dropdown
        if (schema?.schema?.oneOf) elemToReturn.props.options = JSON.stringify(schema.schema.oneOf);

        // Multi Select Dropdown & Exclude Dropdown
        if (schema?.schema?.items?.oneOf)
            elemToReturn.props.options = JSON.stringify(schema.schema.items.oneOf);
        if (schema.uischema?.output) elemToReturn.props.output = schema.uischema.output;

        return elemToReturn;
    };
}

/* REGISTER RENDERERS */

document.body.addEventListener("json-form:beforeMount", (event) => {
    console.log("JSON Form Before Mount Event Fired");
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
    console.log("JSON Form Mounted Event Fired");
    if (event.detail[0].target.readonly == "true") {
        webComponents.forEach((component) => {
            document
                .querySelector("form")
                .querySelectorAll(component)
                .forEach((comp) => {
                    comp.classList.add("disabled");
                });
        });
    }
});

document.body.addEventListener("json-form:updated", (event) => {
    console.log("JSON Form Updated Event Fired");
    webComponents.forEach((component) => {
        document
            .querySelector("form")
            .querySelectorAll(component)
            .forEach((comp) => {
                if (event.detail[0].target.readonly == "true") {
                    comp.classList.add("disabled");
                } else {
                    comp.classList.remove("disabled");
                }
            });
    });
});
