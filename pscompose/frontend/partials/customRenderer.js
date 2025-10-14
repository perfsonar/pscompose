const HIGH_RANK = 6;
const MID_RANK = 3;
const LOWEST_RANK = -1;

/* TEXT INPUT */

function textInputCustomTester(uischema, schema, context) {
    if (!uischema.scope) return LOWEST_RANK;
    if (uischema.customComponent == "input-text") return MID_RANK;
    return LOWEST_RANK;
}

function textInputCustomRenderer(data, handleChange, path, schema) {
    let elemToReturn = { tag: "input-text", props: {} };
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

/* TEXT INPUT NUMBER */

function textInputNumberCustomTester(uischema, schema, context) {
    if (!uischema.scope) return LOWEST_RANK;
    if (uischema.customComponent == "input-number") return HIGH_RANK;

    return LOWEST_RANK;
}

function textInputNumberCustomRenderer(data, handleChange, path, schema) {
    let elemToReturn = { tag: "input-number", props: {} };
    elemToReturn.props.id = schema.uischema.scope;
    elemToReturn.props.value = data == null ? schema.schema.default : data; // Might not have default?
    elemToReturn.props.path = path;
    elemToReturn.props.label = schema.schema.title;
    elemToReturn.props.required = schema.required;
    elemToReturn.props.onChange = (event) => {
        if (event.target.tagName == "INPUT") {
            handleChange(path, event.target.value);
        }
    };
    if (schema?.schema?.description) {
        elemToReturn.props.description = schema.schema.description;
    }
    if (schema?.schema?.minimum) {
        elemToReturn.props.min = schema.schema.minimum;
    }
    if (schema?.schema?.maximum) {
        elemToReturn.props.max = schema.schema.maximum;
    }
    if (schema?.schema?.maximum) {
        elemToReturn.props.step = schema.schema.multipleOf;
    }
    return elemToReturn;
}

/* INPUT TEXT AREA */

function textInputAreaCustomTester(uischema, schema, context) {
    if (!uischema.scope) return LOWEST_RANK;
    if (uischema.customComponent == "input-text-area") return MID_RANK;
    return LOWEST_RANK;
}

function textInputAreaCustomRenderer(data, handleChange, path, schema) {
    let elemToReturn = { tag: "input-text-area", props: {} };
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

/* TEXT INPUT CHECK BOX */

function checkBoxCustomTester(uischema, schema, context) {
    if (!uischema.scope) return LOWEST_RANK;
    if (uischema.customComponent == "input-checkbox") return MID_RANK;

    return LOWEST_RANK;
}

function checkBoxCustomRenderer(data, handleChange, path, schema) {
    let elemToReturn = { tag: "input-checkbox", props: {} };
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
    if (schema?.schema?.description) {
        elemToReturn.props.description = schema.schema.description;
    }
    return elemToReturn;
}

/* SINGLE SELECT DROPDOWN */

function singleSelectDropdownCustomTester(uischema, schema, context) {
    if (!uischema.scope) return LOWEST_RANK;
    if (uischema.customComponent == "dropdown-single-select") return HIGH_RANK;
    return LOWEST_RANK;
}

function singleSelectDropdownCustomRenderer(data, handleChange, path, schema) {
    let elemToReturn = { tag: "dropdown-single-select", props: {} };
    elemToReturn.props.id = schema.uischema.scope;
    elemToReturn.props.selected = data == null ? schema.schema.default : data;
    elemToReturn.props.path = path;
    elemToReturn.props.label = schema.schema.title;
    elemToReturn.props.required = schema.required;
    elemToReturn.props.onSelect = (event) => {
        if (event.target.tagName == "DROPDOWN-SINGLE-SELECT") {
            handleChange(path, event.target.selected);
        }
    };
    if (schema?.schema?.description) {
        elemToReturn.props.description = schema.schema.description;
    }
    if (schema?.schema?.oneOf) {
        elemToReturn.props.options = JSON.stringify(schema.schema.oneOf);
    }
    return elemToReturn;
}

/* MULTI SELECT DROPDOWN - OBJECT */

function multiSelectDropdownObjectCustomTester(uischema, schema, context) {
    if (!uischema.scope) return LOWEST_RANK;
    if (uischema.customComponent == "dropdown-multi-select-object") return HIGH_RANK;
    return LOWEST_RANK;
}

function multiSelectDropdownObjectCustomRenderer(data, handleChange, path, schema) {
    let elemToReturn = { tag: "dropdown-multi-select", props: {} };
    elemToReturn.props.id = schema.uischema.scope;
    elemToReturn.props.selected = data == null ? schema.schema.default : JSON.stringify(data);
    elemToReturn.props.path = path;
    elemToReturn.props.label = schema.schema.title;
    elemToReturn.props.required = schema.required;
    elemToReturn.props.output = "object";
    elemToReturn.props.onSelect = (event) => {
        if (event.target.tagName == "DROPDOWN-MULTI-SELECT" && event.target.selected) {
            handleChange(path, JSON.parse(event.target.selected));
        }
    };
    if (schema?.schema?.description) {
        elemToReturn.props.description = schema.schema.description;
    }
    if (schema?.schema?.items?.oneOf) {
        elemToReturn.props.options = JSON.stringify(schema.schema.items.oneOf);
    }
    return elemToReturn;
}

/* MULTI SELECT DROPDOWN - LIST*/

function multiSelectDropdownListCustomTester(uischema, schema, context) {
    if (!uischema.scope) return LOWEST_RANK;
    if (uischema.customComponent == "dropdown-multi-select-list") return HIGH_RANK;
    return LOWEST_RANK;
}

function multiSelectDropdownListCustomRenderer(data, handleChange, path, schema) {
    let elemToReturn = { tag: "dropdown-multi-select", props: {} };
    elemToReturn.props.id = schema.uischema.scope;
    elemToReturn.props.selected = data == null ? schema.schema.default : JSON.stringify(data);
    elemToReturn.props.path = path;
    elemToReturn.props.label = schema.schema.title;
    elemToReturn.props.required = schema.required;
    elemToReturn.props.output = "list";
    elemToReturn.props.onSelect = (event) => {
        if (event.target.tagName == "DROPDOWN-MULTI-SELECT" && event.target.selected) {
            handleChange(path, JSON.parse(event.target.selected));
        }
    };
    if (schema?.schema?.description) {
        elemToReturn.props.description = schema.schema.description;
    }
    if (schema?.schema?.items?.oneOf) {
        elemToReturn.props.options = JSON.stringify(schema.schema.items.oneOf);
    }
    return elemToReturn;
}

/* EXCLUDES DROPDOWN */

function excludesCustomTester(uischema, schema, context) {
    if (!uischema.scope) return LOWEST_RANK;
    if (uischema.customComponent == "dropdown-exclude") return HIGH_RANK;
    return LOWEST_RANK;
}

function excludesCustomRenderer(data, handleChange, path, schema) {
    let elemToReturn = { tag: "dropdown-excludes", props: {} };
    elemToReturn.props.id = schema.uischema.scope;
    elemToReturn.props.selected = data == null ? schema.schema.default : JSON.stringify(data);
    elemToReturn.props.path = path;
    elemToReturn.props.label = schema.schema.title;
    elemToReturn.props.required = schema.required;
    elemToReturn.props.onSelect = (event) => {
        if (event.target.tagName == "DROPDOWN-EXCLUDES" && event.target.selected) {
            handleChange(path, JSON.parse(event.target.selected));
        }
    };
    if (schema?.schema?.description) {
        elemToReturn.props.description = schema.schema.description;
    }
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
        elem.appendRenderer({
            tester: textInputNumberCustomTester,
            renderer: textInputNumberCustomRenderer,
        });
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
            tester: multiSelectDropdownObjectCustomTester,
            renderer: multiSelectDropdownObjectCustomRenderer,
        });
        elem.appendRenderer({
            tester: multiSelectDropdownListCustomTester,
            renderer: multiSelectDropdownListCustomRenderer,
        });
        elem.appendRenderer({
            tester: excludesCustomTester,
            renderer: excludesCustomRenderer,
        });
    }
});

/* CHECK READONLY */

document.body.addEventListener("json-form:mounted", (event) => {
    let elem = event.detail[0].target;
    if (elem.readonly == "true") {
        const inputs = document.querySelector("form").querySelectorAll("input, textarea");
        const dropdowns = document.querySelector("form").querySelectorAll(".dropdown");

        inputs.forEach((el) => {
            el.disabled = true;
            // Save placeholder if not already saved
            if (!el.dataset.originalPlaceholder) {
                el.dataset.originalPlaceholder = el.placeholder;
            }
            el.placeholder = "";
        });

        dropdowns.forEach((dropdown) => {
            dropdown.classList.add("disabled");
        });
    }
});

document.body.addEventListener("json-form:updated", (event) => {
    const inputs = document.querySelector("form").querySelectorAll("input, textarea");
    const dropdowns = document.querySelector("form").querySelectorAll(".dropdown");

    let elem = event.detail[0].target;
    if (elem.readonly == "true") {
        inputs.forEach((el) => {
            el.disabled = true;
            // Save placeholder if not already saved
            if (!el.dataset.originalPlaceholder) {
                el.dataset.originalPlaceholder = el.placeholder;
            }
            el.placeholder = "";
        });

        dropdowns.forEach((dropdown) => {
            dropdown.classList.add("disabled");
        });
    }
    if (elem.readonly == "false") {
        inputs.forEach((el) => {
            el.disabled = false;
            // Restore original placeholder if we have it
            if (el.dataset.originalPlaceholder !== undefined) {
                el.placeholder = el.dataset.originalPlaceholder;
            }
        });

        dropdowns.forEach((dropdown) => {
            dropdown.classList.remove("disabled");
        });
    }
});
