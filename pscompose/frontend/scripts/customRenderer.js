import componentNames from "/components/index.js";

/* CREATE TESTER AND RENDERERS */

function createCustomTester(componentName) {
    return function (uischema, schema, context) {
        if (!uischema.scope) return -1;
        if (uischema.customComponent === componentName) return 6;
        return -1;
    };
}

function createCustomRenderer(componentName) {
    return function (data, handleChange, schema_path, schema) {
        const s = schema?.schema ?? {};
        const required =
            schema?.required ||
            schema?.rootSchema.allOf?.some((obj) => obj?.then?.required?.includes(schema_path)) ||
            false;
        const value = data ?? s.default ?? undefined;

        const props = {
            id: schema?.uischema.scope ?? false,
            path: schema_path,
            label:
                s.title ??
                (schema_path
                    ? schema_path.replace(/-/g, " ").replace(/\b\w/g, (c) => c.toUpperCase())
                    : false),
            required,
            error:
                schema?.errors && s["x-invalid-message"]
                    ? s["x-invalid-message"].replace("%s", value ?? "")
                    : schema?.errors ?? false,
            description: s.description ?? undefined,
            value,
            onChange: (event) => {
                if (event.target.tagName !== schema?.uischema.customComponent?.toUpperCase())
                    return;
                handleChange(schema_path, event.target.value);
            },
        };

        // numeric constraints
        if (s.minimum != null) props.min = s.minimum;
        else if (s.exclusiveMinimum != null) props.min = s.exclusiveMinimum;

        if (s.maximum != null) props.max = s.maximum;
        else if (s.exclusiveMaximum != null) props.max = s.exclusiveMaximum;

        if (s.multipleOf != null) props.step = s.multipleOf;
        else if (props.min != null && props.max != null && props.max > props.min) {
            const range = props.max - props.min;
            props.step = Math.pow(10, Math.floor(Math.log10(range)) - 1);
        }

        // select options
        if (s.oneOf) props.options = JSON.stringify(s.oneOf);
        if (s.enum) props.options = JSON.stringify(s.enum);
        if (s.items?.oneOf) props.options = JSON.stringify(s.items.oneOf);

        return { tag: componentName, props };
    };
}

/* REGISTER RENDERERS */

document.body.addEventListener("json-form:beforeMount", (event) => {
    let elem = event.detail[0].target;
    if (!elem) return;

    componentNames.forEach((component) => {
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
        componentNames.forEach((component) => {
            document
                .querySelector("json-form")
                ?.querySelectorAll(component)
                .forEach((comp) => {
                    comp.disabled = true;
                });
        });
    }
});

document.body.addEventListener("json-form:updated", (event) => {
    componentNames.forEach((component) => {
        document
            .querySelector("json-form")
            ?.querySelectorAll(component)
            .forEach((comp) => {
                if (event.detail[0].target.readonly == "true") {
                    comp.disabled = true;
                } else {
                    comp.disabled = false;
                    document
                        .querySelectorAll(".array-list-add, .array-list-item-delete")
                        .forEach((btn) => {
                            btn.disabled = false;
                            btn.removeAttribute("disabled");
                        });
                }
            });
    });
});

/* Mark Dirty */

document.addEventListener("markAllDirty", () => {
    document.querySelectorAll(componentNames).forEach((control) => {
        if (typeof control.markDirty === "function") {
            control.markDirty();
            control.connectedCallback();
        }
    });

    newMessageBanner("Form fields not all valid", "Error", true);
});
