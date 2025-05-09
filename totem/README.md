# 🎫 Totem de Estacionamento — Projeto Educacional

Este é um **projeto exemplo** desenvolvido com fins didáticos para alunos de graduação em cursos de Computação, Sistemas de Informação e afins. O objetivo é demonstrar a aplicação do padrão arquitetural **MVC (Model-View-Controller)** utilizando a linguagem **Python** com a biblioteca **Tkinter** para interfaces gráficas.

---

## 🧭 Funcionalidades

### Entrada de Veículos

- Geração automática de ticket com placa aleatória
- Registro de data/hora de entrada
- Armazenamento em `data/tickets.json`
- Registro de log em `data/log_estacionamento.log`

### Totem de Pagamento

- Interface visual inspirada em totens reais
- Consulta de ticket e cálculo do valor com base no tempo
- Simula pagamento via Cartão ou PIX
- Gera comprovante de pagamento em `.txt` estilo cupom fiscal
- Atualiza o ticket como "pago" e define tempo de liberação

### Saída de Veículos

- Digita o ticket e verifica se está liberado para saída
- Compara o horário atual com o campo `liberado_ate`
- Exibe mensagem de autorização ou expiração

---

## 🧱 Arquitetura do Projeto

O projeto está organizado segundo o padrão **MVC**:

```terminal

totem/
├── controller/
│   ├── controlador_entrada.py
│   └── controlador_totem.py
├── model/
│   ├── pagamento.py
│   ├── persistencia.py
│   └── ticket.py
├── view/
│   ├── tela_entrada.py
│   ├── tela_pagamento.py
│   └── tela_saida.py
├── data/
│   ├── tickets.json
│   ├── log_estacionamento.log
│   └── comprovantes/
├── main.py            # Totem de pagamento
├── main_entrada.py    # Entrada de veículo
└── main_saida.py      # Saída do veículo

````

---

### Requisitos

- Python 3.8+

---

## 🚀 Como Executar

1. Certifique-se de ter o Python 3 instalado.
2. Clone este repositório.
3. Execute as partes conforme necessidade:

    ```bash
    python main_entrada.py   # Simula entrada do carro
    python main.py           # Simula pagamento no totem
    python main_saida.py     # Verifica liberação de saída
    ```

---

## 📚 Aprendizados Aplicados

- Uso do padrão **MVC**
- Boas práticas com funções, módulos e classes
- Boas práticas com `type hints`, `docstrings`, `logging`
- Persistência de dados com arquivos `.json`
- Manipulação de datas e horários (`datetime`)
- Geração de logs (`logging`)
- Criação de interfaces com **Tkinter**
- Simulação de sistema real: entrada, pagamento e saída
- Geração de comprovantes e simulação de totens reais
- Interface com Tkinter pensada para toque (touchscreen)

---

## 📎 Observações

Este sistema é uma **simulação acadêmica**. Nenhuma integração real com sistemas de pagamento foi implementada. Todos os dados são gerados e armazenados localmente para fins de demonstração.

---

## 👨‍🏫 Autor

Prof. Raphael Mauricio Sanches de Jesus

- Desenvolvedor de software e professor universitário.

> Projeto 100% em Python com foco em aplicação educacional e experiência de uso inspirada em equipamentos reais.
