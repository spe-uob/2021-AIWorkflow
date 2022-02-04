import React from 'react';
import {GoogleLogout} from 'react-google-login'

const clientId = 'YOUR_CLIENT_ID.apps.googleusercontent.com';

function Logout() {
    const onSuccess = () => {
        alert('You have logged out.')
    };

    return (
        <div>
            <GoogleLogout
                clientId={clientId}
                buttonText="Logout"
                onLogoutSuccess={onSuccess}
            ></GoogleLogout>
        </div>
    );
}

export default Logout