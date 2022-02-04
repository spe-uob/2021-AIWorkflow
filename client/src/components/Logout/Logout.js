import React from 'react';
import {GoogleLogout} from 'react-google-login'

const clientId = '516108771432-8r055agb6k336emqdqh242s4c73lduf7.apps.googleusercontent.com';

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