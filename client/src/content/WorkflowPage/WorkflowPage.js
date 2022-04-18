import React, { useState } from "react";
import { useRete } from "./rete";
import {Button}  from 'carbon-components-react';
import "./_workflow-page.scss";
//import { MyNode } from "./MyNode";


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
}
function WorkflowPage() {
  const [visible,] = useState(true);
  
  return (
    <div className="workflow-page" >
      <Button onClick={handleClick} className="run-workflow-button">Run workflow</Button>
      {visible && <Editor />}
    </div>
  );
}
export default WorkflowPage;
