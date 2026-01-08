import os

# Definição dos serviços baseada no material técnico fornecido
services = {
    "soc-24-7.md": """---
title: "Shield & Strike: SOC 24/7"
description: "Monitoramento e resposta a incidentes com inteligência baseada no framework FIM."
icon: "shield-check"
order: 1
category: "Shield & Strike"
---

Nossa operação de **Security Operations Center (SOC)** não se limita a olhar alertas. Utilizamos a metodologia do **CERT.br (Foundations of Incident Management)** para garantir uma resposta tática e coordenada.

### Diferenciais:
- **Resposta Tática:** Gestão completa do ciclo de vida de incidentes.
- **Inteligência de Ameaças:** Identificação proativa baseada em vetores reais.
- **Resiliência Operacional:** Blindagem contínua dos ativos críticos.
""",

    "consultoria-grc.md": """---
title: "Compliance Radar: GRC"
description: "Governança, Riscos e Conformidade através das matrizes CIS v8 e NIST."
icon: "clipboard-list"
order: 2
category: "Shield & Strike"
---

Transformamos a burocracia em estratégia. Nossa consultoria de **GRC** foca em implementar os controles do **CIS Controls v8** para elevar o nível de maturidade da sua empresa.

### O que entregamos:
- **Auditoria Interna:** Validação rigorosa de controles de segurança.
- **Matriz de Riscos:** Priorização baseada em impacto real ao negócio.
- **Selos de Conformidade:** Preparação total para certificações internacionais.
""",

    "devsecops-rust.md": """---
title: "Tactical Dev: DevSecOps"
description: "Engenharia de software segura e ferramentas customizadas em Rust."
icon: "code-bracket"
order: 3
category: "Tactical Development"
---

Segurança não é um anexo, é o alicerce. Desenvolvemos pipelines e ferramentas de segurança utilizando **Rust**, garantindo performance extrema e segurança de memória (Memory Safety).

### Nossa Engenharia:
- **Custom Security Tools:** Ferramentas sob medida para auditoria e defesa.
- **Secure SDLC:** Integração de segurança em todas as fases do desenvolvimento.
- **AI-Driven Defense:** Implementação de IA para detecção de anomalias em código.
""",

    "gestao-itil.md": """---
title: "Core Ops: Gestão Estratégica"
description: "Eficiência operacional e gerenciamento de serviços baseados no ITIL 4."
icon: "cpu-chip"
order: 4
category: "Core Operations"
---

A TI precisa falar a língua do negócio. Aplicamos os princípios do **ITIL 4** para garantir que a infraestrutura e os serviços gerem valor real e escalabilidade.

### Foco Operacional:
- **Service Value System:** Fluxos de trabalho otimizados e sem gargalos.
- **Gestão de Ativos:** Controle total sobre o inventário tecnológico.
- **Suporte de Elite:** Atendimento focado na continuidade do negócio.
"""
}

def setup_services():
    target_dir = "src/content/services"
    
    # Cria a pasta se não existir
    os.makedirs(target_dir, exist_ok=True)
    print(f"📂 Pasta verificada/criada: {target_dir}")

    for filename, content in services.items():
        path = os.path.join(target_dir, filename)
        with open(path, "w", encoding="utf-8") as f:
            f.write(content.strip())
        print(f"✅ Arquivo gerado: {filename}")

if __name__ == "__main__":
    setup_services()