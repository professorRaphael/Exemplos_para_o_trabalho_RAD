# 🌞 Tela de Login e Cadastro em Python

Este é um projeto exemplo criado para auxiliar **estudantes de programação rápida em Python**. O objetivo é demonstrar a criação de uma interface gráfica simples usando o **Tkinter**, com telas de **login** e **cadastro**. Este projeto é puramente **educacional** e deve ser usado apenas para **fins de estudo**.

## Funcionalidades

- Tela de **Login**: Permite ao usuário inserir email e senha.
- Tela de **Cadastro**: Permite o registro de novos usuários no sistema.
- Tela de **Entrada**: Após o login bem-sucedido, o usuário é redirecionado para uma tela principal de boas-vindas.

## Estrutura do Projeto

```code
exemplo_login/
│
├── controller
│   └── auth_controller.py # Controlador responsável por autenticação e registro
├── model
│   └── user.py # Modelo de dados do usuário
├── view
│   ├── login_view.py # Tela de Login
│   └── register_view.py # Tela de Cadastro
│   └── main_view.py # Tela de Entrada
└── db
    └── database.py # Conexão e manipulação do banco de dados (SQLite)
```

## Requisitos

- **Python 3.x**
- **Tkinter** (já incluso em distribuições Python)
- **SQLite** (biblioteca padrão do Python)

## Instalação

1. Clone o repositório ou baixe o código.

   ```bash
   git clone https://github.com/ProfessorRaphael/exemplo_login.git
   cd exemplo_login
    ```

2. Execute o script login_view.py para abrir a tela de login:

   ```bash
   python login_view.py
   ```

## Uso

- Tela de Login: Insira o email e senha de um usuário registrado.
Se você não tem um usuário registrado, clique em Registrar para acessar a tela de cadastro.
- Tela de Cadastro: Insira seu nome, email e senha. Após o registro, você será redirecionado de volta à tela de login.
- Após o login, você será levado para a tela principal de boas-vindas.

## Finalidade

Este projeto foi criado para fins educacionais e exemplificação do uso de interfaces gráficas em Python. Não deve ser utilizado em produção, pois contém apenas o básico de lógica de autenticação e uso de banco de dados para estudo.

Destina-se a estudantes de programação e serve como uma base inicial para entender o uso de Tkinter e manipulação de banco de dados com SQLite.

## Contribuição

Contribuições são bem-vindas! Se você tiver sugestões para melhorias ou novos exemplos, fique à vontade para abrir um pull request.

🫠*Nota*: Este projeto não possui medidas de segurança avançadas, como criptografia de senhas ou autenticação robusta, sendo adequado apenas para propósitos educacionais simples, por favor continue avançando seus estudos na manipulação de um login mais e mais adequado.
