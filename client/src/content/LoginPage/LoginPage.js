import React from 'react';
import Login from '../../components/Login/Login';
import Logout from '../../components/Logout/Logout';

import cookie from "json-cookie";

const LoginPage = () => {
  console.log(cookie.get("googleObj"));
  if (cookie.get("googleObj") === "") {
    return (
      <div>
        <div className="login-info">
          <h1>You have not signed in.</h1>
        </div>
        <div>
          <Login/>
        </div>
      </div>
    )
  } else {
    var picture = cookie.get("googleObj").picture;
    var email = cookie.get("googleObj").email;
    var name = cookie.get("googleObj").name;
    return (
      <div className="user-information">
        <img src={picture} alt="logo" />
        <p>Welcome back, {name}</p>
        <p>email: {email}</p>
        <Logout/>
      </div>
    )
  }
};

export default LoginPage;
