import os

# --- CONTEÚDO DOS ARQUIVOS ---

# 1. Página de Login (Futurista)
FILE_LOGIN = """---
import BaseLayout from '../layouts/BaseLayout.astro';
---

<BaseLayout title="Acesso Restrito">
    <div class="min-h-screen flex items-center justify-center px-4">
        <div class="max-w-md w-full bg-deep-space/80 border border-white/10 p-8 rounded-2xl backdrop-blur-xl relative overflow-hidden group">
            
            <div class="absolute inset-0 bg-gradient-to-r from-transparent via-cyber-blue/20 to-transparent translate-x-[-200%] group-hover:translate-x-[200%] transition-transform duration-[2s] pointer-events-none"></div>

            <div class="text-center mb-8">
                <div class="inline-flex items-center justify-center w-16 h-16 rounded-full bg-cyber-blue/10 text-cyber-blue mb-4 border border-cyber-blue/20">
                    <svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect width="18" height="11" x="3" y="11" rx="2" ry="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg>
                </div>
                <h1 class="text-2xl font-bold font-orbitron text-white">Acesso Membro</h1>
                <p class="text-slate-400 text-sm mt-2">Identifique-se para acessar o Command Center.</p>
            </div>

            <form class="space-y-6" action="/dashboard"> <div>
                    <label for="email" class="block text-xs font-mono text-cyber-blue mb-2 uppercase tracking-wider">ID Operacional (Email)</label>
                    <input type="email" id="email" name="email" class="w-full bg-black/50 border border-white/10 rounded px-4 py-3 text-white focus:border-cyber-blue focus:ring-1 focus:ring-cyber-blue outline-none transition-all" placeholder="nome@empresa.com" required>
                </div>

                <div>
                    <label for="password" class="block text-xs font-mono text-cyber-blue mb-2 uppercase tracking-wider">Chave de Acesso</label>
                    <input type="password" id="password" name="password" class="w-full bg-black/50 border border-white/10 rounded px-4 py-3 text-white focus:border-cyber-blue focus:ring-1 focus:ring-cyber-blue outline-none transition-all" placeholder="••••••••" required>
                </div>

                <button type="submit" class="w-full bg-cyber-blue text-deep-space font-bold py-3 rounded hover:bg-cyan-400 transition-all shadow-[0_0_15px_rgba(0,212,255,0.3)]">
                    INICIAR SESSÃO
                </button>
            </form>

            <div class="mt-6 text-center">
                <a href="#" class="text-xs text-slate-500 hover:text-cyber-blue transition-colors">Esqueceu suas credenciais?</a>
            </div>
        </div>
    </div>
</BaseLayout>
"""

# 2. Layout do Dashboard (Sidebar + Topbar)
FILE_DASHBOARD_LAYOUT = """---
import '../styles/global.css';

interface Props {
	title: string;
}

const { title } = Astro.props;
---

<!doctype html>
<html lang="pt-br">
	<head>
		<meta charset="UTF-8" />
		<meta name="viewport" content="width=device-width" />
		<link rel="icon" type="image/svg+xml" href="/favicon.svg" />
		<title>{title} | Command Center</title>
		<link rel="preconnect" href="https://fonts.googleapis.com">
		<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
		<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600&family=Orbitron:wght@400;700&display=swap" rel="stylesheet">
	</head>
	<body class="bg-deep-space text-slate-200 font-inter antialiased flex h-screen overflow-hidden">
		
        <aside class="w-64 border-r border-white/10 bg-[#020617] flex flex-col hidden md:flex">
            <div class="h-16 flex items-center px-6 border-b border-white/5">
                <span class="text-lg font-bold font-orbitron text-white">TINAMENTE<span class="text-cyber-blue text-xs ml-1">v2</span></span>
            </div>

            <nav class="flex-1 px-4 py-6 space-y-1">
                <a href="/dashboard" class="flex items-center gap-3 px-4 py-3 bg-cyber-blue/10 text-cyber-blue rounded-md text-sm font-medium border border-cyber-blue/20">
                    <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2H6a2 2 0 01-2-2V6zM14 6a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2V6zM4 16a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2H6a2 2 0 01-2-2v-2zM14 16a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2v-2z"></path></svg>
                    Visão Geral
                </a>
                <a href="#" class="flex items-center gap-3 px-4 py-3 text-slate-400 hover:text-white hover:bg-white/5 rounded-md text-sm font-medium transition-colors">
                    <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
                    Meus Selos
                </a>
                <a href="#" class="flex items-center gap-3 px-4 py-3 text-slate-400 hover:text-white hover:bg-white/5 rounded-md text-sm font-medium transition-colors">
                    <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2m14 0V9a2 2 0 00-2-2M5 11V9a2 2 0 012-2m0 0V5a2 2 0 012-2h6a2 2 0 012 2v2M7 7h10"></path></svg>
                    Cofre de Evidências
                </a>
            </nav>

            <div class="p-4 border-t border-white/5">
                <a href="/" class="flex items-center gap-2 text-xs text-slate-500 hover:text-white transition-colors">
                    <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 16l4-4m0 0l-4-4m4 4H7m6 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h4a3 3 0 013 3v1"></path></svg>
                    Sair do Sistema
                </a>
            </div>
        </aside>

        <main class="flex-1 flex flex-col h-screen overflow-hidden bg-black/20">
            <header class="h-16 border-b border-white/5 flex items-center justify-between px-6 bg-deep-space md:bg-transparent">
                <h1 class="text-xl font-orbitron text-white md:hidden">TINAMENTE</h1>
                <div class="text-sm text-slate-400 ml-auto">
                    Logado como: <span class="text-cyber-blue font-mono">ADMIN_CISO</span>
                </div>
            </header>

            <div class="flex-1 overflow-auto p-6 md:p-10">
                <slot />
            </div>
        </main>
	</body>
</html>
"""

# 3. Dashboard Principal (Index)
FILE_DASHBOARD_INDEX = """---
import DashboardLayout from '../../layouts/DashboardLayout.astro';

// Simulação de dados
const stats = [
    { label: "Nível de Conformidade", value: "15%", color: "text-cyber-red", desc: "Crítico - Atenção Necessária" },
    { label: "Controles Implementados", value: "3/153", color: "text-white", desc: "CIS Controls v8" },
    { label: "Evidências Validadas", value: "0", color: "text-white", desc: "Aguardando Upload" },
];
---

<DashboardLayout title="Visão Geral">
    <div class="max-w-6xl mx-auto space-y-8">
        
        <div class="flex flex-col md:flex-row md:items-center justify-between gap-4">
            <div>
                <h2 class="text-3xl font-bold text-white font-orbitron">Painel de Comando</h2>
                <p class="text-slate-400">Status atual da postura de segurança da organização.</p>
            </div>
            <button class="px-4 py-2 bg-cyber-blue text-deep-space font-bold rounded text-sm hover:bg-cyan-400 transition-colors">
                + NOVA AUDITORIA
            </button>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
            {stats.map(stat => (
                <div class="p-6 rounded-xl border border-white/5 bg-white/[0.02] backdrop-blur hover:border-white/10 transition-all">
                    <h3 class="text-slate-500 text-xs font-mono uppercase mb-2">{stat.label}</h3>
                    <div class={`text-4xl font-bold font-orbitron mb-1 ${stat.color}`}>{stat.value}</div>
                    <div class="text-xs text-slate-500">{stat.desc}</div>
                </div>
            ))}
        </div>

        <div class="p-8 rounded-xl border border-white/5 bg-white/[0.02]">
            <h3 class="text-xl font-bold text-white font-orbitron mb-6 flex items-center gap-2">
                <span class="w-2 h-2 rounded-full bg-cyber-red animate-pulse"></span>
                Ações Prioritárias (IG1)
            </h3>
            
            <div class="space-y-4">
                {[1, 2, 3].map(i => (
                    <div class="flex items-center justify-between p-4 rounded bg-black/40 border border-white/5 hover:border-cyber-blue/30 transition-colors group">
                        <div class="flex items-center gap-4">
                            <div class="w-8 h-8 rounded bg-white/5 flex items-center justify-center text-xs font-mono text-slate-400 group-hover:text-cyber-blue">0{i}</div>
                            <div>
                                <h4 class="text-white text-sm font-medium">Inventário de Ativos Enterprise</h4>
                                <p class="text-xs text-slate-500">CIS Control 1.{i} • Função: IDENTIFICAR</p>
                            </div>
                        </div>
                        <button class="text-xs border border-white/10 px-3 py-1 rounded text-slate-400 hover:text-white hover:border-white/30">
                            Detalhes
                        </button>
                    </div>
                ))}
            </div>
        </div>

    </div>
</DashboardLayout>
"""

# 4. Página "Sobre" (Estrutura para colar conteúdo)
FILE_SOBRE = """---
import BaseLayout from '../layouts/BaseLayout.astro';
---

<BaseLayout title="A Empresa">
    <main class="max-w-4xl mx-auto px-6 py-20">
        
        <header class="mb-16 text-center">
            <h1 class="text-4xl md:text-6xl font-bold font-orbitron text-white mb-6">QUEM <span class="text-cyber-blue">SOMOS</span></h1>
            <div class="w-24 h-1 bg-cyber-blue mx-auto rounded-full"></div>
        </header>

        <article class="prose prose-invert prose-lg max-w-none text-slate-300">
            <h3>Nossa Missão</h3>
            <p>
                [COLE AQUI O TEXTO DE MISSÃO DO SITE ANTIGO]
                Transformar a segurança cibernética de um centro de custo para um diferencial estratégico...
            </p>

            <h3>Nossa Visão</h3>
            <p>
                [COLE AQUI O TEXTO DE VISÃO]
                Ser a referência nacional em implementação de frameworks de governança automatizada...
            </p>

            <div class="grid md:grid-cols-2 gap-8 my-12 not-prose">
                <div class="p-6 border border-white/10 rounded-lg bg-white/5">
                    <h4 class="text-xl font-orbitron text-white mb-2">Engenharia</h4>
                    <p class="text-sm">Desenvolvimento de soluções proprietárias em Rust e Python.</p>
                </div>
                <div class="p-6 border border-white/10 rounded-lg bg-white/5">
                    <h4 class="text-xl font-orbitron text-white mb-2">Consultoria</h4>
                    <p class="text-sm">Alinhamento estratégico com ITIL 4 e CIS v8.</p>
                </div>
            </div>

            <h3>Nossa História</h3>
            <p>
                [COLE AQUI A HISTÓRIA DA TINAMENTE]
                Fundada com o propósito de...
            </p>

        </article>

    </main>
</BaseLayout>
"""

def write_file(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"✅ Criado: {path}")

def main():
    root = os.getcwd()
    print(f"🛠️ Iniciando deploy da Área de Membros em: {root}")

    # Criando arquivos
    write_file(os.path.join(root, "src/pages/login.astro"), FILE_LOGIN)
    write_file(os.path.join(root, "src/layouts/DashboardLayout.astro"), FILE_DASHBOARD_LAYOUT)
    write_file(os.path.join(root, "src/pages/dashboard/index.astro"), FILE_DASHBOARD_INDEX)
    write_file(os.path.join(root, "src/pages/sobre.astro"), FILE_SOBRE)

    print("\n🚀 Área de Membros Implantada.")
    print("1. Acesse /login para ver a tela de entrada.")
    print("2. Clique em 'Iniciar Sessão' para ver o Dashboard.")
    print("3. Edite src/pages/sobre.astro para colar os textos do site antigo.")

if __name__ == "__main__":
    main()