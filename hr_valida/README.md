# HR-Valida — Terminal Local de Onboarding

## ⚠️ Aviso de Escopo Acadêmico

> **Nota do Desenvolvedor:** Este projeto foi desenvolvido exclusivamente para fins didáticos e avaliativos em nível de graduação. Embora aplique padrões arquiteturais de mercado (MVC limpo, injeção de dependências e higienização rigorosa de dados via Regex), trata-se de um **Protótipo de Validação de Conceito (PoC)**. Em um ambiente corporativo real, sistemas que lidam com dados sensíveis (LGPD) exigiriam criptografia de banco de dados, ofuscação de memória e túneis seguros de sincronização de rede que não estão implementados aqui.

---

## 📝 Sobre o Projeto

O **HR-Valida** é uma aplicação desktop offline (Data Gatekeeper) desenvolvida para o Departamento Pessoal de redes de varejo. O sistema atua como uma barreira sanitária de dados durante o processo de pré-cadastro e onboarding de novos colaboradores nas filiais.

O objetivo principal é garantir que **nenhum dado malformado, incompleto ou matematicamente inválido** seja persistido no banco de dados local antes da sincronização com o ERP central (nuvem).

### Principais Funcionalidades

* **Motor de Validação (Regex):** Filtros rigorosos para e-mails corporativos restritos, telefones e nomes utilizando Expressões Regulares (`re`).
* **Verificação Lógica:** Validação matemática do dígito verificador de CPFs e consistência do calendário para datas de nascimento.
* **Feedback Dinâmico na UI:** A interface informa o usuário em tempo real exatamente qual campo falhou na validação de negócio.
* **Persistência Local (SQLite):** Banco de dados isolado no ambiente operacional (`pathlib`), protegido contra inserções de CPFs duplicados.

---

## 🏗️ Arquitetura Modular (MVC)

O projeto rompe com o modelo de script único e implementa uma separação estrita de responsabilidades, facilitando a manutenção e a criação de testes unitários.

```text
hr_valida/
│
├── main.py            # Ponto de entrada e Injeção de Dependências
├── config.py          # Centralização de caminhos OS absolutos (pathlib) e constantes
├── validators.py      # Camada de Regras (Regex puros e lógica matemática)
├── models.py          # Camada Model: Conexão SQLite e queries SQL
├── controllers.py     # Camada Controller: Orquestração de negócio e sanitização
└── views.py           # Camada View: Interface Tkinter (GUI) reativa

```

### Tecnologias Utilizadas

* **Linguagem:** Python 3.10+
* **Expressões Regulares:** Módulo `re` (Built-in)
* **Interface Gráfica:** Tkinter / TTK (Built-in)
* **Banco de Dados:** SQLite3 (Serverless)
* **Manipulação de Arquivos OS:** `pathlib`

---

## 🚀 Como Executar o Projeto

A aplicação foi desenvolvida utilizando apenas a **Standard Library** do Python. Não é necessária a criação de ambientes virtuais (`venv`) ou instalação de dependências via `pip`.

1. **Geração Automática de Infraestrutura:**
Ao rodar a aplicação pela primeira vez, o script `config.py` se encarregará de criar a pasta `data/` na raiz do projeto e inicializar o banco de dados `onboarding.db` de forma autônoma.

---

## 🛠️ Detalhes de Implementação Técnica

* **Desacoplamento de Regex:** A classe `ValidadorRegex` é 100% estática e não conhece nada sobre Tkinter ou SQLite. Isso permite que essas regras sejam facilmente importadas para uma API Flask ou FastAPI no futuro.
* **Prevenção de SQL Injection e Concorrência:** Uso de prepared statements (parâmetros `?`) no SQLite e tratamento da exceção `sqlite3.IntegrityError` no Controller para lidar graciosamente com CPFs duplicados.

---

## 📋 Informações do Projeto Acadêmico

* **Instituição:** Universidade Estácio de Sá
* **Contexto:** Atividade Prática
* **Professor:** Raphael Mauricio Sanches de Jesus
