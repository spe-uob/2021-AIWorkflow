import React from 'react';
import Login from '../../components/Login/Login';
import Logout from '../../components/Logout/Logout';

const LoginPage = () => {
  return <div>
    <div>    
      <h3>You are logged out.</h3>
    </div>
    <div>
      <Login/>
    </div>
    <div >
      <Logout/>
    </div>
  </div>;
};

export default LoginPage;
