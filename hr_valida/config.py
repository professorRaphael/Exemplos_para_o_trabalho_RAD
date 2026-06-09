from pathlib import Path

# Definição de caminhos absolutos
BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"

# Garante a existência da pasta de dados
DATA_DIR.mkdir(parents=True, exist_ok=True)

DB_PATH = DATA_DIR / "onboarding.db"
EMPRESA_DOMINIO = "@varejotech.com.br"