import React, {useState} from 'react';
import {
  Button,
  Form,
  FormGroup,
  Search,
  Checkbox,
  DatePicker,
  DatePickerInput,
  InlineLoading
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
  if (sessionStorage.getItem("googleObj") === null) {
    window.location.assign("./profile")
  }
  function FormSubmission({children}) {
      const [isSubmitting, setIsSubmitting] = useState(false);
      const [success, setSuccess] = useState(false);
      const [description, setDescription] = useState('Submitting...');
      const [ariaLive, setAriaLive] = useState('off');
      const handleSubmit = async () => {
        setIsSubmitting(true);
        setSuccess(false);
        setAriaLive('assertive');
  

        setDescription('Running Workflow...');
        await runWorkflowDemo();
        setAriaLive('off');


        setSuccess(true);
        setDescription('Workflow Complete!');
      };
    
      return children({
        handleSubmit,
        isSubmitting,
        success,
        description,
        ariaLive,
      });
    }


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
        <Search {...keywordBoxProps} required id="keywords" labelText="" placeholder="IBM Cloud, VPC, Watson" />
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
      <FormSubmission>
      {({ handleSubmit, isSubmitting, success, description, ariaLive }) => (
        <div style={{ display: 'flex', width: '300px' }}>
          {isSubmitting || success ? (
            <InlineLoading
              style={{ marginLeft: '1rem' }}
              description={description}
              status={success ? 'finished' : 'active'}
              aria-live={ariaLive}
            />
          ) : (
            <Button className="form-submit-button" onClick={handleSubmit} type="submit">Run Demo Workflow</Button>
          )}
        </div>
      )}
      </FormSubmission>
    </Form>
    <script src="/workflow_demo.js"></script>
  </div>
  );};

export default WorkflowDemoPage;


