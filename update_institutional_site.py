import os

# --- CONTEÚDO DA INDEX (HOME) ---
CONTENT_INDEX = """---
import BaseLayout from '../layouts/BaseLayout.astro';
---

<BaseLayout title="Novo Amanhecer">
	<main class="relative min-h-screen">
		
		<section class="relative min-h-screen flex flex-col items-center justify-center px-6 overflow-hidden">
			<div class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[500px] h-[500px] bg-cyber-blue/10 blur-[120px] rounded-full pointer-events-none"></div>

			<div class="text-center z-10 space-y-8 max-w-4xl">
				<div class="inline-flex items-center gap-3 px-4 py-2 rounded-full border border-cyber-blue/20 bg-cyber-blue/5 text-cyber-blue text-xs font-mono tracking-[0.2em] uppercase animate-pulse-slow">
					<span class="w-1.5 h-1.5 rounded-full bg-cyber-blue shadow-[0_0_10px_#00d4ff]"></span>
					Protocolo de Autoridade Ativo
				</div>

				<h1 class="text-5xl md:text-8xl font-black tracking-tighter text-white leading-tight font-orbitron">
					SOBERANIA <br />
					<span class="text-transparent bg-clip-text bg-gradient-to-r from-cyber-blue via-blue-500 to-purple-600 drop-shadow-[0_0_20px_rgba(0,212,255,0.3)] font-orbitron">DIGITAL</span>
				</h1>

				<p class="max-w-3xl mx-auto text-slate-300 text-lg md:text-xl font-light leading-relaxed">
					Na <span class="text-white font-semibold uppercase tracking-widest">T.I. NA MENTE</span>, não apenas observamos o futuro; <span class="text-cyber-blue">nós o auditamos e protegemos</span>. 
					Nossa jornada é definida pela convergência entre a inteligência cibernética e a governança inabalável. 
					Somos o farol que guia instituições através da névoa das ameaças, transformando infraestruturas vulneráveis em <span class="text-white font-semibold underline decoration-cyber-blue/50 underline-offset-4">fortalezas resilientes</span>.
				</p>

				<div class="flex flex-col sm:flex-row gap-5 justify-center pt-8">
					<a href="/servicos" class="group relative px-10 py-4 bg-cyber-blue text-deep-space font-bold rounded-sm overflow-hidden transition-all hover:shadow-[0_0_30px_rgba(0,212,255,0.4)]">
						<span class="relative z-10 font-orbitron tracking-widest uppercase">Explorar Capacidades</span>
						<div class="absolute inset-0 bg-white/20 translate-x-[-100%] group-hover:translate-x-[100%] transition-transform duration-500"></div>
					</a>
					<a href="/sobre" class="px-10 py-4 border border-white/10 text-white font-bold rounded-sm hover:bg-white/5 transition-all font-orbitron uppercase tracking-widest text-sm">
						A Empresa
					</a>
				</div>
			</div>
		</section>

		<section class="py-24 bg-white/[0.01] border-y border-white/5 relative overflow-hidden">
			<div class="max-w-7xl mx-auto px-6 text-center">
				<h2 class="text-cyber-blue font-mono text-xs tracking-[0.4em] uppercase mb-8">Estratégia Central</h2>
				<blockquote class="text-2xl md:text-4xl font-light text-slate-300 italic max-w-4xl mx-auto leading-tight">
					"Nossa missão é a sua soberania digital. Fornecemos soluções sob medida, capacitando sua empresa a enfrentar os desafios de um mundo digital em constante evolução."
				</blockquote>
			</div>
		</section>

		<section class="py-32 max-w-7xl mx-auto px-6">
			<h2 class="text-center text-3xl font-bold font-orbitron text-white mb-16 uppercase tracking-widest">Nossa <span class="text-cyber-blue">Cultura</span> de Engenharia</h2>
			<div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">
				{[
					{ t: "Inovação", d: "Transformamos problemas complexos em soluções disruptivas." },
					{ t: "Comprometimento", d: "Excelência técnica em cada entrega do SOC ao GRC." },
					{ t: "Colaboração", d: "Diversidade de ideias focadas em resultados de elite." },
					{ t: "Integridade", d: "Altos padrões éticos e transparência total em dados." }
				].map(v => (
					<div class="p-8 border border-white/5 bg-black/40 hover:border-cyber-blue/30 transition-all rounded-lg group">
						<div class="w-10 h-1 bg-cyber-blue/30 mb-4 group-hover:w-full transition-all duration-500"></div>
						<h4 class="text-cyber-blue font-bold mb-2 uppercase text-sm tracking-widest">{v.t}</h4>
						<p class="text-slate-500 text-xs leading-relaxed uppercase font-mono">{v.d}</p>
					</div>
				))}
			</div>
		</section>

		<div class="py-10 border-t border-white/5 flex flex-wrap justify-center gap-8 md:gap-12 text-slate-500 text-[10px] font-mono opacity-50 uppercase tracking-widest">
			<div>STATUS: <span class="text-emerald-500 animate-pulse">ONLINE</span></div>
			<div>VER: <span class="text-white">2.0.1-SOVEREIGN</span></div>
			<div>REGION: <span class="text-white">SA-EAST-1</span></div>
			<div>PROTOCOL: <span class="text-white">HTTPS/3-QUIC</span></div>
		</div>
	</main>
</BaseLayout>
"""

# --- CONTEÚDO DA PÁGINA SOBRE (HISTÓRICO LEGADO) ---
CONTENT_SOBRE = """---
import BaseLayout from '../layouts/BaseLayout.astro';
---

<BaseLayout title="A Empresa" description="Conheça a história e os valores da T.I. NA MENTE.">
    <main class="max-w-7xl mx-auto px-6 py-24 relative mt-16">
        
        <div class="absolute top-0 right-0 w-96 h-96 bg-purple-600/5 blur-[120px] rounded-full pointer-events-none"></div>

        <section class="max-w-4xl mx-auto space-y-20">
            <div class="space-y-6">
                <h1 class="text-4xl md:text-6xl font-black text-white font-orbitron tracking-tighter">
                    NOSSA <span class="text-cyber-blue">JORNADA</span>
                </h1>
                <p class="text-slate-400 text-lg md:text-xl leading-relaxed">
                    Na <span class="text-white font-bold">T.I. NA MENTE</span>, nossa jornada é moldada pela paixão e compromisso inabalável com a excelência em soluções tecnológicas. Fundada com a visão de transformar ideias em realidade, nossa empresa é um farol de inovação e confiabilidade no cenário do mundo da tecnologia da informação.
                </p>
            </div>

            <div class="grid md:grid-cols-2 gap-12">
                <div class="p-8 rounded-xl border border-white/10 bg-white/[0.02] hover:bg-white/[0.04] transition-all">
                    <h2 class="text-cyber-blue font-bold font-orbitron mb-4 tracking-widest text-lg uppercase">Missão</h2>
                    <p class="text-slate-300 text-sm leading-relaxed">
                        Fornecer consultoria, suporte e propor soluções tecnológicas inovadoras, sob medida para nossos clientes, capacitando-os a enfrentar os desafios do mundo digital. Nossa equipe apaixonada e especializada se empenha em compreender as necessidades únicas de cada cliente, transformando ideias em realidade por meio de serviços de TI excepcionais.
                    </p>
                </div>
                <div class="p-8 rounded-xl border border-white/10 bg-white/[0.02] hover:bg-white/[0.04] transition-all">
                    <h2 class="text-purple-500 font-bold font-orbitron mb-4 tracking-widest text-lg uppercase">Visão</h2>
                    <p class="text-slate-300 text-sm leading-relaxed">
                        Ser reconhecida não só como a principal empresa de soluções tecnológicas, mas como uma referência em inovação, excelência e parceria. Buscamos constantemente expandir nossos horizontes, explorar novas fronteiras tecnológicas e liderar o caminho em um mundo em constante evolução, deixando uma marca significativa no cenário global.
                    </p>
                </div>
            </div>

            <div class="space-y-12">
                <h2 class="text-2xl font-bold font-orbitron text-white text-center tracking-widest">PRINCÍPIOS OPERACIONAIS</h2>
                <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                    {[
                        { t: "Inovação", d: "Abraçamos a mudança e a criatividade, buscando constantemente maneiras novas e melhores de resolver problemas e agregar valor aos nossos clientes." },
                        { t: "Comprometimento", d: "Somos comprometidos com a excelência em cada aspecto do nosso trabalho, desde o atendimento ao cliente até a entrega final de projetos." },
                        { t: "Colaboração", d: "Acreditamos no poder da colaboração, valorizando a diversidade de ideias e trabalhando em equipe para alcançar resultados excepcionais." },
                        { t: "Integridade", d: "Agimos com integridade em todas as interações, mantendo altos padrões éticos e construindo confiança duradoura." },
                        { t: "Aprendizado Contínuo", d: "Estamos sempre em busca de conhecimento e crescimento, mantendo-nos atualizados com as últimas tendências tecnológicas." },
                        { t: "Responsabilidade Social", d: "Reconhecemos nossa responsabilidade para com a sociedade e o meio ambiente. Buscamos impactar positivamente as comunidades em que atuamos." }
                    ].map(v => (
                        <div class="flex gap-4 p-6 border-l border-white/10 bg-white/[0.01]">
                            <div class="text-cyber-blue font-mono text-lg font-bold">//</div>
                            <div>
                                <h4 class="text-white font-bold mb-1 uppercase text-sm tracking-wider">{v.t}</h4>
                                <p class="text-slate-500 text-xs leading-relaxed">{v.d}</p>
                            </div>
                        </div>
                    ))}
                </div>
            </div>
        </section>
    </main>
</BaseLayout>
"""

def main():
    print("🚀 Kortana inicializando atualização do site institucional...")
    
    # Grava Index
    with open("src/pages/index.astro", "w", encoding="utf-8") as f:
        f.write(CONTENT_INDEX)
    print("✅ src/pages/index.astro atualizado (O Manifesto).")

    # Grava Sobre
    with open("src/pages/sobre.astro", "w", encoding="utf-8") as f:
        f.write(CONTENT_SOBRE)
    print("✅ src/pages/sobre.astro atualizado (Histórico & Valores).")

    print("\n🏁 Vitrine Institucional consolidada. Execute 'npm run dev' para conferir o resultado.")

if __name__ == "__main__":
    main()