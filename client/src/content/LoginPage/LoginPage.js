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
    <div className="leftPart" >

      {/* <img src={picture} alt="logo" /> */}
        <h2>name:</h2>
        <h2>email:</h2>
    </div>
    <div className="rightPart">
      <br/>
      <div>    
          <h1>{stri}</h1>
         {obj}
      </div>
    </div>
  </div>;
  
};

export default LoginPage;
