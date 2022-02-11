import React from 'react';
import { useGoogleLogout } from 'react-google-login';

const clientId = '516108771432-8r055agb6k336emqdqh242s4c73lduf7.apps.googleusercontent.com';


function LogoutHooks() {
  const onLogoutSuccess = (res) => {
    console.log('Logged out Success');
    sessionStorage.removeItem('sessionObj');
    window.location.replace("./");
    fetch('localhost:5001', {
      method: 'POST',
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
      },
      body: {'Hashed-Email': res.googleId}
    })
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