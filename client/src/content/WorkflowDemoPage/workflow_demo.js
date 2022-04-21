import $ from 'jquery';
import Constants from '../../settings';

async function runWorkflow() {
  console.log('Running workflow demo...');
  var formData = new FormData();
  formData.append('user_id', JSON.parse(sessionStorage.getItem('googleObj')).id);
  var keywords = $('#keywords').val();
  formData.append('keywords', keywords);
  var tones = [];
  var positive = $('#tones').is(':checked');
  if (positive) {
    tones.push("Positive");
  }
  var negative = $('#tones1').is(':checked');
  if (negative) {
    tones.push("Negative");
  }
  formData.append('tones', tones.join(','));
  var date_start = $('#date_start').val();
  formData.append('date_start', date_start);
  var date_end = $('#date_end').val();
  formData.append('date_end', date_end);
  for (var pair of formData.entries()) {
    console.log(pair[0]+ ', ' + pair[1]); 
  }
  const queryString = new URLSearchParams(formData).toString();
  var url = new URL(Constants.API_DOMAIN+"/twitterapi/tweets?"+queryString);
  if (cookie.get('googleObj') === "") {
    alert("You have not signed in yet -- redirecting you to the login page");
    window.location.assign("./profile");
  } else {
    const response = await fetch(url, {
    method: 'GET',
    mode: Constants.CORS,
    headers: {
      'Access-Control-Allow-Origin':'*',
      'Content-type': 'application/json;charset=UTF-8',
      'Authorization': 'Bearer ' + JSON.parse(sessionStorage.getItem('googleObj')).code
    },
    });
    if (response.ok) {
      console.log(response.json().message);
    } else {
      console.log("Error: " + response.statusText);
    }    
  }
}

export async function runWorkflowDemo(){
  await runWorkflow();
};