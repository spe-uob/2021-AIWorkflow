import React from 'react';
import {Button} from 'carbon-components-react';
import bgvideo from './bg-video.mp4'
import './LandingPage.css';


const LandingPage = () => {
  return (
    <div className="video-container">
     <video autoPlay loop muted>
      <source src={bgvideo} type="video/mp4"/>
     </video>
     <div className="caption">
        <h1>AI WORKFLOW INTEGRATION</h1>
        <Button>
          GET STARTED
        </Button>
      </div>
    </div>
  );
};

export default LandingPage;
