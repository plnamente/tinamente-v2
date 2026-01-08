import os

# --- 1. COMPONENTE DE NAVEGAÇÃO (Navigation.astro) ---
# Usando Alpine.js para o menu mobile ser ultra-leve
FILE_NAV_COMPONENT = """---
const navItems = [
    { name: 'Início', href: '/' },
    { name: 'Serviços', href: '/servicos' },
    { name: 'A Empresa', href: '/sobre' },
    { name: 'Contato', href: '/contato' },
];
---

<nav x-data="{ mobileMenuOpen: false }" class="fixed top-0 w-full z-50 border-b border-white/5 bg-deep-space/80 backdrop-blur-md">
    <div class="max-w-7xl mx-auto px-6 h-20 flex items-center justify-between">
        <a href="/" class="text-2xl font-bold text-white tracking-tighter font-orbitron group">
            T.I.<span class="text-cyber-blue group-hover:drop-shadow-[0_0_8px_#00d4ff] transition-all">NA</span>MENTE
        </a>

        <div class="hidden md:flex items-center gap-8">
            {navItems.map(item => (
                <a href={item.href} class="text-sm font-medium text-slate-400 hover:text-cyber-blue transition-colors uppercase tracking-widest font-orbitron">
                    {item.name}
                </a>
            ))}
            <a href="/login" class="px-5 py-2 border border-cyber-blue/30 text-cyber-blue text-xs font-bold rounded-sm hover:bg-cyber-blue hover:text-deep-space transition-all font-orbitron">
                ÁREA DO CLIENTE
            </a>
        </div>

        <button @click="mobileMenuOpen = !mobileMenuOpen" class="md:hidden text-white p-2">
            <svg x-show="!mobileMenuOpen" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="4" x2="20" y1="12" y2="12"/><line x1="4" x2="20" y1="6" y2="6"/><line x1="4" x2="20" y1="18" y2="18"/></svg>
            <svg x-show="mobileMenuOpen" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M18 6 6 18"/><path d="m6 6 12 12"/></svg>
        </button>
    </div>

    <div x-show="mobileMenuOpen" 
         x-transition:enter="transition ease-out duration-200"
         x-transition:enter-start="opacity-0 -translate-y-4"
         x-transition:enter-end="opacity-100 translate-y-0"
         class="md:hidden bg-deep-space border-b border-white/10 px-6 py-8 space-y-4 shadow-2xl">
        {navItems.map(item => (
            <a href={item.href} class="block text-lg font-orbitron text-white hover:text-cyber-blue tracking-widest uppercase">
                {item.name}
            </a>
        ))}
        <div class="pt-4 border-t border-white/5">
            <a href="/login" class="block w-full text-center py-4 bg-cyber-blue text-deep-space font-bold font-orbitron">
                ACESSAR PORTAL
            </a>
        </div>
    </div>
</nav>
"""

# --- 2. PÁGINA DE CONTATO (contato.astro) ---
FILE_PAGE_CONTACT = """---
import BaseLayout from '../layouts/BaseLayout.astro';
---

<BaseLayout title="Contato e Suporte">
    <main class="max-w-7xl mx-auto px-6 py-32 mt-10">
        
        <div class="grid lg:grid-cols-2 gap-20">
            <div class="space-y-12">
                <header class="space-y-4">
                    <div class="text-cyber-blue font-mono text-xs tracking-[0.5em] uppercase">Status: Pronta para Escuta</div>
                    <h1 class="text-5xl md:text-7xl font-bold text-white font-orbitron tracking-tighter uppercase">CONTATO</h1>
                    <p class="text-slate-400 text-lg leading-relaxed max-w-md">
                        Precisa de uma auditoria, consultoria ou suporte técnico de elite? Nossa central está operacional.
                    </p>
                </header>

                <div class="space-y-8">
                    <div class="flex gap-6 items-start">
                        <div class="w-12 h-12 bg-white/5 border border-white/10 rounded-lg flex items-center justify-center text-cyber-blue shrink-0">
                            <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect width="20" height="16" x="2" y="4" rx="2"/><path d="m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7"/></svg>
                        </div>
                        <div>
                            <h4 class="text-white font-orbitron text-sm tracking-widest mb-1 uppercase">Comunicação Digital</h4>
                            <p class="text-slate-500 font-mono text-sm">contato@tinamente.com.br</p>
                        </div>
                    </div>

                    <div class="flex gap-6 items-start">
                        <div class="w-12 h-12 bg-white/5 border border-white/10 rounded-lg flex items-center justify-center text-cyber-blue shrink-0">
                            <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/></svg>
                        </div>
                        <div>
                            <h4 class="text-white font-orbitron text-sm tracking-widest mb-1 uppercase">Linha Direta</h4>
                            <p class="text-slate-500 font-mono text-sm">(XX) XXXXX-XXXX</p>
                        </div>
                    </div>
                </div>

                <div class="relative h-64 rounded-2xl border border-white/5 bg-black overflow-hidden group">
                    <div class="absolute inset-0 opacity-40 grayscale group-hover:grayscale-0 transition-all duration-700">
                        <img src="https://images.unsplash.com/photo-1526778548025-fa2f459cd5c1?auto=format&fit=crop&q=80&w=1000" alt="Map Overlay" class="w-full h-full object-cover">
                    </div>
                    <div class="absolute inset-0 bg-gradient-to-t from-deep-space via-transparent to-transparent"></div>
                    <div class="absolute bottom-6 left-6">
                        <span class="px-3 py-1 bg-cyber-blue text-deep-space text-[10px] font-bold font-orbitron rounded">MATRIZ_OPERACIONAL</span>
                        <p class="text-white text-xs mt-2 font-mono">São Paulo, BR - HQ Virtual</p>
                    </div>
                </div>
            </div>

            <div class="relative group">
                <div class="absolute -inset-1 bg-gradient-to-r from-cyber-blue to-purple-600 rounded-2xl blur opacity-10 group-hover:opacity-20 transition duration-1000"></div>
                <div class="relative p-10 bg-deep-space/50 border border-white/10 rounded-2xl backdrop-blur-xl">
                    <form class="space-y-8">
                        <div class="grid md:grid-cols-2 gap-6">
                            <div class="space-y-2">
                                <label class="text-[10px] font-mono text-cyber-blue uppercase tracking-widest">Identificação</label>
                                <input type="text" placeholder="Nome Completo" class="w-full bg-black/40 border border-white/10 rounded px-4 py-3 text-white focus:border-cyber-blue outline-none transition-all">
                            </div>
                            <div class="space-y-2">
                                <label class="text-[10px] font-mono text-cyber-blue uppercase tracking-widest">Canal de Retorno</label>
                                <input type="email" placeholder="email@empresa.com" class="w-full bg-black/40 border border-white/10 rounded px-4 py-3 text-white focus:border-cyber-blue outline-none transition-all">
                            </div>
                        </div>
                        <div class="space-y-2">
                            <label class="text-[10px] font-mono text-cyber-blue uppercase tracking-widest">Assunto Estratégico</label>
                            <select class="w-full bg-black/40 border border-white/10 rounded px-4 py-3 text-white focus:border-cyber-blue outline-none transition-all appearance-none">
                                <option>Consultoria GRC / CIS v8</option>
                                <option>Implementação SOC / FIM</option>
                                <option>Engenharia DevSecOps (Rust)</option>
                                <option>Gestão ITIL 4</option>
                                <option>Outros Assuntos</option>
                            </select>
                        </div>
                        <div class="space-y-2">
                            <label class="text-[10px] font-mono text-cyber-blue uppercase tracking-widest">Briefing da Demanda</label>
                            <textarea rows="4" placeholder="Descreva brevemente como podemos acolher sua necessidade técnica..." class="w-full bg-black/40 border border-white/10 rounded px-4 py-3 text-white focus:border-cyber-blue outline-none transition-all"></textarea>
                        </div>
                        <button class="w-full py-4 bg-white text-deep-space font-bold font-orbitron tracking-widest hover:bg-cyber-blue hover:text-white transition-all shadow-[0_0_20px_rgba(255,255,255,0.1)]">
                            ENVIAR SOLICITAÇÃO
                        </button>
                    </form>
                </div>
            </div>
        </div>
    </main>
</BaseLayout>
"""

# --- 3. ATUALIZAÇÃO DO LAYOUT BASE (BaseLayout.astro) ---
FILE_BASE_LAYOUT_UPDATED = """---
import '../styles/global.css';
import Navigation from '../components/ui/Navigation.astro';

interface Props {
	title: string;
    description?: string;
}

const { title, description = "T.I. Na Mente - Inteligência que Protege. Estratégia que Acolhe." } = Astro.props;
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
        
        <script defer src="https://cdn.jsdelivr.net/npm/alpinejs@3.x.x/dist/cdn.min.js"></script>
	</head>
	<body class="overflow-x-hidden">
		<div class="fixed inset-0 z-[-1] pointer-events-none opacity-10 bg-[linear-gradient(to_right,#80808012_1px,transparent_1px),linear-gradient(to_bottom,#80808012_1px,transparent_1px)] bg-[size:24px_24px]"></div>
		
        <Navigation />

        <slot />
        
        <footer class="border-t border-white/5 py-20 mt-20 bg-black/40">
            <div class="max-w-7xl mx-auto px-6 grid md:grid-cols-3 gap-12">
                <div class="space-y-6">
                    <a href="/" class="text-2xl font-bold text-white font-orbitron tracking-tighter">T.I.<span class="text-cyber-blue">NA</span>MENTE</a>
                    <p class="text-slate-500 text-sm leading-relaxed">Referência em engenharia de segurança, governança ativa e consultoria estratégica de TI.</p>
                </div>
                <div class="space-y-6">
                    <h4 class="text-white font-orbitron text-xs tracking-widest uppercase">Navegação</h4>
                    <div class="flex flex-col gap-3 text-sm text-slate-400">
                        <a href="/servicos" class="hover:text-cyber-blue transition-colors">Capacidades</a>
                        <a href="/sobre" class="hover:text-cyber-blue transition-colors">A Empresa</a>
                        <a href="/contato" class="hover:text-cyber-blue transition-colors">Contato</a>
                    </div>
                </div>
                <div class="space-y-6 text-slate-500 text-xs font-mono">
                    <p>// PROTOCOLO_2.0_SOVEREIGN</p>
                    <p>// STATUS: OPERACIONAL</p>
                    <p>&copy; {new Date().getFullYear()} T.I. NA MENTE.</p>
                </div>
            </div>
        </footer>
	</body>
</html>
"""

def main():
    root = os.getcwd()
    print("🛠️ Kortana operacionalizando Navegação e Contato...")

    # Garante pasta de componentes
    os.makedirs(os.path.join(root, "src/components/ui"), exist_ok=True)

    # Escreve os arquivos
    with open(os.path.join(root, "src/components/ui/Navigation.astro"), "w", encoding="utf-8") as f:
        f.write(FILE_NAV_COMPONENT)
    
    with open(os.path.join(root, "src/layouts/BaseLayout.astro"), "w", encoding="utf-8") as f:
        f.write(FILE_BASE_LAYOUT_UPDATED)

    with open(os.path.join(root, "src/pages/contato.astro"), "w", encoding="utf-8") as f:
        f.write(FILE_PAGE_CONTACT)

    print("\\n✅ COMPONENTE: src/components/ui/Navigation.astro (Menu Alpine.js)")
    print("✅ LAYOUT: src/layouts/BaseLayout.astro (Integrado)")
    print("✅ PÁGINA: src/pages/contato.astro (Formulário & Mapa)")
    
    print("\\n🏁 Missão Concluída. Todas as páginas agora estão conectadas e responsivas!")

if __name__ == "__main__":
    main()