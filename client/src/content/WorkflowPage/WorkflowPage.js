

import React, { useEffect, useState } from "react";
import ReactDOM from "react-dom";
import { useRete } from "./rete";

import "./styles.css";

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
    <div className="App">
      <button onClick={() => setVisible(false)}>Destroy</button>
      <button onClick={() => setVisible(true)}>Restore</button>
      {visible && <Editor />}
    </div>
  );
}






export default WorkflowPage
