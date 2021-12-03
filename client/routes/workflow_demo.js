var request = require('request');
var express = require('express');
var router = express.Router();

/* GET home page. */
router.get('/workflow_demo', function(req, res, next) {
  request('http://backend/hello_world', { json: true }, (err, response, body) => {
    if (err) { return console.log(err); }
      res.render('workflow_demo', {title: body.message});
    });
});

module.exports = router;
