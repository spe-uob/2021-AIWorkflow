import React from 'react';
import Login from '../../components/Login/Login';
import Logout from '../../components/Logout/Logout';

const LoginPage = () => {
  return <div className="App">
    <div>    
      <h3>You are logged out.</h3>
    </div>
    <br/>
    <div>
      <Login/>
    </div>
    <br/>
    <div >
      <Logout/>
    </div>
  </div>;
};

export default LoginPage;
