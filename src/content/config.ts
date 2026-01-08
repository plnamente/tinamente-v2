import { defineCollection, z } from 'astro:content';

const services = defineCollection({
  type: 'content',
  schema: z.object({
    title: z.string(),
    description: z.string(),
    icon: z.string(),
    order: z.number(),
    category: z.enum(['Shield & Strike', 'Tactical Development', 'Core Operations']),
  }),
});

const blog = defineCollection({
  type: 'content',
  schema: z.object({
    title: z.string(),
    description: z.string(),
    pubDate: z.date(),
    author: z.string(),
    image: z.string().optional(),
    tags: z.array(z.string()),
  }),
});

// Definição para evitar warnings de coleções auto-geradas
const frameworks = defineCollection({
  type: 'data', 
  schema: z.object({
    id: z.string(),
    control: z.string(),
    title: z.string(),
    description: z.string(),
    asset_type: z.string().optional(),
  }).optional()
});

const docs = defineCollection({
    type: 'content',
    schema: z.any(), // Schema genérico para documentos futuros
});

export const collections = { services, blog, frameworks, docs };
