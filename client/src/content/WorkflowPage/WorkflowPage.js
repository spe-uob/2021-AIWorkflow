import React, { useState } from "react";
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
function handleClick(){
    console.log(JSON.parse(sessionStorage.getItem("workflowObj")));
    workflowObj = sessionStorage.getItem("workflowObj")
    userId = JSON.parse(sessionStorage.getItem("googleObj")).id
    fetch(Constants.API_DOMAIN+'/workflow/run', {
      method: 'POST',
      mode: Constants.CORS,
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + JSON.parse(sessionStorage.getItem('googleObj')).code
      },
      body: JSON.stringify({'workflow': workflowObj, 'user_id': userId})
    })
}
function WorkflowPage() {
  if (sessionStorage.getItem("googleObj") === null) {
    window.location.assign("./#/profile")
  }
  const [visible,] = useState(true);
  
  return (
    <div className="workflow-page" >
      <Button onClick={handleClick} className="run-workflow-button">Run workflow</Button>
      {visible && <Editor />}
    </div>
  );
}
export default WorkflowPage;
