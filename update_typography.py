import os

# 1. ATUALIZAÇÃO DO LAYOUT BASE (Novas Fontes)
FILE_BASE_LAYOUT_TYPO = """---
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
		<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&family=Plus+Jakarta+Sans:wght@500;700;800&family=Orbitron:wght@400;700&display=swap" rel="stylesheet">
        
        <script defer src="https://cdn.jsdelivr.net/npm/alpinejs@3.x.x/dist/cdn.min.js"></script>
	</head>
	<body class="overflow-x-hidden">
		<div class="fixed inset-0 z-[-1] pointer-events-none opacity-10 bg-[linear-gradient(to_right,#80808012_1px,transparent_1px),linear-gradient(to_bottom,#80808012_1px,transparent_1px)] bg-[size:24px_24px]"></div>
		
        <Navigation />
        <slot />
        
        <footer class="border-t border-white/5 py-20 mt-20 bg-black/40">
            <div class="max-w-7xl mx-auto px-6 grid md:grid-cols-3 gap-12 text-center md:text-left">
                <div class="space-y-6">
                    <a href="/" class="text-2xl font-bold text-white tracking-tighter font-jakarta">T.I.<span class="text-cyber-blue">NA</span>MENTE</a>
                    <p class="text-slate-500 text-sm leading-relaxed">Engenharia de confiança e estratégia voltada ao valor institucional.</p>
                </div>
                <div class="space-y-6">
                    <h4 class="text-white font-jakarta text-xs font-bold tracking-widest uppercase">Navegação</h4>
                    <div class="flex flex-col gap-3 text-sm text-slate-400">
                        <a href="/servicos" class="hover:text-cyber-blue transition-colors">Capacidades</a>
                        <a href="/sobre" class="hover:text-cyber-blue transition-colors">A Empresa</a>
                        <a href="/contato" class="hover:text-cyber-blue transition-colors">Contato</a>
                    </div>
                </div>
                <div class="space-y-6 text-slate-500 text-[10px] font-mono uppercase tracking-widest">
                    <p>// PROTOCOLO_2.0_SOVEREIGN</p>
                    <p>// STATUS: OPERACIONAL</p>
                    <p>&copy; {new Date().getFullYear()} T.I. NA MENTE.</p>
                </div>
            </div>
        </footer>
	</body>
</html>
"""

# 2. ATUALIZAÇÃO DO GLOBAL CSS (Novos Tokens de Fonte)
FILE_GLOBAL_CSS_TYPO = """@import "tailwindcss";

@theme {
  --color-cyber-blue: #00d4ff;
  --color-cyber-red: #ff0055;
  --color-deep-space: #020617;
  
  /* Sistema de Fontes Refinado */
  --font-jakarta: "Plus Jakarta Sans", sans-serif;
  --font-inter: "Inter", sans-serif;
  --font-orbitron: "Orbitron", sans-serif;

  --animate-scan: scan 3s linear infinite;
}

@keyframes scan {
  0% { background-position: 0% 0%; }
  100% { background-position: 0% 100%; }
}

@layer base {
  body {
    @apply bg-deep-space text-slate-200 font-inter antialiased;
    background-image: 
      radial-gradient(circle at 50% -20%, #0ea5e915 0%, transparent 50%),
      radial-gradient(circle at 0% 0%, #020617 100%);
    background-attachment: fixed;
  }
  
  /* Títulos principais agora usam Jakarta para maior elegância */
  h1, h2, h3 {
    @apply font-jakarta tracking-tight;
  }

  /* Orbitron reservada para status e labels técnicos */
  .font-tech {
    @apply font-orbitron tracking-widest;
  }
}
"""

# 3. ATUALIZAÇÃO DA HOME (Aplicando a nova estética)
FILE_INDEX_TYPO = """---
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

				<h1 class="text-5xl md:text-7xl font-extrabold tracking-tight text-white leading-[1.1] font-jakarta">
					Inteligência que <span class="text-cyber-blue drop-shadow-[0_0_15px_rgba(0,212,255,0.2)]">protege</span>,<br />
					estratégia que <span class="text-slate-200">acolhe</span>.
				</h1>

				<p class="max-w-2xl mx-auto text-slate-400 text-lg md:text-xl font-light leading-relaxed">
					Na <span class="text-white font-medium">T.I. NA MENTE</span>, a tecnologia é o meio, mas a sua tranquilidade é o fim. Unimos precisão técnica e consultoria próxima para blindar o que é essencial para você.
				</p>

				<div class="flex flex-col sm:flex-row gap-5 justify-center pt-6">
					<a href="/servicos" class="px-10 py-4 bg-white text-deep-space font-bold rounded hover:bg-cyber-blue hover:text-white transition-all font-jakarta tracking-wide text-sm">
						VER CAPACIDADES
					</a>
					<a href="/sobre" class="px-10 py-4 border border-white/10 text-white font-bold rounded hover:bg-white/5 transition-all font-jakarta tracking-wide text-sm">
						NOSSA HISTÓRIA
					</a>
				</div>
			</div>
		</section>
	</main>
</BaseLayout>
"""

def main():
    root = os.getcwd()
    print("🎨 Kortana refinando a tipografia e o equilíbrio visual...")

    with open(os.path.join(root, "src/layouts/BaseLayout.astro"), "w", encoding="utf-8") as f:
        f.write(FILE_BASE_LAYOUT_TYPO)
    
    with open(os.path.join(root, "src/styles/global.css"), "w", encoding="utf-8") as f:
        f.write(FILE_GLOBAL_CSS_TYPO)

    with open(os.path.join(root, "src/pages/index.astro"), "w", encoding="utf-8") as f:
        f.write(FILE_INDEX_TYPO)

    print("\\n✅ LAYOUT: src/layouts/BaseLayout.astro (Fontes Plus Jakarta & Inter)")
    print("✅ STYLE: src/styles/global.css (Tokens Refinados)")
    print("✅ HOME: src/pages/index.astro (Headline Acolhedor)")
    
    print("\\n🏁 Refatoração de UX concluída. A vitrine agora está mais imponente e elegante.")

if __name__ == "__main__":
    main()