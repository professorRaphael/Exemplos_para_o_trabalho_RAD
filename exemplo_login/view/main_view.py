import tkinter as tk


class MainView(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Tela Principal")
        self.geometry("400x200")
        self.config(bg="#f0f0f0")
        self.centralizar_janela()
        self.create_widgets()

    def centralizar_janela(self):
        self.update_idletasks()
        width = self.winfo_width()
        height = self.winfo_height()
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry(f"{width}x{height}+{x}+{y}")

    def create_widgets(self):
        welcome_label = tk.Label(
            self, text="Bem-vindo ao Sistema!", font=("Helvetica", 16), bg="#f0f0f0"
        )
        welcome_label.pack(pady=20)

        btn_logout = tk.Button(
            self,
            text="Sair",
            command=self.sair,
            bg="#ff4d4d",
            fg="white",
            font=("Helvetica", 12),
            width=10,
        )
        btn_logout.pack(pady=10)

    def sair(self):
        self.destroy()
        LoginView()
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from view.login_view import (
    LoginView,
)
