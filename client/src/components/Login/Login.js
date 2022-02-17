import React from 'react';
import { useGoogleLogin } from 'react-google-login';

const clientId = '516108771432-k0ifm1hkdanslpbd44tojjqehni63bj5.apps.googleusercontent.com';

function Login() {
  const onSuccess = (res) => {
    console.log('Login Success: currentUser:', res);
    sessionStorage.setItem('sessionObj', JSON.stringify(res));
    fetch('localhost:5001', {
      method: 'POST',
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(res)
    })
    window.location.replace("./");
  };

  const onFailure = (res) => {
    console.log('Login failed: res:', res);
  };

  const { signIn } = useGoogleLogin({
    onSuccess,
    onFailure,
    clientId,
    isSignedIn: true,
    scope: "email profile https://www.googleapis.com/auth/drive https://www.googleapis.com/auth/spreadsheets https://www.googleapis.com/auth/presentations",
    prompt: "consent",
    responseType: "code",
    accessType: "offline",
  });

  return (
    <button onClick={signIn} className="button">
      <img src="icons/google.svg" alt="google login" className="icon"></img>

      <span className="buttonText">Sign in with Google</span>
    </button>
  );
}

export default Login;