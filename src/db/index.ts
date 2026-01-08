import { drizzle } from 'drizzle-orm/postgres-js';
import postgres from 'postgres';
import * as schema from './schema';

const connectionString = import.meta.env.DATABASE_URL;

// Em build, não quebra se não houver banco, mas avisa
if (!connectionString && import.meta.env.MODE !== 'production') {
  console.warn('⚠️ DATABASE_URL não definida. O sistema funcionará em modo apenas visual.');
}

const client = postgres(connectionString || 'postgres://user:pass@localhost:5432/db');
export const db = drizzle(client, { schema });
