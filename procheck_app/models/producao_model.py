import sqlite3
import logging
from config import DB_PATH
from core.exceptions import DatabaseConnectionError

logger = logging.getLogger(__name__)

class ProducaoModel:
    # O Model agora recebe ou assume o caminho absoluto injetado pelas configurações
    def __init__(self, db_path=DB_PATH):
        self.db_path = db_path
        self._criar_tabela()

    def _conectar(self):
        try:
            # Passando o objeto Path diretamente (o sqlite3 aceita a partir do Python 3.7)
            return sqlite3.connect(self.db_path)
        except sqlite3.Error as e:
            logger.critical(f"Falha de conexão no caminho absoluto {self.db_path}: {e}")
            raise DatabaseConnectionError("Erro de hardware ou permissão ao acessar o banco de dados.")

    def _criar_tabela(self):
        try:
            with self._conectar() as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS saida_producao (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        codigo_lote TEXT UNIQUE NOT NULL,
                        operador TEXT NOT NULL,
                        quantidade INTEGER NOT NULL,
                        status_qualidade TEXT NOT NULL,
                        motivo_rejeicao TEXT,
                        data_hora TEXT NOT NULL
                    )
                """)
                conn.commit()
        except sqlite3.Error as e:
            logger.critical(f"Erro ao inicializar tabelas do sistema: {e}")
            raise DatabaseConnectionError("Erro de infraestrutura ao inicializar o banco de dados.")

    def lote_existe(self, lote: str) -> bool:
        with self._conectar() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT 1 FROM saida_producao WHERE codigo_lote = ?", (lote,))
            return cursor.fetchone() is not None

    def salvar(self, lote: str, operador: str, quantidade: int, status: str, motivo: str, data_hora: str):
        try:
            with self._conectar() as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    INSERT INTO saida_producao (codigo_lote, operador, quantidade, status_qualidade, motivo_rejeicao, data_hora)
                    VALUES (?, ?, ?, ?, ?, ?)
                """, (lote, operador, quantidade, status, motivo, data_hora))
                conn.commit()
        except sqlite3.IntegrityError as e:
            logger.warning(f"Tentativa de violação de integridade (Lote duplicado): {lote}. Erro: {e}")
            raise sqlite3.IntegrityError(f"O lote {lote} já foi registrado anteriormente.")
        except sqlite3.Error as e:
            logger.error(f"Erro operacional no banco de dados ao salvar lote {lote}: {e}")
            raise DatabaseConnectionError("Falha interna ao gravar os dados de produção.")

    def listar_ultimos_registros(self, limite=10):
        try:
            with self._conectar() as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    SELECT codigo_lote, operador, quantidade, status_qualidade, data_hora 
                    FROM saida_producao 
                    ORDER BY id DESC LIMIT ?
                """, (limite,))
                return cursor.fetchall()
        except sqlite3.Error as e:
            logger.error(f"Erro ao consultar registros de produção: {e}")
            return []