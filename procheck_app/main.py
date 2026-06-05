import tkinter as tk
import logging
import sys
from config import LOG_FILE_PATH
from models.producao_model import ProducaoModel
from controllers.producao_controller import ProducaoController
from views.main_view import ProducaoView

def configurar_logging():
    """Configura os logs utilizando o caminho absoluto centralizado."""
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        handlers=[
            # Uso do Path absoluto garante escrita no local correto
            logging.FileHandler(LOG_FILE_PATH, encoding="utf-8"),
            logging.StreamHandler(sys.stdout)
        ]
    )

def main():
    configurar_logging()
    logging.info("Inicializando o terminal ProCheck Industrial...")

    root = tk.Tk()
    try:
        model = ProducaoModel()
        controller = ProducaoController(model)
        app = ProducaoView(root, controller)
        
        root.mainloop()
    except Exception as e:
        logging.critical(f"Falha fatal na inicialização da aplicação: {e}")

if __name__ == "__main__":
    main()