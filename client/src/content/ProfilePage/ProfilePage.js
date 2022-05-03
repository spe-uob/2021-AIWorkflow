import React from 'react';
import Login from '../../components/Login/Login';
import Logout from '../../components/Logout/Logout';
import cookie from "json-cookie";

const ProfilePage = () => {
  console.log(cookie.get("googleObj"));
  if (cookie.get("googleObj") === "") {
    return (
      <>
      <div className={"login-container"}>
        <div className={"background"}>
          <img src={"./login-background.png"} alt={"lol"}/>
        </div>
        <div className="login-text">
          <h1>Log in to IBM <span className={"bold"}>AIWorkflow</span></h1>
        </div>
        <div className={"login-with-google"}>
          <Login/>
        </div>
      </div>
      </>
    )}
};

export default ProfilePage;
