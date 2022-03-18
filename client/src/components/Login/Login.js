import React from 'react';
import { useGoogleLogin } from 'react-google-login';
import Constants from '../../settings';

const clientId = Constants.CLIENT_ID

function Login() {
  const onSuccess = (res) => {
    try {
      console.log('Login Success: currentUser:', res);
      sessionStorage.setItem('sessionObj', JSON.stringify(res));
      console.log(sessionStorage.getItem("sessionObj"));
      var googleObj = null;
      var sanitisedCode = String.raw`${res.code}`.replace("\\", "\\\\");
      console.log(sanitisedCode);
      fetch('http://localhost:5001/user/login', {
        method: 'POST',
        mode: 'cors',
        headers: {
          'Accept': 'application/json',
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({'code': sanitisedCode})
      }).then(response => response.json())
      .then(data => googleObj = data)
      .then(() => console.log(googleObj))
      .then(() => sessionStorage.setItem("googleObj", JSON.stringify(googleObj.data.google_object)));
    } catch (error) {
      console.log(error);
    }
    window.location.replace("./");

  };

  const onFailure = (res) => {
    console.log('Login failed: res:', res);
  };

  const { signIn } = useGoogleLogin({
    onSuccess,
    onFailure,
    clientId,
    isSignedIn: false,
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