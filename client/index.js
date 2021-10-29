'use strict';

const express = require('express');
const request = require('request');

// Constants
const PORT = 8080;
const HOST = '0.0.0.0';

// App
const app = express();
app.get('/', (req, res) => {
  request('http://backend/hello_world', { json: true }, (err, response, body) => {
    if (err) { return console.log(err); }
      res.send(body.message);
    });
});

app.listen(PORT, HOST);
console.log(`Running on http://${HOST}:${PORT}`);