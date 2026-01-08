import os

# --- CONTEÚDO DA INDEX (HOME REVISADA) ---
CONTENT_INDEX_V3 = """---
import BaseLayout from '../layouts/BaseLayout.astro';
---

<BaseLayout title="Tecnologia com Propósito">
	<main class="relative min-h-screen">
		
		<section class="relative min-h-screen flex flex-col items-center justify-center px-6 overflow-hidden">
			<div class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[600px] h-[600px] bg-cyber-blue/5 blur-[140px] rounded-full pointer-events-none"></div>

			<div class="text-center z-10 space-y-10 max-w-4xl">
				<div class="inline-flex items-center gap-3 px-5 py-2 rounded-full border border-white/10 bg-white/5 text-slate-300 text-xs font-mono tracking-[0.2em] uppercase">
					<span class="w-1.5 h-1.5 rounded-full bg-emerald-500 animate-pulse"></span>
					Seja bem-vindo ao Comando de Operações
				</div>

				<h1 class="text-5xl md:text-7xl font-bold tracking-tighter text-white leading-[1.1] font-orbitron">
					INTELIGÊNCIA QUE <span class="text-cyber-blue">PROTEGE</span>,<br />
					ESTRATÉGIA QUE <span class="text-transparent bg-clip-text bg-gradient-to-r from-blue-400 to-indigo-500">ACOLHE</span>.
				</h1>

				<p class="max-w-3xl mx-auto text-slate-400 text-lg md:text-xl font-light leading-relaxed font-inter">
					Na <span class="text-white font-semibold">T.I. NA MENTE</span>, acreditamos que a tecnologia só cumpre seu papel quando traz tranquilidade. Nossa jornada é definida pela união entre a <strong>precisão da engenharia</strong> e o <strong>respeito institucional</strong>. Aqui, transformamos o complexo em seguro, e o vulnerável em resiliente.
				</p>

				<div class="flex flex-col sm:flex-row gap-5 justify-center pt-6">
					<a href="/servicos" class="group relative px-10 py-4 bg-white text-deep-space font-bold rounded-sm overflow-hidden transition-all hover:bg-cyber-blue hover:text-white">
						<span class="relative z-10 font-orbitron tracking-widest text-sm">VER NOSSAS SOLUÇÕES</span>
					</a>
					<a href="/sobre" class="px-10 py-4 border border-white/10 text-white font-bold rounded-sm hover:bg-white/5 transition-all font-orbitron tracking-widest text-sm">
						CONHEÇA NOSSO TIME
					</a>
				</div>
			</div>
		</section>

        <section class="py-24 border-t border-white/5 bg-black/20">
            <div class="max-w-7xl mx-auto px-6 grid md:grid-cols-3 gap-12 text-center">
                <div class="space-y-4">
                    <div class="text-cyber-blue text-4xl font-bold font-orbitron">01</div>
                    <h3 class="text-white font-bold tracking-wider">FOCO NO RESULTADO</h3>
                    <p class="text-slate-500 text-sm">Soluções pensadas para a continuidade e o crescimento do seu negócio.</p>
                </div>
                <div class="space-y-4">
                    <div class="text-cyber-blue text-4xl font-bold font-orbitron">02</div>
                    <h3 class="text-white font-bold tracking-wider">ENGENHARIA DE ELITE</h3>
                    <p class="text-slate-500 text-sm">Especialistas em Rust e Python construindo ferramentas seguras e escaláveis.</p>
                </div>
                <div class="space-y-4">
                    <div class="text-cyber-blue text-4xl font-bold font-orbitron">03</div>
                    <h3 class="text-white font-bold tracking-wider">MINDSET GRC</h3>
                    <p class="text-slate-500 text-sm">Governança e Riscos integrados nativamente em cada serviço prestado.</p>
                </div>
            </div>
        </section>
	</main>
</BaseLayout>
"""

# --- CONTEÚDO DA PÁGINA DE SERVIÇOS ---
CONTENT_SERVICES = """---
import BaseLayout from '../layouts/BaseLayout.astro';
import { getCollection } from 'astro:content';

const services = await getCollection('services');
const sortedServices = services.sort((a, b) => a.data.order - b.data.order);
---

<BaseLayout title="Capacidades e Serviços">
    <main class="max-w-7xl mx-auto px-6 py-32 mt-16">
        
        <header class="max-w-3xl mb-24 space-y-6">
            <div class="text-cyber-blue font-mono text-sm tracking-[0.4em] uppercase">Nosso Portfólio</div>
            <h1 class="text-5xl md:text-7xl font-bold text-white font-orbitron tracking-tighter uppercase">
                CAPACIDADES <br /><span class="text-slate-500 text-3xl md:text-5xl italic font-light">TÉCNICAS</span>
            </h1>
            <p class="text-slate-400 text-lg leading-relaxed border-l-2 border-cyber-blue/30 pl-8">
                Oferecemos uma abordagem multidisciplinar que remove o peso da gestão tecnológica dos seus ombros, permitindo que você foque no que realmente importa: seu negócio.
            </p>
        </header>

        <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
            {sortedServices.map(service => (
                <div class="group relative p-1 rounded-2xl bg-white/5 hover:bg-gradient-to-br hover:from-cyber-blue/20 hover:to-transparent transition-all duration-500">
                    <div class="bg-deep-space/80 backdrop-blur-md p-10 rounded-2xl h-full flex flex-col justify-between border border-white/5 group-hover:border-cyber-blue/20">
                        <div>
                            <div class="flex items-center justify-between mb-8">
                                <div class="p-3 bg-cyber-blue/10 rounded-lg text-cyber-blue border border-cyber-blue/20">
                                    <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m21 21-6-6m2-5a7 7 0 1 1-14 0 7 7 0 0 1 14 0Z"/></svg>
                                </div>
                                <span class="text-[10px] font-mono text-slate-500 tracking-widest uppercase">{service.data.category}</span>
                            </div>
                            
                            <h2 class="text-2xl font-bold text-white font-orbitron mb-4 group-hover:text-cyber-blue transition-colors uppercase tracking-tight">
                                {service.data.title}
                            </h2>
                            <p class="text-slate-400 leading-relaxed font-light mb-8">
                                {service.data.description}
                            </p>
                        </div>

                        <div class="flex items-center gap-2 text-xs font-bold text-cyber-blue font-orbitron opacity-0 group-hover:opacity-100 transition-opacity">
                            SAIBA MAIS <span>→</span>
                        </div>
                    </div>
                </div>
            ))}
        </div>

        <section class="mt-32 p-12 rounded-3xl bg-gradient-to-r from-blue-900/20 to-purple-900/20 border border-white/5 text-center space-y-8">
            <h3 class="text-3xl font-bold text-white font-orbitron uppercase tracking-widest">Vamos conversar sobre o seu futuro?</h3>
            <p class="text-slate-400 max-w-xl mx-auto">Nossos especialistas estão prontos para entender seu cenário e desenhar uma solução que traga segurança e valor real.</p>
            <a href="/contato" class="inline-block px-12 py-4 bg-white text-deep-space font-bold rounded-sm font-orbitron hover:scale-105 transition-transform tracking-widest text-sm">
                AGENDAR CONSULTORIA
            </a>
        </section>
    </main>
</BaseLayout>
"""

def main():
    print("🚀 Kortana aplicando ajustes de Identidade & Serviços...")
    
    # Atualiza Index
    with open("src/pages/index.astro", "w", encoding="utf-8") as f:
        f.write(CONTENT_INDEX_V3)
    print("✅ src/pages/index.astro atualizado (Humildade & Poder).")

    # Atualiza Serviços
    with open("src/pages/servicos.astro", "w", encoding="utf-8") as f:
        f.write(CONTENT_SERVICES)
    print("✅ src/pages/servicos.astro atualizado (Vitrine Técnica).")

    print("\n🏁 Vitrine atualizada com sucesso. Rode 'npm run dev' para conferir.")

if __name__ == "__main__":
    main()