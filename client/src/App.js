import React, { Component } from 'react';
import './app.scss';
import { Content } from 'carbon-components-react';
import AIWorkflowHeader from './components/Header';
import { Route, Routes } from 'react-router-dom';
import LandingPage from './content/LandingPage';
import WorkflowDemoPage from './content/WorkflowDemoPage';

class App extends Component {
  render() {
    return (
      <>
        <AIWorkflowHeader />
        <Content>
          <Routes>
            <Route exact path="/" element={<LandingPage/ >} />
            <Route path="/workflow_demo" element={<WorkflowDemoPage/>} />
          </Routes>
        </Content>
      </>
    );
  }
}

export default App;