import cookie from 'json-cookie';
import React from 'react';
import Login from '../../components/Login/Login';
import Logout from '../../components/Logout/Logout';

const LoginPage = () => {
  console.log(cookie.get("googleObj"));
  if (cookie.get("googleObj") === "") {
    return (
      <div>
        <div>
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
      <div>
        <img src={picture} alt="logo" />
        <p>Welcome back, {name}</p>
        <p>email: {email}</p>
        <Logout/>
      </div>
    )
  }

};

export default LoginPage;
