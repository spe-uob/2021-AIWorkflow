import React from 'react';
import {
  Button,
  Form,
  FormGroup,
  Search,
  Checkbox,
  DatePicker,
  DatePickerInput
} from 'carbon-components-react';
import {runWorkflowDemo} from './workflow_demo.js';

const fieldsetKeywordBoxProps = {
  className: "demo-workflow-class",
  legendText: "Keywords (Seperate Terms By Comma)"
}

const fieldsetCheckboxProps ={
  className: "demo-workflow-class",
  legendText: "Tones"
}

const keywordBoxProps = {
  className: "demo-workflow-class",
}

const datePickerBoxProps = {
  className: "demo-workflow-class",
  legendText: "Date Range"
}


const WorkflowDemoPage = () => {
  return (
  <div className="bx--grid bx--grid--full-width">
    <br />
    <h1>Workflow Demo</h1> 
    This runs a demo workflow that:
    <ul>
      <li>- Calls the Twitter API and gets a list of tweets based on the given keywords (anonymised)</li>
      <li>- Calls the Tone Analyzer API and gets the tonality of the tweets</li>
      <li>- Appends the Results to Google Sheet(s) and Google Slide(s)</li>
    </ul>
    <br />
    <Form id="demo_workflow_form">
      <FormGroup {...fieldsetKeywordBoxProps}>
        <Search {...keywordBoxProps} id="keywords" labelText="" placeholder="IBM Cloud, VPC, Watson" />
      </FormGroup>
      <FormGroup {...fieldsetCheckboxProps}>
        <Checkbox labelText="Positive" id="tones" value="positive"/>
        <Checkbox labelText="Negative" id="tones1" value="negative" />
      </FormGroup>
      <FormGroup {...datePickerBoxProps}>
        <DatePicker datePickerType="range">
          <DatePickerInput
            id="date_start"
            placeholder="mm/dd/yyyy"
            labelText="Start date"
          />
          <DatePickerInput
            id="date_end"
            placeholder="mm/dd/yyyy"
            labelText="End date"
          />
        </DatePicker>
      </FormGroup>
      <Button onClick={runWorkflowDemo} type="submit">Run Demo Workflow</Button>
    </Form>
    <script src="/workflow_demo.js"></script>
  </div>
  );};

export default WorkflowDemoPage;


