from pathlib import Path

# Define a raiz do projeto (onde o main.py está localizado)
BASE_DIR = Path(__file__).resolve().parent

# Define os caminhos para os dados e logs (isolados para organização)
DATA_DIR = BASE_DIR / "data"
LOG_DIR = BASE_DIR / "logs"

# Garante que os diretórios físicos existam no sistema operacional
DATA_DIR.mkdir(parents=True, exist_ok=True)
LOG_DIR.mkdir(parents=True, exist_ok=True)

# Caminhos absolutos e imutáveis para os arquivos
DB_PATH = DATA_DIR / "logistica_producao.db"
LOG_FILE_PATH = LOG_DIR / "terminal_operacao.log"

# String de conexão padronizada para o SQLite
SQLITE_URI = f"file:{DB_PATH}?mode=rwc"