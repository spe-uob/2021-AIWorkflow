var request = require('request');
var express = require('express');
var router = express.Router();

/* GET home page. */
router.get('/workflow_demo', function(req, res) {
  res.render('workflow_demo', {});
});

module.exports = router;
