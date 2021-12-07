const userAction = async () => {
  const response = await fetch('http://localhost:5001/twitterapi/tweets');
  const myJson = await response.json(); //extract JSON from the http response
 
  alert('search status: ' + myJson.message);
}
  
