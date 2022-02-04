import React from 'react';
import {GoogleLogout} from 'react-google-login'

const clientId = '516108771432-3t5hh91jqmvhtrvgk9ef9uhkd4njhj3l.apps.googleusercontent.com';

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