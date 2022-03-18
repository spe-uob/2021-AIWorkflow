import React from 'react';
import { shallow } from 'enzyme';
import LandingPage from './content/LandingPage';
import LoginPage from './content/LoginPage';
import WorkflowDemoPage from './content/WorkflowDemoPage';


describe('Pages load properly', () => {
  it('renders landing page without crashing', () => {
    shallow(<LandingPage />);
  });
  it('renders landing page without crashing', () => {
    shallow(<LoginPage />);
  });
  it('renders landing page without crashing', () => {
    shallow(<WorkflowDemoPage />);
  });

  // const wrapper = shallow(<RepoPage />);
  // it('contains a RepoTable', () => {
  //   expect(wrapper.find('RepoTable').length).toBe(1);
  // });
});
