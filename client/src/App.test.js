import React from 'react';
import { shallow } from 'enzyme';
import LandingPage from './content/LandingPage';
import LoginPage from './content/LoginPage';
import WorkflowDemoPage from './content/WorkflowDemoPage';


describe('Pages load properly', () => {
  it('renders landing page without crashing', () => {
    shallow(<LandingPage />);
  });
  it('renders login page without crashing', () => {
    shallow(<LoginPage />);
  });
  it('renders workflowDemo page without crashing', () => {
    shallow(<WorkflowDemoPage />);
  });
});
