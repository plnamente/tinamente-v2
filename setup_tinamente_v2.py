import os
import sys

# --- CONTEÚDO DOS ARQUIVOS ---

# 1. CSS Global (Tailwind v4)
FILE_GLOBAL_CSS = """@import "tailwindcss";

@theme {
  /* Paleta Cyber-GRC */
  --color-cyber-blue: #00d4ff;
  --color-cyber-red: #ff0055;
  --color-deep-space: #020617;
  --color-glass: rgba(255, 255, 255, 0.03);
  --color-glass-border: rgba(255, 255, 255, 0.1);
  
  /* Tipografia */
  --font-orbitron: "Orbitron", sans-serif;
  --font-inter: "Inter", sans-serif;

  /* Animações */
  --animate-scan: scan 3s linear infinite;
  --animate-pulse-slow: pulse 4s cubic-bezier(0.4, 0, 0.6, 1) infinite;
}

@keyframes scan {
  0% { background-position: 0% 0%; }
  100% { background-position: 0% 100%; }
}

@layer base {
  body {
    @apply bg-deep-space text-slate-200 font-inter antialiased;
    background-image: 
      radial-gradient(circle at 50% -20%, #0ea5e920 0%, transparent 50%),
      radial-gradient(circle at 0% 0%, #020617 100%);
    background-attachment: fixed;
  }
  
  h1, h2, h3, h4, h5, h6 {
    @apply font-orbitron;
  }
}
"""

# 2. Configuração de Conteúdo (Collections)
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

const frameworks = defineCollection({
  type: 'data',
  schema: z.object({
    id: z.string(),
    control: z.string(),
    title: z.string(),
    description: z.string(),
    asset_type: z.string().optional(),
  })
});

export const collections = { services, frameworks };
"""

# 3. Layout Base
FILE_BASE_LAYOUT = """---
import '../styles/global.css';

interface Props {
	title: string;
    description?: string;
}

const { title, description = "T.I. Na Mente - Cyber-GRC e Governança Estratégica" } = Astro.props;
---

<!doctype html>
<html lang="pt-br" class="scroll-smooth">
	<head>
		<meta charset="UTF-8" />
		<meta name="viewport" content="width=device-width" />
		<link rel="icon" type="image/svg+xml" href="/favicon.svg" />
		<meta name="generator" content={Astro.generator} />
        <meta name="description" content={description} />
		<title>{title} | T.I. NA MENTE</title>
		
        <link rel="preconnect" href="https://fonts.googleapis.com">
		<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
		<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600&family=Orbitron:wght@400;700;900&display=swap" rel="stylesheet">
	</head>
	<body class="overflow-x-hidden">
        <div class="fixed inset-0 z-[-1] pointer-events-none opacity-10 bg-[linear-gradient(to_right,#80808012_1px,transparent_1px),linear-gradient(to_bottom,#80808012_1px,transparent_1px)] bg-[size:24px_24px]"></div>
		
        <nav class="fixed top-0 w-full z-50 border-b border-white/5 bg-deep-space/80 backdrop-blur-md">
            <div class="max-w-7xl mx-auto px-6 h-16 flex items-center justify-between">
                <a href="/" class="text-xl font-bold text-white tracking-widest">T.I.<span class="text-cyber-blue">NA</span>MENTE</a>
                <div class="flex gap-6 text-sm font-medium">
                    <a href="/servicos" class="hover:text-cyber-blue transition-colors">SERVIÇOS</a>
                    <a href="/dashboard" class="text-slate-500 hover:text-white transition-colors cursor-not-allowed" title="Em breve">ÁREA MEMBROS</a>
                </div>
            </div>
        </nav>

        <slot />
        
        <footer class="border-t border-white/5 py-10 mt-20 text-center text-slate-600 text-sm">
            <p>&copy; {new Date().getFullYear()} T.I. NA MENTE. Protocolo de Segurança Ativo.</p>
        </footer>
	</body>
</html>
"""

# 4. Página Home (Index)
FILE_PAGE_INDEX = """---
import BaseLayout from '../layouts/BaseLayout.astro';
---

<BaseLayout title="Novo Amanhecer">
	<main class="relative min-h-screen flex flex-col items-center justify-center px-6 pt-16">
		
		<div class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[500px] h-[500px] bg-cyber-blue/10 blur-[120px] rounded-full pointer-events-none"></div>

		<section class="text-center z-10 space-y-8 max-w-4xl">
			<div class="inline-flex items-center gap-3 px-4 py-2 rounded-full border border-cyber-blue/20 bg-cyber-blue/5 text-cyber-blue text-xs font-mono tracking-[0.2em] uppercase animate-pulse-slow">
				<span class="w-1.5 h-1.5 rounded-full bg-cyber-blue shadow-[0_0_10px_#00d4ff]"></span>
				Sistema Operacional
			</div>

			<h1 class="text-5xl md:text-8xl font-black tracking-tighter text-white leading-tight">
				BLINDAGEM <br />
				<span class="text-transparent bg-clip-text bg-gradient-to-r from-cyber-blue via-blue-500 to-purple-600 drop-shadow-[0_0_20px_rgba(0,212,255,0.3)]">ESTRATÉGICA</span>
			</h1>

			<p class="max-w-2xl mx-auto text-slate-400 text-lg md:text-xl font-light leading-relaxed">
				Unimos a inteligência do <strong>CIS v8</strong> com a robustez da engenharia <strong>Rust</strong>. 
				Não apenas resolvemos incidentes; nós redefinimos a postura de defesa da sua empresa.
			</p>

			<div class="flex flex-col sm:flex-row gap-5 justify-center pt-8">
				<a href="/servicos" class="group relative px-8 py-4 bg-cyber-blue text-deep-space font-bold rounded-sm overflow-hidden transition-all hover:shadow-[0_0_30px_rgba(0,212,255,0.4)]">
					<span class="relative z-10">EXPLORAR SOLUÇÕES</span>
					<div class="absolute inset-0 bg-white/20 translate-x-[-100%] group-hover:translate-x-[100%] transition-transform duration-500"></div>
				</a>
				<a href="https://github.com/plnamente" target="_blank" class="px-8 py-4 border border-white/10 text-white font-bold rounded-sm hover:bg-white/5 transition-all flex items-center justify-center gap-2">
					<svg class="w-5 h-5" fill="currentColor" viewBox="0 0 24 24" aria-hidden="true"><path fill-rule="evenodd" d="M12 2C6.477 2 2 6.484 2 12.017c0 4.425 2.865 8.18 6.839 9.504.5.092.682-.217.682-.483 0-.237-.008-.868-.013-1.703-2.782.605-3.369-1.343-3.369-1.343-.454-1.158-1.11-1.466-1.11-1.466-.908-.62.069-.608.069-.608 1.003.07 1.531 1.032 1.531 1.032.892 1.53 2.341 1.088 2.91.832.092-.647.35-1.088.636-1.338-2.22-.253-4.555-1.113-4.555-4.951 0-1.093.39-1.988 1.029-2.688-.103-.253-.446-1.272.098-2.65 0 0 .84-.27 2.75 1.026A9.564 9.564 0 0112 6.844c.85.004 1.705.115 2.504.337 1.909-1.296 2.747-1.027 2.747-1.027.546 1.379.202 2.398.1 2.651.64.7 1.028 1.595 1.028 2.688 0 3.848-2.339 4.695-4.566 4.943.359.309.678.92.678 1.855 0 1.338-.012 2.419-.012 2.747 0 .268.18.58.688.482A10.019 10.019 0 0022 12.017C22 6.484 17.522 2 12 2z" clip-rule="evenodd" /></svg>
					GITHUB
				</a>
			</div>
		</section>

        <div class="absolute bottom-10 left-0 w-full flex justify-center gap-12 text-slate-500 text-sm font-mono opacity-50">
            <div>STATUS: <span class="text-emerald-500">ONLINE</span></div>
            <div>VER: <span class="text-white">2.0.0-ALPHA</span></div>
            <div>REGION: <span class="text-white">SA-EAST-1</span></div>
        </div>
	</main>
</BaseLayout>
"""

# 5. Página de Serviços (Lista)
FILE_PAGE_SERVICES = """---
import BaseLayout from '../layouts/BaseLayout.astro';
import { getCollection } from 'astro:content';

const services = await getCollection('services');
const sortedServices = services.sort((a, b) => a.data.order - b.data.order);
---

<BaseLayout title="Serviços de Elite">
    <main class="max-w-7xl mx-auto px-6 py-32">
        <header class="mb-20">
            <h1 class="text-4xl md:text-6xl font-bold mb-6 text-white">NOSSAS <span class="text-cyber-blue">CAPACIDADES</span></h1>
            <p class="text-slate-400 text-lg max-w-2xl border-l-2 border-cyber-blue/30 pl-6">
                Abordagem multidisciplinar que integra Governança, Engenharia de Software e Operações de Segurança.
            </p>
        </header>

        <div class="grid md:grid-cols-2 gap-8">
            {sortedServices.map(service => (
                <article class="group relative p-8 rounded-xl border border-white/5 bg-white/[0.02] hover:bg-white/[0.04] transition-all overflow-hidden">
                    <div class="absolute top-0 left-0 w-full h-1 bg-gradient-to-r from-transparent via-cyber-blue to-transparent translate-x-[-100%] group-hover:translate-x-[100%] transition-transform duration-1000"></div>
                    
                    <div class="flex items-start justify-between mb-6">
                        <span class="text-xs font-mono text-cyber-blue border border-cyber-blue/20 px-2 py-1 rounded">
                            {service.data.category.toUpperCase()}
                        </span>
                        <div class="text-slate-500 group-hover:text-cyber-blue transition-colors">
                            <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10"/></svg>
                        </div>
                    </div>

                    <h2 class="text-2xl font-bold text-white mb-4 font-orbitron group-hover:text-cyber-blue transition-colors">
                        {service.data.title}
                    </h2>
                    
                    <p class="text-slate-400 leading-relaxed">
                        {service.data.description}
                    </p>

                    </article>
            ))}
        </div>
    </main>
</BaseLayout>
"""

# 6. Conteúdos Markdown (Serviços)
SERVICES_CONTENT = {
    "soc-24-7.md": """---
title: "Shield & Strike: SOC"
description: "Operações de Defesa Ativa. Monitoramento contínuo e resposta a incidentes baseada no framework FIM (CERT.br)."
icon: "shield"
order: 1
category: "Shield & Strike"
---
""",
    "consultoria-grc.md": """---
title: "Compliance Radar: GRC"
description: "Transformação de governança. Auditoria e implementação dos controles CIS v8, NIST e preparação para ISO 27001."
icon: "activity"
order: 2
category: "Shield & Strike"
---
""",
    "devsecops.md": """---
title: "Tactical Dev: DevSecOps"
description: "Engenharia de software segura com Rust. Ferramentas de CLI personalizadas e pipelines de CI/CD blindados."
icon: "code"
order: 3
category: "Tactical Development"
---
""",
    "gestao-itil.md": """---
title: "Core Ops: ITIL 4"
description: "Gestão estratégica de serviços. Alinhamento entre tecnologia e negócio para maximizar valor e estabilidade."
icon: "cpu"
order: 4
category: "Core Operations"
---
"""
}

# --- FUNÇÕES UTILITÁRIAS ---

def create_folder(path):
    if not os.path.exists(path):
        os.makedirs(path)
        print(f"📂 Criado: {path}")

def write_file(path, content):
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"✅ Gerado: {path}")

def main():
    root_dir = os.getcwd()
    print(f"🚀 Iniciando Setup 'Novo Amanhecer' em: {root_dir}")

    # 1. Estrutura de Pastas
    folders = [
        "src/components/ui",
        "src/components/grc",
        "src/content/services",
        "src/content/frameworks",
        "src/content/blog",
        "src/layouts",
        "src/pages",
        "src/styles",
        "src/lib",
        "public/assets"
    ]
    
    for folder in folders:
        create_folder(os.path.join(root_dir, folder))

    # 2. Arquivos de Configuração e Estilo
    write_file(os.path.join(root_dir, "src/styles/global.css"), FILE_GLOBAL_CSS)
    write_file(os.path.join(root_dir, "src/content/config.ts"), FILE_CONTENT_CONFIG)

    # 3. Layouts e Páginas
    write_file(os.path.join(root_dir, "src/layouts/BaseLayout.astro"), FILE_BASE_LAYOUT)
    write_file(os.path.join(root_dir, "src/pages/index.astro"), FILE_PAGE_INDEX)
    write_file(os.path.join(root_dir, "src/pages/servicos.astro"), FILE_PAGE_SERVICES)

    # 4. Gerar Conteúdo dos Serviços
    for filename, content in SERVICES_CONTENT.items():
        write_file(os.path.join(root_dir, "src/content/services", filename), content.strip())

    print("\n🏁 Missão Cumprida. A arquitetura está pronta.")
    print("👉 Execute 'npm run dev' para visualizar a nova T.I. NA MENTE.")

if __name__ == "__main__":
    main()