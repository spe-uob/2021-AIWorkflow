import React from 'react';
import Login from '../../components/Login/Login';
import Logout from '../../components/Logout/Logout';

if (sessionStorage.getItem("sessionObj") == null) {
  var stri = "You are logged out."
} else {
  var stri = "You are logged in as " + sessionStorage.sessionObj
}

const LoginPage = () => {
  return <div className="App">
    <br/>
    <div>    
      <h1>{stri}</h1>
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
