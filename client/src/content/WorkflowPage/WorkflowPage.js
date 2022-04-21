import React from "react";
import { Navigate } from 'react-router-dom';
import { useRete } from "./rete";
import {Button}  from 'carbon-components-react';
import "./_workflow-page.scss";
import Constants from '../../settings';

import cookie from "json-cookie";

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
    const workflowObj = JSON.parse(sessionStorage.getItem("workflowObj"))
    const userId = cookie.get("googleObj").id
    fetch(Constants.API_DOMAIN+'/workflow/run', {
      method: 'POST',
      mode: Constants.CORS,
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + cookie.get('googleObj').code
      },
      body: JSON.stringify({'user_id': userId, 'workflow': workflowObj})
    })
}
    
function WorkflowPage() {
  if (cookie.get("googleObj") === "") {
    return <Navigate to='/profile' replace={true}/>
  } else {
    return (
      <div className="workflow-page" >
        <div className={"desc"}>
          <b>Workflow Editor</b>
        </div>
        <Button onClick={handleClick} className="run-workflow-button">Run workflow</Button>
        <Editor />
      </div>
    );
  }
}

export default WorkflowPage;