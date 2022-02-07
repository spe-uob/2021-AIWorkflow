import React from 'react';
import {GoogleLogin} from 'react-google-login'

const clientId = '516108771432-8r055agb6k336emqdqh242s4c73lduf7.apps.googleusercontent.com';

function Login() {
    const onSuccess = (res) => {
        console.log('[Login Success] currentUser:', res);
        sessionStorage.setItem('userGoogleTokenId', JSON.stringify(res.tokenId));
    };

    const onFailure = (res) => {
        console.log('[Login failed] res:', res);
    };

    return (
        <div>
            <GoogleLogin
                clientId={clientId}
                buttonText="Login"
                onSuccess={onSuccess}
                onFailure={onFailure}
                cookiePolicy={'single_host_origin'}
                scope={['email', 'profile', 'https://www.googleapis.com/auth/drive', 'https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/presentations'].join(" ")}
                style={{marginTop: '100px'}}
                isSignedIn={true}
            />
        </div>
    );
}

export default Login;