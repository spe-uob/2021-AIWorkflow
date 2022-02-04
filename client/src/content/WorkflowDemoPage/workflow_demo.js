import $ from 'jquery';

function runWorkflow() {
  console.log('Running workflow demo...');
  var formData = new FormData();
  formData.append('user_id', "demo");
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
  console.log(queryString);
  var url = new URL("http://localhost:5001/twitterapi/tweets?"+queryString);
  var googleObj = JSON.parse(sessionStorage.userGoogleTokenId);
  console.log(googleObj);
  var formResult;
  fetch(url, {
  method: 'GET',
  headers: {'Content-type': 'application/json;charset=UTF-8'}
  })
    .then(response => response.json())
    .then(data => formResult = data)
    .then(() => alert(formResult.message))
    .catch(error => alert(error));
}

export function runWorkflowDemo(){
  runWorkflow();
}