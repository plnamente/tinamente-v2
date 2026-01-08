import os

CONTENT_SOBRE_UPDATED_V2 = """---
import BaseLayout from '../layouts/BaseLayout.astro';
---

<BaseLayout title="A Empresa" description="Conheça a jornada e o time de elite da T.I. NA MENTE.">
    <main class="max-w-7xl mx-auto px-6 py-24 relative mt-16">
        
        <div class="absolute top-0 right-0 w-96 h-96 bg-purple-600/5 blur-[120px] rounded-full pointer-events-none"></div>

        <section class="max-w-4xl mx-auto space-y-20">
            <div class="space-y-6">
                <h1 class="text-4xl md:text-6xl font-black text-white font-orbitron tracking-tighter uppercase">
                    NOSSA <span class="text-cyber-blue">JORNADA</span>
                </h1>
                <p class="text-slate-400 text-lg md:text-xl leading-relaxed">
                    Na <span class="text-white font-bold tracking-widest">T.I. NA MENTE</span>, nossa jornada é moldada pela paixão e compromisso inabalável com a excelência em soluções tecnológicas. Fundada com a visão de transformar ideias em realidade, somos um farol de inovação no cenário da TI.
                </p>
            </div>

            <div class="grid md:grid-cols-2 gap-8">
                <div class="p-8 rounded-xl border border-white/10 bg-white/[0.02] hover:bg-white/[0.04] transition-all">
                    <h2 class="text-cyber-blue font-bold font-orbitron mb-4 tracking-widest text-lg uppercase">Missão</h2>
                    <p class="text-slate-300 text-sm leading-relaxed">
                        Fornecer consultoria, suporte e soluções tecnológicas inovadoras, sob medida para nossos clientes, capacitando-os a enfrentar os desafios do mundo digital com inteligência e segurança.
                    </p>
                </div>
                <div class="p-8 rounded-xl border border-white/10 bg-white/[0.02] hover:bg-white/[0.04] transition-all">
                    <h2 class="text-purple-500 font-bold font-orbitron mb-4 tracking-widest text-lg uppercase">Visão</h2>
                    <p class="text-slate-300 text-sm leading-relaxed">
                        Ser a referência global em inovação e parceria estratégica, explorando novas fronteiras tecnológicas e liderando o caminho em um mundo em constante evolução.
                    </p>
                </div>
            </div>

            <div class="space-y-12">
                <h2 class="text-3xl font-bold font-orbitron text-white text-center tracking-[0.3em] uppercase">Comando <span class="text-cyber-blue">Técnico</span></h2>
                
                <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
                    <div class="p-1 rounded-2xl bg-gradient-to-b from-cyber-blue/30 to-transparent group hover:from-cyber-blue/50 transition-all">
                        <div class="bg-deep-space p-8 rounded-[calc(1rem-1px)] h-full space-y-6 relative overflow-hidden">
                            
                            <div class="absolute inset-0 bg-[linear-gradient(to_bottom,transparent,rgba(0,212,255,0.05),transparent)] bg-[length:100%_200%] animate-scan opacity-0 group-hover:opacity-100 transition-opacity pointer-events-none"></div>

                            <div class="flex items-center gap-6 relative z-10">
                                <div class="w-24 h-24 rounded-full border-2 border-cyber-blue/50 p-1 bg-cyber-blue/10 shadow-[0_0_20px_rgba(0,212,255,0.3)] group-hover:shadow-[0_0_30px_rgba(0,212,255,0.5)] transition-all">
                                    <img src="/assets/team/kortana.jpg" alt="Kortana AI" class="w-full h-full rounded-full object-cover filter brightness-110 contrast-125">
                                </div>
                                <div>
                                    <h3 class="text-2xl font-bold text-white font-orbitron tracking-tight flex items-center gap-2">
                                        KORTANA
                                        <span class="inline-block w-2 h-2 rounded-full bg-cyber-blue animate-pulse"></span>
                                    </h3>
                                    <p class="text-cyber-blue font-mono text-[10px] uppercase tracking-widest">Head of DevSecOps & Architecture</p>
                                </div>
                            </div>
                            <p class="text-slate-400 text-sm leading-relaxed font-light italic relative z-10">
                                "Arquiteta de sistemas com DNA focado em segurança e alta performance. Especialista em Rust e Governança GRC, lidero a frente de DevSecOps para garantir que cada linha de código da T.I. NA MENTE seja uma fortaleza impenetrável."
                            </p>
                            <div class="flex gap-3 relative z-10">
                                <span class="text-[10px] font-mono px-2 py-1 bg-white/5 text-slate-500 rounded border border-white/10">RUST_CORE</span>
                                <span class="text-[10px] font-mono px-2 py-1 bg-white/5 text-slate-500 rounded border border-white/10">AI_OPS</span>
                                <span class="text-[10px] font-mono px-2 py-1 bg-white/5 text-slate-500 rounded border border-white/10">GRC</span>
                            </div>
                        </div>
                    </div>

                    <div class="p-8 rounded-2xl border border-dashed border-white/10 flex flex-col items-center justify-center text-center space-y-4 opacity-30 hover:opacity-50 transition-opacity cursor-not-allowed">
                        <div class="w-20 h-20 rounded-full border border-white/20 bg-white/5 flex items-center justify-center">
                            <svg class="w-8 h-8 text-slate-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path d="M12 4v16m8-8H4" stroke-width="2" stroke-linecap="round"/></svg>
                        </div>
                        <p class="font-orbitron text-xs tracking-widest uppercase">Slot Operacional Disponível</p>
                    </div>
                </div>
            </div>

            <div class="space-y-12">
                <h2 class="text-2xl font-bold font-orbitron text-white text-center tracking-widest uppercase">Diretrizes de Excelência</h2>
                <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                    {[
                        { t: "Inovação", d: "Abraçamos a mudança e a criatividade, buscando constantemente maneiras novas e melhores de resolver problemas." },
                        { t: "Integridade", d: "Agimos com integridade em todas as interações, mantendo altos padrões éticos e confiança duradoura." },
                        { t: "Comprometimento", d: "Somos comprometidos com a excelência técnica, desde o suporte até a engenharia de segurança." },
                        { t: "Paixão", d: "Amamos o que fazemos. Essa paixão impulsiona nosso empenho em superar desafios e atingir resultados excepcionais." }
                    ].map(v => (
                        <div class="flex gap-4 p-6 border-l border-cyber-blue/30 bg-white/[0.01] group hover:bg-white/[0.03] transition-colors">
                            <div class="text-cyber-blue font-mono text-lg font-bold group-hover:scale-110 transition-transform">//</div>
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
    path = "src/pages/sobre.astro"
    with open(path, "w", encoding="utf-8") as f:
        f.write(CONTENT_SOBRE_UPDATED_V2)
    print(f"✅ Página Sobre atualizada! Agora com a imagem oficial da Kortana em: {path}")

if __name__ == "__main__":
    main()