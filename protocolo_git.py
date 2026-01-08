import os
import subprocess

# Conteúdo do .gitignore (Padrão Astro + Segurança)
GITIGNORE_CONTENT = """# Build output
dist/
.astro/

# Dependencies
node_modules/

# Logs
npm-debug.log*
yarn-debug.log*
yarn-error.log*
pnpm-debug.log*

# Environment Variables (CRÍTICO: Nunca suba senhas)
.env
.env.production
.env.local

# OS Metadata
.DS_Store
Thumbs.db

# Editor directories
.vscode/
.idea/
"""

def run_command(command):
    try:
        result = subprocess.run(command, shell=True, check=True, text=True, capture_output=True)
        print(f"✅ Executado: {command}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"⚠️ Erro ao executar '{command}': {e.stderr.strip()}")
        return False

def main():
    root = os.getcwd()
    print("🛡️ Kortana iniciando Protocolo de Versionamento...")

    # 1. Criar .gitignore
    gitignore_path = os.path.join(root, ".gitignore")
    with open(gitignore_path, "w", encoding="utf-8") as f:
        f.write(GITIGNORE_CONTENT)
    print("✅ Arquivo .gitignore criado (Excluindo node_modules e .env).")

    # 2. Inicializar Git
    if os.path.exists(os.path.join(root, ".git")):
        print("ℹ️ Repositório Git já inicializado.")
    else:
        if run_command("git init"):
            print("✅ Repositório Git inicializado.")

    # 3. Adicionar arquivos e fazer commit inicial
    print("📦 Empacotando código fonte...")
    run_command("git add .")
    
    # Verifica se há algo para commitar
    status = subprocess.run("git status --porcelain", shell=True, capture_output=True, text=True)
    if status.stdout.strip():
        if run_command('git commit -m "feat(core): initial deploy of T.I. NA MENTE v2.0"'):
            print("✅ Commit inicial realizado com sucesso.")
    else:
        print("ℹ️ Nada a commitar (diretório limpo).")

    # 4. Renomear branch para 'main' (Padrão moderno)
    run_command("git branch -M main")

    print("\n🏁 Parte Local Concluída. Agora siga as instruções abaixo para enviar ao GitHub:")
    print("-" * 60)
    print("1. Vá em [https://github.com/new](https://github.com/new) e crie um repositório vazio.")
    print("2. Copie a URL do repositório (ex: [https://github.com/seu-usuario/tinamente-v2.git](https://github.com/seu-usuario/tinamente-v2.git)).")
    print("3. Execute os comandos abaixo no terminal:")
    print("-" * 60)
    print("git remote add origin <COLE_A_URL_AQUI>")
    print("git push -u origin main")
    print("-" * 60)

if __name__ == "__main__":
    main()