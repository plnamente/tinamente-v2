import os

# --- 1. CONFIGURAÇÃO DE CONTEÚDO (Moved to top to avoid NameError) ---
FILE_CONTENT_CONFIG = """import { defineCollection, z } from 'astro:content';

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
"""

# --- 2. NAVEGAÇÃO ATUALIZADA (Navigation.astro) ---
FILE_NAV = """---
const navItems = [
    { name: 'Início', href: '/' },
    { name: 'Serviços', href: '/servicos' },
    { name: 'A Empresa', href: '/sobre' },
    { name: 'Blog', href: '/blog' }, // Blog é público
    { name: 'Contato', href: '/contato' },
];
---

<nav x-data="{ mobileMenuOpen: false }" class="fixed top-0 w-full z-50 border-b border-white/5 bg-[#020617]/90 backdrop-blur-md transition-all duration-300">
    <div class="max-w-7xl mx-auto px-6 h-20 flex items-center justify-between">
        
        <!-- LOGO -->
        <a href="/" class="flex items-center gap-3 group transition-all">
            <div class="relative w-10 h-10">
                <div class="absolute -inset-2 bg-cyber-blue rounded-full opacity-0 blur-md group-hover:opacity-30 transition-opacity duration-500"></div>
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" class="w-10 h-10 text-cyber-blue relative z-10">
                    <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10Z" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" class="drop-shadow-[0_0_5px_rgba(0,212,255,0.5)]"/>
                    <path d="M12 8a2 2 0 1 0 0-4 2 2 0 0 0 0 4Z" fill="currentColor" class="animate-pulse"/>
                    <path d="M12 16a2 2 0 1 0 0-4 2 2 0 0 0 0 4Z" fill="currentColor"/>
                    <path d="M7 11a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Z" fill="currentColor" opacity="0.8"/>
                    <path d="M17 11a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Z" fill="currentColor" opacity="0.8"/>
                    <path d="M12 8v4M12 16v2M7 11l5-3l5 3" stroke="currentColor" stroke-width="1" stroke-linecap="round" opacity="0.6"/>
                </svg>
            </div>
            
            <div class="flex flex-col">
                <span class="text-lg font-semibold text-white tracking-tighter font-jakarta leading-none group-hover:text-cyber-blue transition-colors">T.I.NA MENTE</span>
                <span class="text-[9px] text-cyber-blue font-mono uppercase tracking-widest leading-none opacity-70 group-hover:opacity-100 transition-opacity mt-0.5">Intelligence & Defense</span>
            </div>
        </a>

        <!-- Desktop Menu -->
        <div class="hidden md:flex items-center gap-8">
            {navItems.map(item => (
                <a href={item.href} class="text-xs font-semibold text-slate-300 hover:text-white transition-colors uppercase tracking-widest font-jakarta relative after:absolute after:bottom-[-4px] after:left-0 after:h-[2px] after:w-0 after:bg-cyber-blue hover:after:w-full after:transition-all">
                    {item.name}
                </a>
            ))}
            <!-- Botão de Acesso Membro -->
            <a href="/login" class="group relative px-5 py-2 border border-white/10 bg-white/5 text-white text-xs font-semibold rounded-sm overflow-hidden transition-all font-jakarta tracking-widest hover:border-cyber-blue/50">
                <span class="relative z-10 group-hover:text-cyber-blue transition-colors flex items-center gap-2">
                    <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M19 21v-2a4 4 0 0 0-4-4H9a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/></svg>
                    ÁREA DO CLIENTE
                </span>
                <div class="absolute inset-0 bg-cyber-blue/10 translate-y-[100%] group-hover:translate-y-0 transition-transform duration-300"></div>
            </a>
        </div>

        <!-- Mobile Toggle -->
        <button @click="mobileMenuOpen = !mobileMenuOpen" class="md:hidden text-white p-2 hover:text-cyber-blue transition-colors">
            <svg x-show="!mobileMenuOpen" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="4" x2="20" y1="12" y2="12"/><line x1="4" x2="20" y1="6" y2="6"/><line x1="4" x2="20" y1="18" y2="18"/></svg>
            <svg x-show="mobileMenuOpen" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M18 6 6 18"/><path d="m6 6 12 12"/></svg>
        </button>
    </div>

    <!-- Mobile Menu -->
    <div x-show="mobileMenuOpen" 
         x-transition:enter="transition ease-out duration-200"
         x-transition:enter-start="opacity-0 -translate-y-4"
         x-transition:enter-end="opacity-100 translate-y-0"
         @click.outside="mobileMenuOpen = false"
         class="md:hidden bg-[#020617] border-b border-white/10 px-6 py-8 space-y-4 shadow-2xl absolute w-full left-0 top-20">
        {navItems.map(item => (
            <a href={item.href} class="block text-sm font-semibold font-jakarta text-white hover:text-cyber-blue tracking-widest uppercase border-l-2 border-transparent hover:border-cyber-blue pl-4 transition-all py-2">
                {item.name}
            </a>
        ))}
        <div class="pt-6 border-t border-white/5 mt-4">
            <a href="/login" class="flex items-center justify-center gap-2 w-full py-4 bg-cyber-blue text-deep-space font-bold font-jakarta tracking-widest text-xs hover:bg-white transition-all rounded-sm">
                ACESSAR ÁREA DO CLIENTE
            </a>
        </div>
    </div>
</nav>
"""

# --- 3. BLOG PÚBLICO APRIMORADO (pages/blog/index.astro) ---
FILE_BLOG_INDEX = """---
import BaseLayout from '../../layouts/BaseLayout.astro';
import { getCollection } from 'astro:content';

const posts = (await getCollection('blog')).sort(
	(a, b) => b.data.pubDate.valueOf() - a.data.pubDate.valueOf()
);

const tags = [...new Set(posts.flatMap(post => post.data.tags))];
---

<BaseLayout title="Blog & Insights">
    <main class="max-w-7xl mx-auto px-6 py-32 mt-10">
        <header class="mb-20 text-center md:text-left relative">
            <!-- Background Glow -->
            <div class="absolute -top-20 -left-20 w-64 h-64 bg-cyber-blue/10 blur-[100px] rounded-full pointer-events-none"></div>
            
            <div class="relative z-10">
                <div class="text-cyber-blue font-mono text-xs tracking-[0.5em] uppercase mb-4 font-bold">Inteligência Pública</div>
                <h1 class="text-5xl md:text-7xl font-bold text-white font-jakarta tracking-tighter uppercase mb-6">
                    BLOG & <span class="text-transparent bg-clip-text bg-gradient-to-r from-cyber-blue to-purple-500">INSIGHTS</span>
                </h1>
                <p class="text-slate-400 max-w-2xl text-lg font-light leading-relaxed">
                    Análises de mercado, tendências de cibersegurança e novidades da T.I. NA MENTE. 
                    <span class="block mt-6 text-white font-medium italic p-4 border-l-2 border-cyber-blue bg-white/[0.02] rounded-r-lg">
                        "What if: E se, alguém lhe desse uma mão para que você pudesse implementar seus frameworks de forma mais fácil, como seria? quer saber? <a href="/login" class="text-cyber-blue hover:underline decoration-1 underline-offset-4">venha para area de membros</a>."
                    </span>
                </p>
            </div>
        </header>

        <!-- Filtro de Tags (Visual) -->
        <div class="flex flex-wrap gap-2 mb-12">
            <span class="px-4 py-1 bg-white text-deep-space text-xs font-bold rounded-full cursor-pointer hover:opacity-90">Todos</span>
            {tags.map(tag => (
                <span class="px-4 py-1 border border-white/10 text-slate-400 text-xs font-medium rounded-full cursor-pointer hover:border-cyber-blue hover:text-cyber-blue transition-all">
                    {tag}
                </span>
            ))}
        </div>

        <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
            {posts.map(post => (
                <a href={`/blog/${post.slug}`} class="group relative p-1 rounded-2xl bg-gradient-to-br from-white/10 to-transparent hover:from-cyber-blue/50 hover:to-purple-500/50 transition-all duration-500 h-full">
                    <div class="bg-deep-space p-6 rounded-[14px] h-full flex flex-col justify-between relative overflow-hidden">
                        <!-- Scanline Effect -->
                        <div class="absolute inset-0 bg-gradient-to-b from-transparent via-white/5 to-transparent translate-y-[-100%] group-hover:translate-y-[100%] transition-transform duration-700 pointer-events-none"></div>

                        <div>
                            <div class="flex gap-2 mb-4 flex-wrap">
                                {post.data.tags.slice(0, 2).map(tag => (
                                    <span class="text-[10px] font-mono px-2 py-1 bg-white/5 text-cyber-blue rounded border border-cyber-blue/20 uppercase tracking-wider">{tag}</span>
                                ))}
                            </div>
                            <h2 class="text-xl font-bold text-white font-jakarta mb-3 group-hover:text-cyber-blue transition-colors leading-tight">{post.data.title}</h2>
                            <p class="text-slate-500 text-sm leading-relaxed line-clamp-3 mb-6">{post.data.description}</p>
                        </div>
                        
                        <div class="flex items-center justify-between border-t border-white/5 pt-4 mt-auto">
                            <div class="flex items-center gap-2">
                                <div class="w-6 h-6 rounded-full bg-gradient-to-tr from-cyber-blue to-purple-500"></div>
                                <span class="text-[10px] font-mono text-slate-400 uppercase">{post.data.author}</span>
                            </div>
                            <span class="text-[10px] font-mono text-slate-500">{post.data.pubDate.toLocaleDateString('pt-PT')}</span>
                        </div>
                    </div>
                </a>
            ))}
        </div>
    </main>
</BaseLayout>
"""

# --- 3. PÁGINA DO POST (Com link para o Café) ---
FILE_BLOG_POST = """---
import BaseLayout from '../../layouts/BaseLayout.astro';
import { getCollection } from 'astro:content';

export async function getStaticPaths() {
	const posts = await getCollection('blog');
	return posts.map(post => ({
		params: { slug: post.slug },
		props: { post },
	}));
}

const { post } = Astro.props;
const { Content } = await post.render();
---

<BaseLayout title={post.data.title}>
    <!-- Progress Bar de Leitura -->
    <div class="fixed top-20 left-0 h-1 bg-cyber-blue w-0 z-40" id="reading-progress"></div>

    <main class="max-w-4xl mx-auto px-6 py-32 mt-10">
        <article class="prose prose-invert prose-lg max-w-none prose-headings:font-jakarta prose-headings:font-bold prose-a:text-cyber-blue hover:prose-a:text-white prose-strong:text-white">
            <header class="mb-16 not-prose border-b border-white/10 pb-10">
                <div class="flex gap-3 mb-6">
                    {post.data.tags.map(tag => <span class="px-3 py-1 border border-white/10 rounded-full text-xs font-mono text-cyber-blue uppercase tracking-wider">{tag}</span>)}
                </div>
                <h1 class="text-4xl md:text-6xl font-extrabold text-white font-jakarta mb-6 tracking-tight leading-tight">{post.data.title}</h1>
                <div class="flex items-center gap-4 text-sm text-slate-400 font-mono">
                    <span>// {post.data.author}</span>
                    <span>// {post.data.pubDate.toLocaleDateString('pt-PT')}</span>
                    <span>// 5 MIN READ</span>
                </div>
            </header>
            
            <div class="text-slate-300 leading-relaxed font-light">
                <Content />
            </div>
        </article>
        
        <!-- CTA: Fórum Café com seu Byte -->
        <div class="mt-20 relative overflow-hidden rounded-2xl border border-purple-500/30 bg-purple-900/10 p-10 text-center">
            <div class="absolute inset-0 bg-[url('https://www.transparenttextures.com/patterns/carbon-fibre.png')] opacity-10"></div>
            <div class="relative z-10">
                <div class="inline-flex p-3 rounded-full bg-purple-500/20 text-purple-400 mb-6">
                    <svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/></svg>
                </div>
                <h3 class="text-2xl font-bold text-white font-jakarta mb-3">Este assunto continua no Café com seu Byte ☕</h3>
                <p class="text-slate-300 max-w-lg mx-auto mb-8">Dúvidas? Discordâncias? Insights? A discussão técnica de alto nível acontece na nossa área exclusiva para membros.</p>
                
                <div class="flex flex-col sm:flex-row justify-center gap-4">
                    <a href="/dashboard/cafe" class="px-8 py-3 bg-purple-600 hover:bg-purple-500 text-white font-bold rounded-sm font-orbitron text-sm tracking-widest transition-all shadow-lg shadow-purple-900/50">
                        ACESSAR FÓRUM
                    </a>
                    <a href="/login" class="px-8 py-3 border border-white/20 text-white hover:bg-white/5 font-bold rounded-sm font-orbitron text-sm tracking-widest transition-all">
                        CRIAR CONTA GRÁTIS
                    </a>
                </div>
            </div>
        </div>

        <div class="mt-12 pt-8 border-t border-white/5 flex justify-between">
            <a href="/blog" class="text-slate-500 hover:text-white text-xs font-bold font-jakarta tracking-widest uppercase transition-colors">← Voltar ao Blog</a>
        </div>
    </main>

    <script>
        // Script simples para barra de progresso de leitura
        window.onscroll = function() {
            let winScroll = document.body.scrollTop || document.documentElement.scrollTop;
            let height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
            let scrolled = (winScroll / height) * 100;
            document.getElementById("reading-progress").style.width = scrolled + "%";
        };
    </script>
</BaseLayout>
"""

# --- 4. CENTRAL DE INTELIGÊNCIA (dashboard/knowledge.astro) ---
# Agora dentro da área logada, com ar de biblioteca premium
FILE_DASHBOARD_KNOWLEDGE = """---
import DashboardLayout from '../../layouts/DashboardLayout.astro';

const categories = [
    { name: "Frameworks Oficiais", icon: "shield" },
    { name: "Apostilas de Treinamento", icon: "book" },
    { name: "Relatórios de Ameaças", icon: "alert" }
];

const documents = [
    { title: "Apostila FIM Vol. 1 - Fundamentos", category: "Apostilas de Treinamento", size: "2.4 MB", type: "PDF", locked: false },
    { title: "Apostila FIM Vol. 2 - Resposta", category: "Apostilas de Treinamento", size: "3.1 MB", type: "PDF", locked: false },
    { title: "CIS Controls v8 - Implementation Guide", category: "Frameworks Oficiais", size: "5.0 MB", type: "PDF", locked: false },
    { title: "ITIL 4 Strategic Leader Handbook", category: "Frameworks Oficiais", size: "12 MB", type: "PDF", locked: false },
    { title: "Relatório de Ameaças Q1 2026", category: "Relatórios de Ameaças", size: "1.2 MB", type: "PDF", locked: true }, // Exemplo de conteúdo bloqueado
];
---

<DashboardLayout title="Central de Inteligência">
    <div class="max-w-6xl mx-auto space-y-10">
        
        <header class="flex flex-col md:flex-row justify-between items-end gap-6 border-b border-white/10 pb-8">
            <div class="space-y-3">
                <div class="text-cyber-blue font-mono text-xs tracking-[0.3em] uppercase">Acervo Técnico</div>
                <h1 class="text-4xl font-bold text-white font-jakarta">Central de <span class="text-cyber-blue">Inteligência</span></h1>
                <p class="text-slate-400 max-w-xl">Acesse nossa biblioteca de frameworks, guias de implementação e inteligência de ameaças.</p>
            </div>
            
            <!-- Barra de Pesquisa -->
            <div class="relative w-full md:w-64">
                <input type="text" placeholder="Buscar documento..." class="w-full bg-black/40 border border-white/10 rounded px-4 py-2 text-sm text-white focus:border-cyber-blue outline-none transition-all pl-10">
                <svg class="w-4 h-4 text-slate-500 absolute left-3 top-2.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"></path></svg>
            </div>
        </header>

        <!-- Filtros de Categoria -->
        <div class="flex gap-4 overflow-x-auto pb-2">
            <button class="px-4 py-2 bg-cyber-blue text-deep-space font-bold rounded text-xs whitespace-nowrap">Todos</button>
            {categories.map(cat => (
                <button class="px-4 py-2 bg-white/5 border border-white/10 text-slate-300 font-medium rounded text-xs hover:bg-white/10 whitespace-nowrap transition-colors">{cat.name}</button>
            ))}
        </div>

        <!-- Grid de Documentos -->
        <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-6">
            {documents.map(doc => (
                <div class="group relative p-6 rounded-xl border border-white/10 bg-white/[0.02] hover:bg-white/[0.04] transition-all cursor-pointer overflow-hidden">
                    <!-- Status Indicator -->
                    <div class={`absolute top-0 right-0 p-3 rounded-bl-xl ${doc.locked ? 'bg-red-500/10 text-red-500' : 'bg-emerald-500/10 text-emerald-500'}`}>
                        {doc.locked ? 
                            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg> : 
                            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" x2="12" y1="15" y2="3"/></svg>
                        }
                    </div>

                    <div class="mb-6 pt-2">
                        <div class="w-12 h-12 rounded bg-white/5 flex items-center justify-center text-slate-300 mb-4 group-hover:scale-110 transition-transform duration-300">
                            <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M14.5 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V7.5L14.5 2z"/><polyline points="14 2 14 8 20 8"/><path d="M16 13H8"/><path d="M16 17H8"/><path d="M10 9H8"/></svg>
                        </div>
                        <div class="text-[10px] font-mono text-cyber-blue uppercase tracking-wider mb-2">{doc.category}</div>
                        <h3 class="text-white font-bold font-jakarta leading-tight group-hover:text-cyber-blue transition-colors">{doc.title}</h3>
                    </div>

                    <div class="flex items-center justify-between text-xs text-slate-500 border-t border-white/5 pt-4 mt-auto">
                        <span class="font-mono">{doc.type} • {doc.size}</span>
                        <span class="group-hover:translate-x-1 transition-transform text-white">Download →</span>
                    </div>
                </div>
            ))}
        </div>
    </div>
</DashboardLayout>
"""

# --- 5. CAFÉ COM SEU BYTE (dashboard/cafe.astro) ---
# Fórum Multimídia
FILE_DASHBOARD_CAFE = """---
import DashboardLayout from '../../layouts/DashboardLayout.astro';

const trendingTopics = [
    { title: "Implementando Rust em ambientes Legacy", author: "DevMaster", replies: 42, hot: true },
    { title: "Dúvidas sobre o Controle 3.4 do CIS v8", author: "SecOps_Junior", replies: 12, hot: false },
    { title: "Melhores práticas para backup imutável", author: "SysAdmin_BR", replies: 28, hot: true },
];

const videos = [
    { title: "Análise de Malware com IA", author: "Kortana Lab", duration: "12:40", views: "1.2k" },
    { title: "Tutorial: Configurando Firewall no Linux", author: "T.I. NA MENTE", duration: "08:15", views: "3.4k" },
];
---

<DashboardLayout title="Café com seu Byte">
    <div class="max-w-7xl mx-auto space-y-12">
        
        <!-- Header da Comunidade -->
        <header class="relative rounded-2xl overflow-hidden bg-gradient-to-r from-purple-900/40 to-blue-900/40 border border-white/10 p-10">
            <div class="absolute inset-0 bg-[url('https://www.transparenttextures.com/patterns/cubes.png')] opacity-10"></div>
            <div class="relative z-10 flex flex-col md:flex-row justify-between items-end gap-6">
                <div>
                    <h1 class="text-4xl md:text-5xl font-bold text-white font-jakarta mb-3">Café com seu <span class="text-transparent bg-clip-text bg-gradient-to-r from-purple-400 to-pink-400">Byte</span> ☕</h1>
                    <p class="text-slate-300 text-lg max-w-xl">O ponto de encontro da elite técnica. Debata, aprenda e compartilhe conhecimento sem filtros corporativos.</p>
                </div>
                <div class="flex gap-3">
                    <button class="px-6 py-3 bg-white/10 text-white font-bold rounded hover:bg-white/20 transition-all font-jakarta text-sm border border-white/10">MEUS TÓPICOS</button>
                    <button class="px-6 py-3 bg-purple-600 text-white font-bold rounded hover:bg-purple-500 transition-all font-jakarta text-sm shadow-lg shadow-purple-900/50">+ NOVO TÓPICO</button>
                </div>
            </div>
        </header>

        <div class="grid lg:grid-cols-3 gap-8">
            
            <!-- Coluna Principal: Feed de Vídeos (Shorts/Youtube style) -->
            <div class="lg:col-span-2 space-y-8">
                <div class="flex items-center justify-between">
                    <h2 class="text-xl font-bold text-white font-jakarta">Vídeos em Destaque</h2>
                    <a href="#" class="text-xs text-purple-400 hover:text-white transition-colors">Ver biblioteca completa</a>
                </div>

                <div class="grid md:grid-cols-2 gap-6">
                    {videos.map(video => (
                        <div class="group rounded-xl overflow-hidden bg-[#0a0a0a] border border-white/10 hover:border-purple-500/50 transition-all cursor-pointer">
                            <div class="aspect-video bg-white/5 relative group-hover:bg-white/10 transition-colors flex items-center justify-center">
                                <svg xmlns="http://www.w3.org/2000/svg" width="48" height="48" viewBox="0 0 24 24" fill="currentColor" class="text-white/50 group-hover:text-white group-hover:scale-110 transition-all"><path d="M10 15.172l9.192-9.193 1.415 1.414L10 18l-6.364-6.364 1.414-1.414z"/><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-2 14.5v-9l6 4.5-6 4.5z"/></svg>
                                <span class="absolute bottom-2 right-2 bg-black/80 text-white text-[10px] px-2 py-0.5 rounded font-mono">{video.duration}</span>
                            </div>
                            <div class="p-4">
                                <h3 class="text-white font-bold leading-tight mb-2 group-hover:text-purple-400 transition-colors">{video.title}</h3>
                                <div class="flex justify-between items-center text-[11px] text-slate-500">
                                    <span>{video.author}</span>
                                    <span>{video.views} visualizações</span>
                                </div>
                            </div>
                        </div>
                    ))}
                </div>

                <!-- Input Rápido -->
                <div class="p-6 rounded-xl border border-white/10 bg-white/[0.02] flex gap-4 items-start">
                    <div class="w-10 h-10 rounded-full bg-gradient-to-br from-cyber-blue to-purple-500 shrink-0"></div>
                    <div class="flex-1">
                        <textarea rows="2" placeholder="No que você está trabalhando hoje? Compartilhe com a comunidade..." class="w-full bg-black/30 border border-white/10 rounded-lg p-3 text-sm text-white focus:border-purple-500 outline-none transition-all resize-none"></textarea>
                        <div class="flex justify-end mt-2">
                            <button class="text-xs font-bold text-white bg-white/10 px-4 py-2 rounded hover:bg-purple-600 transition-colors">PUBLICAR</button>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Sidebar: Tópicos Recentes -->
            <div class="space-y-6">
                <div class="p-6 rounded-xl border border-white/10 bg-white/[0.02]">
                    <h3 class="text-sm font-bold text-slate-400 uppercase tracking-widest mb-6 border-b border-white/5 pb-2">Discussões Quentes 🔥</h3>
                    <div class="space-y-4">
                        {trendingTopics.map(topic => (
                            <div class="group cursor-pointer">
                                <h4 class="text-white font-medium text-sm mb-1 group-hover:text-purple-400 transition-colors line-clamp-2">{topic.title}</h4>
                                <div class="flex items-center gap-3 text-[10px] text-slate-500">
                                    <span class="flex items-center gap-1"><div class="w-2 h-2 rounded-full bg-slate-600"></div> {topic.author}</span>
                                    <span>{topic.replies} respostas</span>
                                </div>
                            </div>
                        ))}
                    </div>
                    <button class="w-full mt-6 py-2 border border-white/10 rounded text-xs text-slate-400 hover:text-white hover:bg-white/5 transition-all">Ver todas as discussões</button>
                </div>

                <!-- Widget Discord/Social -->
                <div class="p-6 rounded-xl bg-[#5865F2] text-white text-center">
                    <h3 class="font-bold text-lg mb-2">Comunidade em Tempo Real</h3>
                    <p class="text-xs opacity-80 mb-4">Junte-se ao nosso servidor para chat de voz e eventos ao vivo.</p>
                    <button class="px-4 py-2 bg-white text-[#5865F2] font-bold rounded text-xs hover:scale-105 transition-transform">CONECTAR AGORA</button>
                </div>
            </div>
        </div>
    </div>
</DashboardLayout>
"""

def write_file(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"✅ Criado/Atualizado: {path}")

def main():
    root = os.getcwd()
    print("🛠️ Finalizando Arquitetura de Conteúdo (Correção de Sintaxe)...")

    # Config (Garante que as coleções existem) - ESTA ORDEM É CRÍTICA
    with open(os.path.join(root, "src/content/config.ts"), "w", encoding="utf-8") as f:
        f.write(FILE_CONTENT_CONFIG)

    # Atualiza Navegação
    with open(os.path.join(root, "src/components/ui/Navigation.astro"), "w", encoding="utf-8") as f:
        f.write(FILE_NAV)

    # Cria Área de Blog Público
    write_file(os.path.join(root, "src/pages/blog/index.astro"), FILE_BLOG_INDEX)
    write_file(os.path.join(root, "src/pages/blog/[...slug].astro"), FILE_BLOG_POST)

    # Cria Módulos da Área de Membros
    write_file(os.path.join(root, "src/pages/dashboard/knowledge.astro"), FILE_DASHBOARD_KNOWLEDGE)
    write_file(os.path.join(root, "src/pages/dashboard/cafe.astro"), FILE_DASHBOARD_CAFE)

    print("\\n🏁 Conteúdo Organizado e Conectado (Sem erros de sintaxe).")
    print("👉 Blog Público (com CTA): /blog")
    print("👉 Área de Membros (Central de Inteligência): /dashboard/knowledge")
    print("👉 Área de Membros (Fórum Café): /dashboard/cafe")

if __name__ == "__main__":
    main()