const HIGH_RANK = 3;
const LOWEST_RANK = -1;

/* TEXT INPUT */

function textInputCustomRenderer(data, handleChange, path, schema) {
  let elemToReturn = { "tag": "text-input", "props": {} }
  elemToReturn.props.id = schema.uischema.scope; 
  elemToReturn.props.value = data;
  elemToReturn.props.path = path; //is this needed?
  elemToReturn.props.onChange = (value) => { handleChange(value); };

  // Text Input Specific
  if (schema.schema.title) { elemToReturn.props.label = schema.schema.title; }
  if (schema.schema.placeholder) { elemToReturn.props.placeholder = schema.schema.placeholder; }

  return elemToReturn
}

function textInputCustomTester(uischema, schema, context){
  if(!uischema.scope) return LOWEST_RANK;

  // List of scope that require text input
  if (uischema.scope.endsWith("name") || 
      uischema.scope.endsWith("address") ||
      uischema.scope.endsWith("lead-bind-address") ||
      uischema.scope.endsWith("pschedular-address") 
      ) return HIGH_RANK;
  return LOWEST_RANK;
}

/* TEXT INPUT AREA */

function textInputAreaCustomRenderer(data, handleChange, path, schema) {
  let elemToReturn = { "tag": "text-input-area", "props": {} }
  elemToReturn.props.id = schema.uischema.scope; 
  elemToReturn.props.value = data;
  elemToReturn.props.path = path; //is this needed?
  elemToReturn.props.onChange = (value) => { handleChange(value); };

  // Text Input Area Specific
  if (schema.schema.title) { elemToReturn.props.label = schema.schema.title; }
  if (schema.schema.placeholder) { elemToReturn.props.placeholder = schema.schema.placeholder; }

  return elemToReturn
}

function textInputAreaCustomTester(uischema, schema, context){
  if(!uischema.scope) return LOWEST_RANK;

  // List of scope that require text input
  if (uischema.scope.endsWith("_meta")
      ) return HIGH_RANK;
  return LOWEST_RANK;
}

/* CHECK BOX */

function checkBoxCustomRenderer(data, handleChange, path, schema) {
  let elemToReturn = { "tag": "simple-checkbox", "props": {} }

  elemToReturn.props.id = schema.uischema.scope; 
  elemToReturn.props.checked = data;
  elemToReturn.props.path = path;
  elemToReturn.props.onChange = (value) => { handleChange(value); };

  // Check box Specific
  if (schema.schema.title) { elemToReturn.props.label = schema.schema.title; }

  return elemToReturn
}

function checkBoxCustomTester(uischema, schema, context){
  if(!uischema.scope) return LOWEST_RANK;

  // List of scope that require text input
  if (uischema.scope.endsWith("disabled") || 
      uischema.scope.endsWith("no-agent")
      ) return HIGH_RANK;
  return LOWEST_RANK;
}

/* MULTI SELECT DROPDOWN */

function multiSelectDropdownCustomRenderer(data, handleChange, path, schema) {
  let elemToReturn = { "tag": "multi-select-dropdown", "props": {} }
  elemToReturn.props.id = schema.uischema.scope; 
  elemToReturn.props.selected = data;
  elemToReturn.props.path = path; //is this needed?
  elemToReturn.props.onChange = (value) => { handleChange(value); };
  if (schema.schema.title) { elemToReturn.props.label = schema.schema.title; }

  // Multi Select Specific
  if (schema.schema.options) { elemToReturn.props.options = schema.schema.options; }

  return elemToReturn
}

function multiSelectDropdownCustomTester(uischema, schema, context){
  if(!uischema.scope) return LOWEST_RANK;

  // List of scope that require multiselect drop down
  if(uischema.scope.endsWith("contexts")) return HIGH_RANK;
  return LOWEST_RANK;
}

/* REGISTER RENDERERS */

document.body.addEventListener('json-form:beforeMount', (event) => {
  let elem = event.detail[0].target;
  if(elem) {
    elem.appendRenderer({ tester: textInputCustomTester, renderer: textInputCustomRenderer });
    elem.appendRenderer({ tester: checkBoxCustomTester, renderer: checkBoxCustomRenderer });
    elem.appendRenderer({ tester: textInputAreaCustomTester, renderer: textInputAreaCustomRenderer });
    elem.appendRenderer({ tester: multiSelectDropdownCustomTester, renderer: multiSelectDropdownCustomRenderer });
  } 
});


