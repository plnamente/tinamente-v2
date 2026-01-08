import subprocess
import sys

def run_command(command):
    print(f"⚙️ Executando: {command}")
    try:
        # Executa o comando e captura a saída
        result = subprocess.run(command, shell=True, check=True, text=True, capture_output=True)
        # Se houver saída, imprime (exceto para git push que joga no stderr as vezes)
        if result.stdout:
            print(f"✅ {result.stdout.strip()}")
        return True
    except subprocess.CalledProcessError as e:
        # Se der erro, imprime o motivo
        print(f"⚠️ Retorno do comando: {e.stderr.strip()}")
        # Git push as vezes retorna status não-zero apenas por avisos, mas vamos considerar erro aqui
        return False

def main():
    print("🛡️ Kortana iniciando protocolo de Sincronização (Push)...")

    # 1. Adicionar todos os arquivos (Staging)
    print("\n📦 Adicionando arquivos modificados ao palco...")
    run_command("git add .")

    # 2. Verificar status antes de commitar
    status = subprocess.run("git status --porcelain", shell=True, capture_output=True, text=True)
    
    if not status.stdout.strip():
        print("ℹ️ Nenhuma alteração nova detectada para enviar.")
        
        # Mesmo sem commit novo, tentamos o push para garantir que o remoto esteja igual ao local
        print("\n🚀 Verificando sincronia com a nuvem...")
        run_command("git push origin main")
    else:
        # 3. Commitar
        print("\n📝 Criando ponto de restauração (Commit)...")
        # Mensagem automática para agilizar
        run_command('git commit -m "feat(update): sync project files and database config"')

        # 4. Enviar (Push)
        print("\n🚀 Enviando (PUSH) para o GitHub...")
        if run_command("git push origin main"):
            print("\n✅ Sincronização concluída! Seu código está 100% atualizado na nuvem.")
        else:
            print("\n❌ Falha no envio. Verifique se o Token de Acesso (PAT) está configurado corretamente se pediu senha.")

if __name__ == "__main__":
    main()