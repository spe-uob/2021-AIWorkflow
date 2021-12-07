function runWorkflowDemo() {
  console.log('Running workflow demo...');
  var formData = $('form').serializeArray();
  var formResult;
  fetch('http://localhost:5001/twitterapi/tweets', {
  method: 'POST',
  body: formData,
  headers: {'Content-type': 'application/json;charset=UTF-8'}
  })
    .then(response => response.json()) 
    .then(data => formResult = data)
    .then(() => alert(formResult.message))
}