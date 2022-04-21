import cookie from 'json-cookie';
import React from 'react';
import Login from '../../components/Login/Login';
import Logout from '../../components/Logout/Logout';

const LoginPage = () => {
  var stri;
  var obj;
  if (cookie.get("googleObj") === "") {
    stri = "You are logged out."
    obj = <Login/>
  } else {
    stri = "You are logged in."
    obj = <Logout/>
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
