const express = require('express');
const cors = require('cors');
const dbRoutes = require('./routes/dbRoutes');
const authRoutes = require('./routes/authRoutes');

const app = express();

app.use(cors());
app.use(express.json());

// Rotas
app.use('/api/db', dbRoutes);
app.use('/api/auth', authRoutes);

app.get('/', (req, res) => {
  res.send({ status: 'Cerberus Backend Running' });
});

module.exports = app;
