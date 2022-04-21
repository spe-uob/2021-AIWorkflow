import React from 'react';
import {Button} from 'carbon-components-react';
 import bgvideo from './bg-video1.mp4'
import './LandingPage.css';

// import bgpicture from "./background.jpeg"


const LandingPage = () => {
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
        
        <Button  onClick={()=>{window.location.href="./profile"}}>
          GET STARTED
        </Button>
       
      </div>
    </div>
  );
};

export default LandingPage;
