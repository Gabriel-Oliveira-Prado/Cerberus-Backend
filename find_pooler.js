const { Client } = require('pg');

const regions = ['sa-east-1', 'us-east-1', 'us-east-2', 'us-west-1', 'us-west-2', 'eu-central-1', 'eu-west-1'];

async function testPooler() {
  for (const region of regions) {
    const host = `aws-0-${region}.pooler.supabase.com`;
    console.log(`Testing ${host}...`);
    const client = new Client({
      host,
      port: 6543,
      database: 'postgres',
      user: 'postgres.qhxxufljpqczfieleqie',
      password: 'cerberus@Base@365',
      ssl: { rejectUnauthorized: false },
      connectionTimeoutMillis: 3000
    });

    try {
      await client.connect();
      console.log(`\n✅ SUCESSO! Encontrado na região: ${region}`);
      console.log(`Host: ${host}`);
      await client.end();
      return;
    } catch (err) {
      console.log(`Falhou: ${err.message}`);
    }
  }
}

testPooler();
