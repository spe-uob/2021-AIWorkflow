import React, { useState } from "react";
import { useRete } from "./rete";
import {Button}  from 'carbon-components-react'

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
  const [visible, setVisible] = useState(true);
  
  return (
    
    <div className="Workflow-Page" >
      {/* <button onClick={() => setVisible(false)}>Destroy</button>
      <button onClick={() => setVisible(true)}>Restore</button> */}
      <Button style={{position:"fixed",bottom:"35px",right:"35px",width:"150px",height:"50px",display:"block",
whiteSpace:"nowrap",overflow:"hidden"}}>Run workflow</Button>
    


      {visible && <Editor />}
    </div>
  );
}
export default WorkflowPage
