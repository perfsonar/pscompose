import React, { useState, useEffect } from 'react';
import Form from '@rjsf/bootstrap-4';
import validator from '@rjsf/validator-ajv8';
import 'bootstrap/dist/css/bootstrap.min.css';
import './App.css';

const CustomFieldTemplate = (props) => {
  const {
    id,
    classNames,
    label,
    help,
    required,
    description,
    errors,
    children,
  } = props;

  return (
    <div className={classNames}>
      <label htmlFor={id}>{label}{required ? "*" : null}</label>
      {description && <p className="field-description">{description}</p>}
      {children}
      {errors && <div className="text-danger">{errors}</div>}
      {help && <div className="help-block">{help}</div>}
    </div>
  );
};
  
const TimeBetweenTestsField = (props) => {
  const { formData, onChange, schema, uiSchema } = props;

  const handleValueChange = (event) => {
    onChange({ ...formData, value: parseInt(event.target.value) });
  };

  const handleUnitChange = (event) => {
    onChange({ ...formData, unit: event.target.value });
  };

  return (
    <div className="form-row align-items-center">
      <div className="col">
        <label htmlFor="timeBetweenTests-value">{schema.properties.value.title}</label>
        <input
          type="number"
          className="form-control"
          id="timeBetweenTests-value"
          value={formData.value}
          onChange={handleValueChange}
        />
      </div>
      <div className="col">
        <label htmlFor="timeBetweenTests-unit">{schema.properties.unit.title}</label>
        <select
          className="form-control"
          id="timeBetweenTests-unit"
          value={formData.unit}
          onChange={handleUnitChange}
        >
          {schema.properties.unit.enum.map((unit) => (
            <option key={unit} value={unit}>
              {unit}
            </option>
          ))}
        </select>
      </div>
    </div>
  );
};
  
function App() {
  const [formData, setFormData] = useState(null);

  useEffect(() => {
    fetch('http://localhost:8000/pscompose/test/throughput2')
      .then(response => response.json())
      .then(data => setFormData(data))
      .catch(error => console.error('Error fetching form data:', error));
  }, []);

  const onSubmit = ({ formData }) => {
    console.log("Form submitted:", formData);
  };

  const onError = (errors) => {
    console.log("Form validation errors:", errors);
  };

  if (!formData) return <div className="container mt-5">Loading...</div>;

  const fields = {
    timeBetweenTestsField: TimeBetweenTestsField
  };

  return (
    <div className="container mt-5">
      <h1 className="mb-4">psCompose - Test Throughput</h1>
      <Form
        schema={formData.schema}
        uiSchema={formData.uiSchema}
        validator={validator}
        onSubmit={onSubmit}
        onError={onError}
        templates={{ FieldTemplate: CustomFieldTemplate }}
        fields={fields}
        liveValidate={true}
        showErrorList={false}
      />
    </div>
  );
}

export default App;