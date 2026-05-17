/* Conectar o banco de dados para manipulação dele */
const { Client } = require('pg');

exports.connectToDb = async (req, res) => {
  const { host, port, database, user, password } = req.body;

  if (!host || !port || !database || !user || !password) {
    return res.status(400).json({ error: 'Todos os campos são obrigatórios' });
  }

  const client = new Client({
    host,
    port,
    database,
    user,
    password,
    ssl: { rejectUnauthorized: false },
  });

  try {
    await client.connect();
    // Testar uma query simples para validar
    const result = await client.query('SELECT NOW()');
    await client.end();
    
    return res.status(200).json({ 
      success: true, 
      message: 'Conexão estabelecida com sucesso',
      time: result.rows[0].now 
    });
  } catch (error) {
    return res.status(500).json({ 
      success: false, 
      error: 'Falha ao conectar no banco de dados', 
      details: error.message 
    });
  }
};
