const express = require('express');
const bodyParser = require('body-parser');
// const cookieParser = require('cookie-parser');
const cors = require('cors');
const router = require('./router/router.js');
const logger = require('./utilities/logger.js');
// const controller = require('./contoller/controller.js');

const app = express();

// app.use(cookieParser());
app.use(bodyParser.json());
app.use(cors);
app.use('/',router);
// app.use(logger);

const port = process.env.PORT || 3000;
app.listen(port, () => {
    console.log(`Server listening on port ${port}`);
})



