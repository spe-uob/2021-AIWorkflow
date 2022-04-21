import React from 'react';
import {Button} from 'carbon-components-react';
import cookie from "json-cookie";
import bgvideo from './bg-video1.mp4'
import './LandingPage.css';
import CookieConsent from "react-cookie-consent"

// import bgpicture from "./background.jpeg"


const LandingPage = () => {
  console.log(cookie.get('googleObj'));
  return (
    <div className="background-container">
     <video autoPlay loop muted>
      <source src={bgvideo} type="video/mp4"/>
     </video>
     {/* <img src={bgpicture} alt="logo" /> */}
     <div className="caption">
        <h1 style={{fontWeight: "bold",fontSize:"50px"}}>
          AI WORKFLOW INTEGRATION
        </h1>
        <br/>
        
        <Button  onClick={()=>{
          if (cookie.get("googleObj") === "") {
            window.location.assign("./profile");
          } else {
            window.location.assign("/workflow");
          }}}>
          GET STARTED
        </Button>
        <CookieConsent location="bottom" cookieName="googleObj" expires={999} overlay>
            This website uses cookies to store login information. If you would like not to use cookies, don't login.
        </CookieConsent>
      </div>
    </div>
  );
};

export default LandingPage;
