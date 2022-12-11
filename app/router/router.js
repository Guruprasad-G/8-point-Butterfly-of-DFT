const express = require('express');
const routing = express.Router();
const controller = require('../controller/controller.js');

routing.get('/', controller.fetchanswer);

module.exports = routing;


