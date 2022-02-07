import React from 'react';
import Login from '../../components/Login/Login';
import Logout from '../../components/Logout/Logout';

const LoginPage = () => {
  if (sessionStorage.getItem("sessionObj") == null) {
    var stri = "You are logged out."
    var obj = <Login/>
  } else {
    var stri = "You are logged in as " + JSON.parse(sessionStorage.sessionObj).profileObj.name
    var obj = <Logout/>
  }

  return <div className="App">
    <br/>
    <div>    
      <h1>{stri}</h1>
    </div>
    <br/>
    <div>
      {obj}
    </div>
  </div>;
};

export default LoginPage;
