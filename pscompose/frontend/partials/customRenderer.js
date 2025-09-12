const HIGH_RANK = 6;
const MID_RANK = 3;
const LOWEST_RANK = -1;

/* TEXT INPUT */

function textInputCustomTester(uischema, schema, context) {
    if (!uischema.scope) return LOWEST_RANK;

    if (
        uischema.scope.endsWith("name") ||
        uischema.scope.endsWith("address") ||
        uischema.scope.endsWith("lead-bind-address") ||
        uischema.scope.endsWith("pschedular-address")
    )
        return MID_RANK;
    return LOWEST_RANK;
}

function textInputCustomRenderer(data, handleChange, path, schema) {
    let elemToReturn = { tag: "text-input", props: {} };
    elemToReturn.props.id = schema.uischema.scope;
    elemToReturn.props.value = data == null ? schema.schema.default : data;
    elemToReturn.props.path = path;
    elemToReturn.props.label = schema.schema.title;
    elemToReturn.props.required = schema.required;
    elemToReturn.props.onChange = (event) => {
        if (event.target.tagName != "INPUT") {
            handleChange(path, event.target.querySelector("input").value);
        }
    };
    if (schema?.schema?.description) {
        elemToReturn.props.description = schema.schema.description;
    }

    return elemToReturn;
}

/* TEXT INPUT AREA */

function textInputAreaCustomTester(uischema, schema, context) {
    if (!uischema.scope) return LOWEST_RANK;

    if (uischema.scope.endsWith("_meta")) return MID_RANK;
    return LOWEST_RANK;
}

function textInputAreaCustomRenderer(data, handleChange, path, schema) {
    let elemToReturn = { tag: "text-input-area", props: {} };

    elemToReturn.props.id = schema.uischema.scope;
    elemToReturn.props.value = data == null ? schema.schema.default : data;
    elemToReturn.props.path = path;
    elemToReturn.props.label = schema.schema.title;
    elemToReturn.props.required = schema.required;
    elemToReturn.props.onChange = (event) => {
        if (event.target.tagName != "TEXTAREA") {
            handleChange(path, event.target.querySelector("textarea").value);
        }
    };
    if (schema?.schema?.description) {
        elemToReturn.props.description = schema.schema.description;
    }

    return elemToReturn;
}

/* CHECK BOX */

function checkBoxCustomTester(uischema, schema, context) {
    if (!uischema.scope) return LOWEST_RANK;

    if (
        uischema.scope.endsWith("disabled") ||
        uischema.scope.endsWith("no-agent") ||
        uischema.scope.endsWith("unidirectional") ||
        uischema.scope.endsWith("excludes-self")
    )
        return MID_RANK;
    return LOWEST_RANK;
}

function checkBoxCustomRenderer(data, handleChange, path, schema) {
    let elemToReturn = { tag: "simple-checkbox", props: {} };

    elemToReturn.props.id = schema.uischema.scope;
    elemToReturn.props.checked = data == null ? schema.schema.default : data;
    elemToReturn.props.path = path;
    elemToReturn.props.label = schema.schema.title;
    elemToReturn.props.required = schema.required;
    elemToReturn.props.onChange = (event) => {
        if (event.target.tagName != "INPUT") {
            handleChange(path, event.target.querySelector("input").checked == true);
        }
    };
    return elemToReturn;
}

/* SINGLE SELECT DROPDOWN */

function singleSelectDropdownCustomTester(uischema, schema, context) {
    if (!uischema.scope) return LOWEST_RANK;

    if (uischema.scope.endsWith("type")) return HIGH_RANK;
    return LOWEST_RANK;
}

function singleSelectDropdownCustomRenderer(data, handleChange, path, schema) {
    let elemToReturn = { tag: "single-select-dropdown", props: {} };

    elemToReturn.props.id = schema.uischema.scope;
    elemToReturn.props.selected = data == null ? schema.schema.default : data;
    elemToReturn.props.path = path;
    elemToReturn.props.label = schema.schema.title;
    elemToReturn.props.required = schema.required;
    elemToReturn.props.onChange = (event) => {
        if (event.target.tagName == "SINGLE-SELECT-DROPDOWN") {
            handleChange(path, event.target.selected);
        }
    };
    if (schema?.schema?.description) {
        elemToReturn.props.description = schema.schema.description;
    }

    // Single Select Dropdown Specific
    if (schema?.schema?.oneOf) {
        elemToReturn.props.options = JSON.stringify(schema.schema.oneOf);
    }

    return elemToReturn;
}

/* MULTI SELECT DROPDOWN */

function multiSelectDropdownCustomTester(uischema, schema, context) {
    if (!uischema.scope) return LOWEST_RANK;

    if (
        uischema.scope.endsWith("contexts") ||
        uischema.scope.endsWith("addresses") ||
        uischema.scope.endsWith("a-addresses") ||
        uischema.scope.endsWith("b-addresses")
    )
        return HIGH_RANK;
    return LOWEST_RANK;
}

function multiSelectDropdownCustomRenderer(data, handleChange, path, schema) {
    let elemToReturn = { tag: "multi-select-dropdown", props: {} };

    elemToReturn.props.id = schema.uischema.scope;
    elemToReturn.props.selected = data == null ? schema.schema.default : JSON.stringify(data);
    elemToReturn.props.path = path;
    elemToReturn.props.label = schema.schema.title;
    elemToReturn.props.required = schema.required;
    elemToReturn.props.onChange = (event) => {
        if (event.target.tagName == "MULTI-SELECT-DROPDOWN" && event.target.selected) {
            handleChange(path, JSON.parse(event.target.selected));
        }
    };
    if (schema?.schema?.description) {
        elemToReturn.props.description = schema.schema.description;
    }

    // Multi Select Dropdown Specific
    if (schema?.schema?.items?.oneOf) {
        elemToReturn.props.options = JSON.stringify(schema.schema.items.oneOf);
    }

    return elemToReturn;
}

/* REGISTER RENDERERS */

document.body.addEventListener("json-form:beforeMount", (event) => {
    let elem = event.detail[0].target;

    if (elem) {
        elem.appendRenderer({ tester: textInputCustomTester, renderer: textInputCustomRenderer });
        elem.appendRenderer({ tester: checkBoxCustomTester, renderer: checkBoxCustomRenderer });
        elem.appendRenderer({
            tester: textInputAreaCustomTester,
            renderer: textInputAreaCustomRenderer,
        });
        elem.appendRenderer({
            tester: singleSelectDropdownCustomTester,
            renderer: singleSelectDropdownCustomRenderer,
        });
        elem.appendRenderer({
            tester: multiSelectDropdownCustomTester,
            renderer: multiSelectDropdownCustomRenderer,
        });
    }
});

/* CHECK READONLY */

document.body.addEventListener("json-form:mounted", (event) => {
    let elem = event.detail[0].target;
    if (elem.readonly == "true") {
        const inputs = document.querySelectorAll("input, select, textarea");
        inputs.forEach((el) => {
            el.disabled = true;
            // Save placeholder if not already saved
            if (!el.dataset.originalPlaceholder) {
                el.dataset.originalPlaceholder = el.placeholder;
            }
            el.placeholder = "";
        });
    }
});

document.body.addEventListener("json-form:updated", (event) => {
    let elem = event.detail[0].target;
    if (elem.readonly == "true") {
        const inputs = document.querySelectorAll("input, select, textarea");
        inputs.forEach((el) => {
            el.disabled = true;
            // Save placeholder if not already saved
            if (!el.dataset.originalPlaceholder) {
                el.dataset.originalPlaceholder = el.placeholder;
            }
            el.placeholder = "";
        });
    }
    if (elem.readonly == "false") {
        const inputs = document.querySelectorAll("input, select, textarea");
        inputs.forEach((el) => {
            el.disabled = false;
            // Restore original placeholder if we have it
            if (el.dataset.originalPlaceholder !== undefined) {
                el.placeholder = el.dataset.originalPlaceholder;
            }
        });
    }
});
