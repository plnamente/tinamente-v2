import os

# --- 1. NAVEGAÇÃO REFINADA (Navigation.astro) ---
# Mudanças:
# - "T.I. NA MENTE": de font-bold para font-semibold (mais leve)
# - Espaçamento: Removido '-space-y-1' e adicionado 'mt-0.5' na tagline para um respiro sutil.
FILE_NAV_REFINED = """---
const navItems = [
    { name: 'Início', href: '/' },
    { name: 'Serviços', href: '/servicos' },
    { name: 'A Empresa', href: '/sobre' },
    { name: 'Contato', href: '/contato' },
];
---

<nav x-data="{ mobileMenuOpen: false }" class="fixed top-0 w-full z-50 border-b border-white/5 bg-[#020617]/90 backdrop-blur-md">
    <div class="max-w-7xl mx-auto px-6 h-20 flex items-center justify-between">
        
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

        <div class="hidden md:flex items-center gap-8">
            {navItems.map(item => (
                // Mudança aqui: font-semibold para os links também
                <a href={item.href} class="text-xs font-semibold text-slate-300 hover:text-white transition-colors uppercase tracking-widest font-jakarta relative after:absolute after:bottom-[-4px] after:left-0 after:h-[2px] after:w-0 after:bg-cyber-blue hover:after:w-full after:transition-all">
                    {item.name}
                </a>
            ))}
            <a href="/login" class="group relative px-5 py-2 border border-white/10 bg-white/5 text-white text-xs font-semibold rounded-sm overflow-hidden transition-all font-jakarta tracking-widest hover:border-cyber-blue/50">
                <span class="relative z-10 group-hover:text-cyber-blue transition-colors">ÁREA DO CLIENTE</span>
                <div class="absolute inset-0 bg-cyber-blue/10 translate-y-[100%] group-hover:translate-y-0 transition-transform duration-300"></div>
            </a>
        </div>

        <button @click="mobileMenuOpen = !mobileMenuOpen" class="md:hidden text-white p-2 hover:text-cyber-blue transition-colors">
            <svg x-show="!mobileMenuOpen" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="4" x2="20" y1="12" y2="12"/><line x1="4" x2="20" y1="6" y2="6"/><line x1="4" x2="20" y1="18" y2="18"/></svg>
            <svg x-show="mobileMenuOpen" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M18 6 6 18"/><path d="m6 6 12 12"/></svg>
        </button>
    </div>

    <div x-show="mobileMenuOpen" 
         x-transition:enter="transition ease-out duration-200"
         x-transition:enter-start="opacity-0 -translate-y-4"
         x-transition:enter-end="opacity-100 translate-y-0"
         @click.outside="mobileMenuOpen = false"
         class="md:hidden bg-[#020617] border-b border-white/10 px-6 py-8 space-y-4 shadow-2xl">
        {navItems.map(item => (
            // Mudança aqui: font-semibold no mobile
            <a href={item.href} class="block text-sm font-semibold font-jakarta text-white hover:text-cyber-blue tracking-widest uppercase border-l-2 border-transparent hover:border-cyber-blue pl-4 transition-all">
                {item.name}
            </a>
        ))}
        <div class="pt-4 border-t border-white/5 mt-6">
            <a href="/login" class="flex items-center justify-center gap-2 w-full py-4 bg-white/5 border border-white/10 text-white font-semibold font-jakarta tracking-widest text-xs hover:bg-cyber-blue/10 hover:border-cyber-blue/30 transition-all rounded-sm">
                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M15 3h4a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2h-4"/><polyline points="10 17 15 12 10 7"/><line x1="15" x2="3" y1="12" y2="12"/></svg>
                ACESSAR PORTAL
            </a>
        </div>
    </div>
</nav>
"""

# --- 2. HOME REFINADA (index.astro) ---
# Mudanças:
# - H1: de font-extrabold para font-bold (menos espesso, mais elegante)
FILE_INDEX_REFINED = """---
import BaseLayout from '../layouts/BaseLayout.astro';
---

<BaseLayout title="Engenharia de Confiança">
	<main class="relative min-h-screen">
		
		<section class="relative min-h-screen flex flex-col items-center justify-center px-6 overflow-hidden">
			<div class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[600px] h-[600px] bg-blue-500/5 blur-[140px] rounded-full pointer-events-none"></div>

			<div class="text-center z-10 space-y-10 max-w-4xl">
				<div class="inline-flex items-center gap-3 px-5 py-2 rounded-full border border-white/5 bg-white/5 text-slate-400 text-[10px] font-mono tracking-[0.3em] uppercase">
					<span class="w-1 h-1 rounded-full bg-cyber-blue shadow-[0_0_8px_#00d4ff]"></span>
					Núcleo de Operações Ativo
				</div>

                <h1 class="text-5xl md:text-7xl font-bold tracking-tight text-white leading-[1.1] font-jakarta">
					Inteligência que <span class="text-cyber-blue drop-shadow-[0_0_15px_rgba(0,212,255,0.2)]">protege</span>,<br />
					estratégia que <span class="text-slate-200">acolhe</span>.
				</h1>

				<p class="max-w-2xl mx-auto text-slate-400 text-lg md:text-xl font-light leading-relaxed">
					Na <span class="text-white font-medium">T.I. NA MENTE</span>, a tecnologia é o meio, mas a sua tranquilidade é o fim. Unimos precisão técnica e consultoria próxima para blindar o que é essencial para você.
				</p>

				<div class="flex flex-col sm:flex-row gap-5 justify-center pt-6">
					<a href="/servicos" class="px-10 py-4 bg-white text-deep-space font-semibold rounded hover:bg-cyber-blue hover:text-white transition-all font-jakarta tracking-wide text-sm">
						VER CAPACIDADES
					</a>
					<a href="/sobre" class="px-10 py-4 border border-white/10 text-white font-semibold rounded hover:bg-white/5 transition-all font-jakarta tracking-wide text-sm">
						NOSSA HISTÓRIA
					</a>
				</div>
			</div>
		</section>

        <section class="py-24 border-t border-white/5 bg-black/20">
            <div class="max-w-7xl mx-auto px-6 grid md:grid-cols-3 gap-12 text-center">
                <div class="space-y-4">
                    <div class="text-cyber-blue text-4xl font-bold font-jakarta">01</div>
                    <h3 class="text-white font-semibold tracking-wider font-jakarta">FOCO NO RESULTADO</h3>
                    <p class="text-slate-500 text-sm">Soluções pensadas para a continuidade e o crescimento do seu negócio.</p>
                </div>
                <div class="space-y-4">
                    <div class="text-cyber-blue text-4xl font-bold font-jakarta">02</div>
                    <h3 class="text-white font-semibold tracking-wider font-jakarta">ENGENHARIA DE ELITE</h3>
                    <p class="text-slate-500 text-sm">Especialistas em Rust e Python construindo ferramentas seguras e escaláveis.</p>
                </div>
                <div class="space-y-4">
                    <div class="text-cyber-blue text-4xl font-bold font-jakarta">03</div>
                    <h3 class="text-white font-semibold tracking-wider font-jakarta">MINDSET GRC</h3>
                    <p class="text-slate-500 text-sm">Governança e Riscos integrados nativamente em cada serviço prestado.</p>
                </div>
            </div>
        </section>
	</main>
</BaseLayout>
"""

def main():
    root = os.getcwd()
    print("⚖️ Kortana aplicando refinamento de peso e espaçamento...")
    
    # Atualiza Navegação
    with open(os.path.join(root, "src/components/ui/Navigation.astro"), "w", encoding="utf-8") as f:
        f.write(FILE_NAV_REFINED)
    print("✅ NAVEGAÇÃO: Espaçamento da logo ajustado e peso da fonte reduzido.")

    # Atualiza Home
    with open(os.path.join(root, "src/pages/index.astro"), "w", encoding="utf-8") as f:
        f.write(FILE_INDEX_REFINED)
    print("✅ HOME: Título principal afinado para maior elegância.")

    print("\\n🏁 Ajustes finos aplicados. Verifique o resultado no navegador.")

if __name__ == "__main__":
    main()