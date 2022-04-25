import React from 'react';
import { useGoogleLogout } from 'react-google-login';
import cookie from "json-cookie";

const clientId = process.env.REACT_APP_CLIENT_ID;

function LogoutHooks() {
  const onLogoutSuccess = (res) => {
    try{
      fetch(process.env.REACT_APP_API_DOMAIN+'/user/logout', {
        method: 'POST',
        mode: process.env.REACT_APP_CORS,
        headers: {
          'Accept': 'application/json',
          'Content-Type': 'application/json',
          'Authorization': 'Bearer ' + cookie.get('googleObj').code
        },
        body: JSON.stringify({'user_id': cookie.get('googleObj').id})
      })
      
    } catch (error){
      console.log(error);
    }
    cookie.delete("googleObj");
    console.log('Logged out Success');
    window.location.replace("./");
  };

  const onFailure = () => {
    console.log('Handle failure cases');
  };

  const { signOut } = useGoogleLogout({
    clientId,
    onLogoutSuccess,
    onFailure,
  });

  return (
    <button onClick={signOut} className="button">
      <img src="icons/google.svg" alt="google login" className="icon"></img>

      <span className="buttonText">Sign out</span>
    </button>
  );
}

export default LogoutHooks;