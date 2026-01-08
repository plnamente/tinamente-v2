import os

# Conteúdo do Workflow do GitHub Actions
FILE_GITHUB_WORKFLOW = """name: Deploy to Hostinger

on:
  push:
    branches: [ main ]

jobs:
  web-deploy:
    name: 🎉 Deploy to Hostinger
    runs-on: ubuntu-latest
    steps:
    - name: 🚚 Get latest code
      uses: actions/checkout@v4

    - name: 🟢 Setup Node.js
      uses: actions/setup-node@v4
      with:
        node-version: '20'

    - name: 📦 Install dependencies
      run: npm install

    - name: 🏗️ Build Project
      run: npm run build

    - name: 📂 Upload to Hostinger (FTP)
      uses: SamKirkland/FTP-Deploy-Action@v4.3.5
      with:
        server: ${{ secrets.FTP_SERVER }}
        username: ${{ secrets.FTP_USERNAME }}
        password: ${{ secrets.FTP_PASSWORD }}
        local-dir: ./dist/
        server-dir: ./public_html/ 
        # ATENÇÃO: Se o seu site estiver numa subpasta no Hostinger, 
        # ajuste o server-dir acima. Ex: ./public_html/meusite/
"""

def write_file(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"✅ Criado: {path}")

def main():
    root = os.getcwd()
    print("🚀 Kortana configurando Pipeline de CI/CD...")

    # Cria a pasta .github/workflows e o arquivo YAML
    write_file(os.path.join(root, ".github/workflows/deploy.yml"), FILE_GITHUB_WORKFLOW)

    print("\\n🏁 Pipeline Configurado.")
    print("👉 Próximo passo: Configurar os Segredos (Secrets) no GitHub.")

if __name__ == "__main__":
    main()