import sqlite3
from config import DB_PATH

class DatabaseModel:
    def __init__(self):
        self._criar_tabelas()

    def _conectar(self):
        return sqlite3.connect(DB_PATH)

    def _criar_tabelas(self):
        with self._conectar() as conn:
            conn.cursor().execute("""
                CREATE TABLE IF NOT EXISTS candidatos (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome_completo TEXT NOT NULL,
                    cpf TEXT UNIQUE NOT NULL,
                    email_corporativo TEXT NOT NULL,
                    telefone TEXT NOT NULL,
                    data_nascimento TEXT NOT NULL
                )
            """)
            conn.commit()

    def inserir_candidato(self, nome: str, cpf: str, email: str, telefone: str, data_nasc: str):
        with self._conectar() as conn:
            conn.cursor().execute("""
                INSERT INTO candidatos (nome_completo, cpf, email_corporativo, telefone, data_nascimento)
                VALUES (?, ?, ?, ?, ?)
            """, (nome, cpf, email, telefone, data_nasc))
            conn.commit()

    def buscar_cadastros_recentes(self):
        with self._conectar() as conn:
            return conn.cursor().execute("""
                SELECT nome_completo, cpf, email_corporativo 
                FROM candidatos ORDER BY id DESC LIMIT 15
            """).fetchall()