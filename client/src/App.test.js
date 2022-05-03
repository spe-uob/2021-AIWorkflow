import React from 'react';
import { shallow } from 'enzyme';
import LandingPage from './content/LandingPage';

import ProfilePage from "./content/ProfilePage"
import WorkflowPage from "./content/WorkflowPage"


describe('Pages load properly', () => {
  it('renders landing page without crashing', () => {
    shallow(<LandingPage />);
  });
 
  it('renders Workflow page without crashing', () => {
    shallow(<WorkflowPage />);
  });
  it('renders landing page without crashing', () => {
    shallow(<ProfilePage />);
  });
});
