import React from 'react';
import { useGoogleLogout } from 'react-google-login';
import { CLIENT_ID, CORS, API_DOMAIN } from '../../settings';
import { Button } from "carbon-components-react";
import cookie from "json-cookie";

const clientId = CLIENT_ID;

function LogoutHooks() {
  const onLogoutSuccess = (res) => {
    try{
      fetch(API_DOMAIN()+'/user/logout', {
        method: 'POST',
        mode: CORS,
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
    <Button onClick={signOut} className="button">
      Sign out
    </Button>
  );
}

export default LogoutHooks;