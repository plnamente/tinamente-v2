import { pgTable, serial, text, numeric, timestamp, jsonb } from 'drizzle-orm/pg-core';

// Tabela de Relatórios de Impacto (Calculadora)
export const impactReports = pgTable('impact_reports', {
  id: serial('id').primaryKey(),
  companyName: text('company_name').notNull(),
  annualRevenue: numeric('annual_revenue').notNull(),
  employees: numeric('employees').notNull(),
  downtimeHours: numeric('downtime_hours').notNull(),
  estimatedLoss: numeric('estimated_loss').notNull(), // O valor calculado
  sector: text('sector'), // Financeiro, Saúde, Varejo...
  createdAt: timestamp('created_at').defaultNow(),
  metadata: jsonb('metadata'), // Para guardar inputs extras
});

// Tabela de Leads (Quem gerou o relatório)
export const leads = pgTable('leads', {
  id: serial('id').primaryKey(),
  email: text('email').notNull().unique(),
  name: text('name'),
  role: text('role'),
  createdAt: timestamp('created_at').defaultNow(),
});
