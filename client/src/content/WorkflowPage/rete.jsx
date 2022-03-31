import React, { useState, useEffect, useRef } from "react";
import 'regenerator-runtime';
import Rete from "rete";
import ReactRenderPlugin from "rete-react-render-plugin";
import ConnectionPlugin from "rete-connection-plugin";
import AreaPlugin from "rete-area-plugin";
import { MyNode } from "./MyNode";

// Created sockets
var strSocket = new Rete.Socket("String value");
var boolSocket = new Rete.Socket("Boolean value");


// created controls
// class NumControl extends Rete.Control {
//   static component = ({ value, onChange }) => (
//     <input
//       type="number"
//       value={value}
//       ref={(ref) => {
//         ref && ref.addEventListener("pointerdown", (e) => e.stopPropagation());
//       }}
//       onChange={(e) => onChange(+e.target.value)}
//     />
//   );

//   constructor(emitter, key, node, readonly = false) {
//     super(key);
//     this.emitter = emitter;
//     this.key = key;
//     this.component = NumControl.component;

//     const initial = node.data[key] || 0;

//     node.data[key] = initial;
//     this.props = {
//       readonly,
//       value: initial,
//       onChange: (v) => {
//         this.setValue(v);
//         this.emitter.trigger("process");
//       }
//     };
//   }

//   setValue(val) {
//     this.props.value = val;
//     this.putData(this.key, val);
//     this.update();
//   }
// }
class CheckboxControl extends Rete.Control{
  static component = ({ label, value, onChange }) => (
    <div>
      <input
      id="checkbox"
      type="checkbox"
      checked={value}
      onChange={(e) => onChange(e.target.value)}
    />
    <label>{label}</label>
    </div>
  );

  constructor(emitter, key, node, readonly = false) {
    super(key);
    this.emitter = emitter;
    this.key = key;
    this.component = CheckboxControl.component;

    const initial = node.data[key] || false;

    node.data[key] = initial;
    this.props = {
      readonly,
      label: key,
      value: initial,
      onChange: (v) => {
        this.setValue(v);
        this.emitter.trigger("process");
      }
    };
  }

  setValue(val) {
    this.props.value = val;
    this.putData(this.key, val);
    this.update();
  }
}

class TextControl extends Rete.Control{
  static component = ({ value, onChange }) => (
    <input
      type="text"
      value={value}
      onChange={(e) => onChange(e.target.value)}
    />
  );

  constructor(emitter, key, node, readonly = false) {
    super(key);
    this.emitter = emitter;
    this.key = key;
    this.component = TextControl.component;

    const initial = node.data[key] || "IBM Cloud, VPC, Watson";

    node.data[key] = initial;
    this.props = {
      readonly,
      value: initial,
      onChange: (v) => {
        this.setValue(v);
        this.emitter.trigger("process");
      }
    };
  }

  setValue(val) {
    this.props.value = val;
    this.putData(this.key, val);
    this.update();
  }
}


//created components
// class NumComponent extends Rete.Component {
//   constructor() {
//     super("Number");
//   }

//   builder(node) {
//     var out1 = new Rete.Output("num", "Number", numSocket);
//     var ctrl = new NumControl(this.editor, "num", node);

//     return node.addControl(ctrl).addOutput(out1);
//   }

//   worker(node, inputs, outputs) {
//     outputs["num"] = node.data.num;
//   }
// }
// class AddComponent extends Rete.Component {
//   constructor() {
//     super("Add");
//     this.data.component = MyNode; // optional
//   }

//   builder(node) {
//     var inp1 = new Rete.Input("num1", "Number", numSocket);
//     var inp2 = new Rete.Input("num2", "Number2", numSocket);
//     var out = new Rete.Output("num", "Number", numSocket);

//     inp1.addControl(new NumControl(this.editor, "num1", node));
//     inp2.addControl(new NumControl(this.editor, "num2", node));

//     return node
//       .addInput(inp1)
//       .addInput(inp2)
//       .addControl(new NumControl(this.editor, "preview", node, true))
//       .addOutput(out);
//   }

//   worker(node, inputs, outputs) {
//     var n1 = inputs["num1"].length ? inputs["num1"][0] : node.data.num1;
//     var n2 = inputs["num2"].length ? inputs["num2"][0] : node.data.num2;
//     var sum = n1 + n2;

//     this.editor.nodes
//       .find((n) => n.id === node.id)
//       .controls.get("preview")
//       .setValue(sum);
//     outputs["num"] = sum;
//   }
// }
class SearchTwitterComponent extends Rete.Component {
  constructor() {
    super("Search Twitter");
    this.data.component = MyNode; // optional
  }
    
  builder(node) {
    var ctrl = new TextControl(this.editor, "keywords", strSocket);
    var out = new Rete.Output("tweets", "Tweets", strSocket);

    return node
    .addControl(ctrl)
    .addOutput(out);
  }

  worker(node, inputs, outputs) {
    outputs["tweets"] = node.data.keywords;
  }
}
class GoogleSheets extends Rete.Component {
  constructor() {
    super("Write to google sheets");
    this.data.component = MyNode; // optional
  }

  builder(node) {
    var inp1 = new Rete.Input("tweets", "Tweets", strSocket);
    var out = new Rete.Output("tweets", "Tweets", strSocket);
    
    return node
      .addInput(inp1)
      .addOutput(out);
  }
  worker(node, inputs, outputs) {
   
    outputs["tweets"] = node.data;
  }
}
class ToneAnalyzerComponent extends Rete.Component {
  constructor() {
    super("Tone Analyzer");
    this.data.component = MyNode; // optional
  }
    
  builder(node) {
    var inp = new Rete.Input("tweets","Tweets",strSocket)
    var positiveCtrl = new CheckboxControl(this.editor, "Positive", boolSocket);
    var negativeCtrl = new CheckboxControl(this.editor, "Negative", boolSocket);
    var out = new Rete.Output("analyzed tweets", "Analyzed Tweets", strSocket);

    return node
    .addInput(inp)
    .addControl(positiveCtrl)
    .addControl(negativeCtrl)
    .addOutput(out);
  }

  worker(node, inputs, outputs) {
    outputs["analyzed tweets"] = node.data.keywords;
  }
}
class GoogleSlides extends Rete.Component {
  constructor() {
    super("Write to google slides");
    this.data.component = MyNode; // optional
  }

  builder(node) {
    var inp1 = new Rete.Input("analyzed tweets", "Analyzed Tweets", strSocket);
    var out = new Rete.Output("tweets", "Tweets", strSocket);

    return node
      .addInput(inp1)
      .addOutput(out);
  }

  worker(node, inputs, outputs) {
      outputs["tweets"] = node.data
  }
}
export async function createEditor(container) {
  var components = [new SearchTwitterComponent(),new ToneAnalyzerComponent(),new GoogleSheets(),new GoogleSlides()];

  var editor = new Rete.NodeEditor("demo@0.1.0", container);
  editor.use(ConnectionPlugin);
  editor.use(ReactRenderPlugin);

  var engine = new Rete.Engine("demo@0.1.0");

  components.forEach((c) => { 
    editor.register(c);
    engine.register(c);
  });

  // var n1 = await components[0].createNode({ num: 2 });
  // var n2 = await components[0].createNode({ num: 3 });
  // var add = await components[1].createNode();
  var twitter = await components[0].createNode();
  var toneAnalyzer= await components[1].createNode();
  var googleSheets = await components[2].createNode()
  var googleSlides =await components[3].createNode()

  // n1.position = [80, 200];
  // n2.position = [80, 400];
  // add.position = [500, 240];
  twitter.position = [0, 800];
  toneAnalyzer.position=[600,800];
  googleSheets.position=[300,800];
  googleSlides.position=[900,800]
  // editor.addNode(n1);
  // editor.addNode(n2);
  // editor.addNode(add);
  editor.addNode(twitter);
  editor.addNode(toneAnalyzer)
  editor.addNode(googleSheets)
  editor.addNode(googleSlides)

  // editor.connect(n1.outputs.get("num"), add.inputs.get("num1"));
  // editor.connect(n2.outputs.get("num"), add.inputs.get("num2"));
  editor.connect(twitter.outputs.get("tweets"), googleSheets.inputs.get("tweets"));
  editor.connect(googleSheets.outputs.get("tweets"), toneAnalyzer.inputs.get("tweets"));
  editor.connect(toneAnalyzer.outputs.get("analyzed tweets"), googleSlides.inputs.get("analyzed tweets"));
  
  editor.on(
    "process nodecreated noderemoved connectioncreated connectionremoved",
    async () => {
      console.log("process");
      console.log(editor.toJSON());
      await engine.abort();
      await engine.process(editor.toJSON());
    }
  );

  editor.view.resize();
  editor.trigger("process");
  AreaPlugin.zoomAt(editor, editor.nodes);

  return editor;
}

export function useRete() {
  const [container, setContainer] = useState(null);
  const editorRef = useRef();

  useEffect(() => {
    if (container) {
      createEditor(container).then((value) => {
        console.log("created");
        editorRef.current = value;
      });
    }
  }, [container]);

  useEffect(() => {
    return () => {
      if (editorRef.current) {
        console.log("destroy");
        editorRef.current.destroy();
      }
    };
  }, []);

  return [setContainer];
}
