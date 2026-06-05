# ProCheck Industrial — Terminal de Borda (Academic Project)

### ⚠️ Aviso de Escopo Acadêmico
> **Nota do Desenvolvedor:** Este projeto foi desenvolvido exclusivamente para fins didáticos e avaliativos em nível de graduação tecnológica. Embora siga rigorosos padrões arquiteturais de mercado (MVC, tratamento de exceções robusto e logging), trata-se de um **Protótipo de Validação de Conceito (PoC)**. Portanto, não possui todas as camadas de segurança, criptografia, sincronização de rede ou redundância necessárias para um ambiente de produção industrial real.

---

## 📝 Sobre o Projeto

O **ProCheck Industrial** é um sistema desktop de ponta de linha (Edge Computing) projetado para otimizar o registro de saída de lotes e o controle de qualidade no chão de fábrica da metalúrgica fictícia *SteelTech S.A.*.

O sistema visa substituir registros manuais em papel por um terminal de alta resiliência, capaz de operar de forma 100% offline, mitigando problemas comuns de infraestrutura industrial (como quedas de rede e flutuação de energia).

### Principais Funcionalidades
* **Bipagem Assistida:** Otimização de foco de interface para leitura automatizada via leitores de código de barras.
* **Persistência Resiliente:** Armazenamento local autossuficiente via SQLite com isolamento de diretórios.
* **Controle de Qualidade Condicional:** Bloqueio e exigência de justificativas técnicas para lotes classificados como "Reprovados".
* **Auditoria por Log:** Rastreabilidade completa de operações e erros críticos gravados em arquivo físico rotativo.

---

## 🏗️ Arquitetura e Boas Práticas

O projeto foi construído utilizando o padrão **MVC (Model-View-Controller)** para garantir o desacoplamento de responsabilidades, alta testabilidade e facilidade de manutenção.

```text
procheck_app/
│
├── main.py                # Ponto de entrada e inicialização dos serviços
├── config.py              # Centralização de caminhos absolutos e paths OS (pathlib)
├── core/
│   └── exceptions.py      # Definição de exceções customizadas de negócio
├── models/
│   └── producao_model.py  # Camada Model: Queries SQL puras e persistência SQLite
├── controllers/
│   └── producao_controller.py # Camada Controller: Validações e regras de negócio
└── views/
    └── main_view.py       # Camada View: Interface gráfica (GUI) baseada em Tkinter

```

### Tecnologias Utilizadas

* **Linguagem:** Python 3.10+
* **Interface Gráfica:** Tkinter / TTK (Built-in)
* **Banco de Dados:** SQLite3 (Serverless)
* **Manipulação de Arquivos:** `pathlib` (Cross-platform compatibility)
* **Monitoramento:** `logging` (Built-in)

---

## 🚀 Como Executar o Projeto

Como o projeto priorizou a resiliência local e utilizou apenas a biblioteca padrão do Python, **não há necessidade de instalar dependências externas via pip**.

### Pré-requisitos

* Python 3.10 ou superior instalado e adicionado ao seu PATH.

### Passo a Passo

1. **Clonar o Repositório:**
```bash
git clone [https://github.com/professorRaphael/procheck_app.git](https://github.com/professorRaphael/procheck_app.git)
cd procheck_app

```


2. **Executar a Aplicação:**
```bash
python main.py

```


3. **Verificação do Ambiente:**
Após a primeira execução, o sistema criará automaticamente a seguinte estrutura de infraestrutura no diretório raiz:
* `data/logistica_producao.db`: O banco de dados local inicializado.
* `logs/terminal_operacao.log`: O arquivo de texto capturando os eventos em tempo real.



---

## 🛠️ Detalhes de Implementação Técnica

* **Robustez de Caminhos (Path Management):** Utilização de caminhos absolutos e geração dinâmica de diretórios pelo `pathlib.Path`, prevenindo a criação de arquivos órfãos quando o app é executado via atalhos do Windows.
* **Tratamento de Exceções Hierárquico:** Separação clara entre `BusinessError` (erros de operação do usuário) e `DatabaseConnectionError` (falhas físicas de infraestrutura ou permissão de escrita).

---

## 📋 Informações do Projeto

* **Contexto:** Atividade Prática de Fixação - RAD
* **Professor Orientador:** Raphael Mauricio Sanches de Jesus
