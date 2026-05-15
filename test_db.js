const { Client } = require('pg');

async function test() {
  const client = new Client({
    host: 'db.qhxxufljpqczfieleqie.supabase.co',
    port: 5432,
    database: 'postgres',
    user: 'postgres',
    password: 'cerberus@Base@365',
    ssl: { rejectUnauthorized: false },
  });

  try {
    await client.connect();
    const res = await client.query('SELECT NOW()');
    console.log('Success:', res.rows[0]);
    await client.end();
  } catch (err) {
    console.error('Error:', err.message);
  }
}

test();
