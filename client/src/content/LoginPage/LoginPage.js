import React from 'react';
import Login from '../../components/Login/Login';
import Logout from '../../components/Logout/Logout';

const LoginPage = () => {
  var stri;
  var obj;
  if (sessionStorage.getItem("sessionObj") == null) {
    stri = "You are not signed in."
    obj = <Login/>
  } else {
    stri = "You are signed in."
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
