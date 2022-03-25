import React from 'react';
import { useGoogleLogout } from 'react-google-login';
import Constants from '../../settings';

const clientId = Constants.CLIENT_ID

function LogoutHooks() {
  const onLogoutSuccess = (res) => {
    try{
      console.log('Logged out Success');
      sessionStorage.removeItem('sessionObj');
      fetch(Constants.API_DOMAIN+'/user/logout', {
        method: 'POST',
        mode: Constants.CORS,
        headers: {
          'Accept': 'application/json',
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({'user_id': JSON.parse(sessionStorage.getItem('googleObj')).id})
      })
      sessionStorage.removeItem("googleObj")
    } catch (error){
      console.log(error);
    }
    window.location.replace("./#");

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