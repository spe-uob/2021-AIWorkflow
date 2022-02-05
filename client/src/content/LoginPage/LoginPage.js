import React from 'react';
import Login from '../../components/Login/Login';
import Logout from '../../components/Logout/Logout';

const LoginPage = () => {
  return <div>
    <h3>You are logged out.</h3>
    <Login/><Logout/>
  </div>;
};

export default LoginPage;
