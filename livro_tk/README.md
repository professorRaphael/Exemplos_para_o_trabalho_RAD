# Livraria Tkinter

Este projeto é um exemplo de aplicação de gerenciamento de livros utilizando a biblioteca Tkinter para a interface gráfica e SQLite para o banco de dados. Este exemplo foi criado para a turma de Programação Rápida Python como um ponto de partida para seus próprios projetos. ***Ele contém propositalmente algumas falhas e áreas de melhoria, incentivando os alunos a corrigir e aprimorar o código.***

## Descrição

A aplicação permite:

- Visualizar todos os livros
= Pesquisar livros por título, autor, ano ou ISBN
- Adicionar novos livros
- Atualizar informações de livros existentes
- Deletar livros
- Selecionar um livro da lista para visualizar ou editar suas informações

## Estrutura do Projeto

O projeto é dividido em dois arquivos principais:

- frontend.py: Contém o código para a interface gráfica utilizando Tkinter.
- backend.py: Contém as funções de banco de dados utilizando SQLite.

## frontend.py

Este arquivo define a interface gráfica e as funcionalidades da aplicação. Ele inclui:

- Entradas de texto para título, autor, ano e ISBN
- Botões para visualizar, adicionar, atualizar, deletar e fechar a aplicação
- Uma lista que exibe os livros com um sistema de seleção para editar ou deletar

## backend.py

Este arquivo define as funções que interagem com o banco de dados SQLite. Ele inclui:

- Funções para conectar ao banco de dados e criar a tabela de livros
- Funções para inserir, visualizar, pesquisar, atualizar e deletar registros no banco de dados

## Observações

- O código contém algumas falhas propositais, como falta de validação de entrada e manejo básico de erros. Essas falhas foram deixadas intencionalmente para que os alunos possam identificar e corrigir como parte do aprendizado.
- Certifique-se de que o arquivo backend.py esteja no mesmo diretório que frontend.py.
