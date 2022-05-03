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
    else {
      var picture = cookie.get("googleObj").picture;
      var email = cookie.get("googleObj").email;
      var name = cookie.get("googleObj").name;
      return (
        <div className="profile-container">
          <div className={"background"}>
            <img src={"./login-background.png"} alt={"lol"}/>
          </div>
          <div>
            <img className={"profile-pic"} src={picture} alt="logo" />
            <p><span className={"bold"}>Name: </span>{name}</p>
            <p><span className={"bold"}>Email: </span> {email}</p>
            <Logout/>
          </div>
        </div>
      )
    }
};

export default ProfilePage;
