import React, { Component } from 'react';
import './app.scss';
import { Content } from 'carbon-components-react';
import AIWorkflowHeader from './components/Header';
import {
  Route,
  Routes 
} from 'react-router-dom';
import LandingPage from './content/LandingPage';
import WorkflowDemoPage from './content/WorkflowDemoPage';
import LoginPage from './content/LoginPage';
import WorkflowPage from './content/WorkflowPage';

class App extends Component {
  render() {
    return (
      <div>
        <AIWorkflowHeader />
        <Content>
          <Routes basename="/">
            <Route exact path="/" element={<LandingPage/ >} />
            <Route path="/workflow_demo" element={<WorkflowDemoPage/>} />
            <Route path="/profile" element={<LoginPage/>}/>
            <Route exact path="/workflow">
              {sessionStorage.getItem('googleObj') === null ? <Redirect to="/profile" /> : <WorkflowPage />}
            </Route>        
          </Routes>
        </Content>
      </div>
    );
  }
}

export default App;
