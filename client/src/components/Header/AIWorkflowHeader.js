import React from 'react';
import {
  Header,
  HeaderContainer,
  HeaderName,
  HeaderNavigation,
  HeaderMenuButton,
  HeaderMenuItem,
  HeaderGlobalBar,
  HeaderGlobalAction,
  SkipToContent,
  SideNav,
  SideNavItems,
  HeaderSideNavItems,
} from 'carbon-components-react';
import {
  Notification20,
  UserAvatar20,
} from '@carbon/icons-react';
import { Link } from 'react-router-dom';

function goToLogin(){
  window.location.replace("./#/profile");
}

const AIWorkflowHeader = () => (
  <HeaderContainer
    render={({ isSideNavExpanded, onClickSideNavExpand }) => (
      <Header aria-label="AI Workflow">
        <SkipToContent />
        <HeaderMenuButton
          aria-label="Open menu"
          onClick={onClickSideNavExpand}
          isActive={isSideNavExpanded}
        />
        <HeaderName element={Link} to="/" prefix="IBM">
          AI Workflow
        </HeaderName>
        <HeaderNavigation aria-label="AI Workflow">
          <HeaderMenuItem element={Link} to="/workflow_demo">
            Workflow Demo
          </HeaderMenuItem>
        </HeaderNavigation>
        <HeaderNavigation aria-label="AI Workflow">
          <HeaderMenuItem element={Link} to="/workflow">
            Workflow
          </HeaderMenuItem>
        </HeaderNavigation>
        
        <SideNav
          aria-label="Side navigation"
          expanded={isSideNavExpanded}
          isPersistent={false}>
          <SideNavItems>
            <HeaderSideNavItems>
              <HeaderMenuItem element={Link} to="/workflow_demo">
                Workflow Demo
              </HeaderMenuItem>
            </HeaderSideNavItems>
          </SideNavItems>
        </SideNav>
        <HeaderGlobalBar>
          <HeaderGlobalAction aria-label="Notifications">
            <Notification20 />
          </HeaderGlobalAction>
          <HeaderGlobalAction aria-label="Profile" onClick={goToLogin} tooltipAlignment="end">            <UserAvatar20 />
          </HeaderGlobalAction>
        </HeaderGlobalBar>
      </Header>
    )}
  />
);

export default AIWorkflowHeader;
