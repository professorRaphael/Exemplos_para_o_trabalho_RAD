import sqlite3
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from model.user import User
import os


class Database:
    def __init__(self, nome_banco="auth_db.sqlite"):
        self.nome_banco = os.path.join(os.path.dirname(__file__), nome_banco)
        self.conn = None
        self.conectar()
        self.criar_tabela_usuarios()

    def conectar(self):
        """Conecta ao banco de dados SQLite"""
        try:
            self.conn = sqlite3.connect(self.nome_banco)
        except sqlite3.Error as e:
            print(f"Erro ao conectar ao banco de dados: {e}")

    def criar_tabela_usuarios(self):
        if self.conn:
            try:
                cursor = self.conn.cursor()
                cursor.execute(
                    """CREATE TABLE IF NOT EXISTS Usuario (
                        email TEXT PRIMARY KEY,
                        nome TEXT NOT NULL,
                        senha TEXT NOT NULL
                    )"""
                )
                self.conn.commit()
            except sqlite3.Error as e:
                print(f"Erro ao criar tabela Usuario: {e}")

    def inserir_usuario(self, user: User):
        if self.conn:
            try:
                cursor = self.conn.cursor()
                cursor.execute(
                    "INSERT INTO Usuario (email, nome, senha) VALUES (?, ?, ?)",
                    (user.email, user.nome, user.senha),
                )
                self.conn.commit()
            except sqlite3.Error as e:
                print(f"Erro ao inserir usuário: {e}")

    def buscar_usuario_por_email(self, email: str):
        if self.conn:
            try:
                cursor = self.conn.cursor()
                cursor.execute("SELECT * FROM Usuario WHERE email=?", (email,))
                row = cursor.fetchone()
                if row:
                    return User(nome=row[1], email=row[0], senha=row[2])
            except sqlite3.Error as e:
                print(f"Erro ao buscar usuário por email: {e}")
        return None
