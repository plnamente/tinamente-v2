import os

folders = [
    "src/content/blog",       # Artigos e News
    "src/content/docs",       # Manuais FIM, ITIL, CIS
    "src/content/frameworks", # Matrizes de Risco (JSON/YAML)
    "src/components/ui",      # Design System (Buttons, Cards)
    "src/components/grc",     # Widgets de Conformidade
    "src/components/sentinel",# Componentes do Oráculo IA
    "src/layouts",            # Templates (Base, Dashboard, Auth)
    "src/pages/dashboard",    # Área do Cliente
    "src/pages/api/v1",       # Endpoints para integração
    "src/lib/supabase",       # Cliente do Banco de Dados
    "src/lib/utils",          # Helpers (Criptografia, Hashes)
    "src/styles",             # Tailwind v4 Configuration
    "public/assets/branding", # Logos e Mascote
]

for folder in folders:
    os.makedirs(folder, exist_ok=True)
    # Cria um .gitkeep para garantir que pastas vazias subam para o Git
    with open(os.path.join(folder, ".gitkeep"), "w") as f:
        pass

print("✅ Estrutura 'Cyber-GRC' implementada com sucesso.")