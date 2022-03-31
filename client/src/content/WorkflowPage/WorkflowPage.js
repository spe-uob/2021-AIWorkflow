import React, { useState } from "react";
import { useRete } from "./rete";


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
    <div className="Workflow-Page">
      {/* <button onClick={() => setVisible(false)}>Destroy</button>
      <button onClick={() => setVisible(true)}>Restore</button> */}
      {visible && <Editor />}
    </div>
  );
}
export default WorkflowPage
