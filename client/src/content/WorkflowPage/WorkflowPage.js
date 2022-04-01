import React, { useState } from "react";
import { useRete } from "./rete";
import {Button}  from 'carbon-components-react';
import "./_workflow-page.scss";

function Editor() {
  const [setContainer] = useRete();

  return (
    <div
      style={{
        width: "100vw",
        height: "100vh"
      }}
      ref={(ref) => ref && setContainer(ref)}
    />
  );
}

function WorkflowPage() {
  const [visible,] = useState(true);
  
  return (
    
    <div className="Workflow-Page" >
      <Button className="run-workflow-button">Run workflow</Button>
      {visible && <Editor />}
    </div>
  );
}
export default WorkflowPage
