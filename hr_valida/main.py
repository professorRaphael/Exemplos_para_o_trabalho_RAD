import tkinter as tk
from models import DatabaseModel
from controllers import HRController
from views import HRView

if __name__ == "__main__":
    root = tk.Tk()
    
    # Orquestração (Injeção de Dependência da Arquitetura Limpa)
    db_model = DatabaseModel()
    hr_controller = HRController(db_model)
    app = HRView(root, hr_controller)
    
    root.mainloop()