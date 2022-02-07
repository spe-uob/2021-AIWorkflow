import React from 'react';
import { useGoogleLogin } from 'react-google-login';

const clientId = '516108771432-8r055agb6k336emqdqh242s4c73lduf7.apps.googleusercontent.com';


function Login() {
  const onSuccess = (res) => {
    console.log('Login Success: currentUser:', res.profileObj);
    alert(
      `Logged in successfully welcome ${res.profileObj.name} 😍. \n See console for full profile object.`
    );
    sessionStorage.setItem('sessionObj', JSON.stringify(res));
  };

  const onFailure = (res) => {
    console.log('Login failed: res:', res);
    alert(
      `Failed to login.`
    );
  };

  const { signIn } = useGoogleLogin({
    onSuccess,
    onFailure,
    clientId,
    isSignedIn: true,
  });

  return (
    <button onClick={signIn} className="button">
      <img src="icons/google.svg" alt="google login" className="icon"></img>

      <span className="buttonText">Sign in with Google</span>
    </button>
  );
}

export default Login;