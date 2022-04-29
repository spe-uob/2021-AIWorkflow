import React from 'react';
import { shallow } from 'enzyme';
import LandingPage from './content/LandingPage';
import LoginPage from './content/LoginPage';

import WorkflowPage from "./content/WorkflowPage"


describe('Pages load properly', () => {
  it('renders landing page without crashing', () => {
    shallow(<LandingPage />);
  });
  it('renders login page without crashing', () => {
    shallow(<LoginPage />);
  });
  
  it('renders Workflow page without crashing', () => {
    shallow(<WorkflowPage />);
  });
});
