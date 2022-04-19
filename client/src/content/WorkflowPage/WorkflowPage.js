import React from "react";
import { useRete } from "./rete";
import {Button}  from 'carbon-components-react';
import "./_workflow-page.scss";
import Constants from '../../settings';



function Editor() {
  const [setContainer] = useRete();

  return (
    <div
      className="workflow-editor-container"
      ref={(ref) => ref && setContainer(ref)}
    />
  );
}

function WorkflowPage() {
  if (sessionStorage.getItem("googleObj") === null) {
    window.location.assign("./#/profile")
  }

  function run_workflow(){
    
    console.log(JSON.parse(sessionStorage.getItem("workflowObj")));
    const workflowObj = JSON.parse(sessionStorage.getItem("workflowObj"))
    const userId = JSON.parse(sessionStorage.getItem("googleObj")).id
    fetch(Constants.API_DOMAIN+'/workflow/run', {
      method: 'POST',
      mode: Constants.CORS,
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + JSON.parse(sessionStorage.getItem('googleObj')).code
      },
      body: JSON.stringify({'user_id': userId, 'workflow': workflowObj})
    })
  }
  
  return (
    <div className="workflow-page" >
        <div className={"desc"}>
          <b>Workflow Editor</b>
        </div>
        <Button className="run-workflow-button" onClick={run_workflow} type="submit">Run Workflow</Button>
      <Editor />
    </div>
  );
}

export default WorkflowPage;