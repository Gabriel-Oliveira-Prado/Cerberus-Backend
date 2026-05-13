const express = require('express');
const router = express.Router();
const dbController = require('../controllers/dbController');

router.post('/connect', dbController.connectToDb);

module.exports = router;
