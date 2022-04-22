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
import CookieConsent from "react-cookie-consent";

class App extends Component {
  render() {
    return (
      <div>
        <AIWorkflowHeader />
        <Content>
          <Routes basename="/">
            <Route exact path="/" element={<LandingPage/>}/>
            <Route path="/workflow_demo" element={<WorkflowDemoPage/>}/>
            <Route path="/profile" element={<LoginPage/>}/>
            <Route path="/workflow" element={<WorkflowPage/>}/>
          </Routes>
        </Content>
        <CookieConsent location="bottom" cookieName="ibm-aiworkflow-accept-cookies" expires={999} overlay>
            This website uses cookies to store login information. If you would like not to use cookies, don't login.
        </CookieConsent>
      </div>
    );
  }
}

export default App;
