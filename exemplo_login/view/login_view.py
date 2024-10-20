import tkinter as tk
from tkinter import messagebox
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from controller.auth_controller import AuthController
from view.main_view import MainView


class LoginView(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Login")
        self.geometry("400x400")
        self.config(bg="#f0f0f0")
        self.auth_controller = AuthController()
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
        title_label = tk.Label(
            self, text="Acessar Sistema", font=("Helvetica", 16), bg="#f0f0f0"
        )
        title_label.pack(pady=15)

        tk.Label(self, text="Email:", bg="#f0f0f0", font=("Helvetica", 12)).pack(pady=5)
        self.entry_email = tk.Entry(self, font=("Helvetica", 12), width=30)
        self.entry_email.pack(pady=5)

        tk.Label(self, text="Senha:", bg="#f0f0f0", font=("Helvetica", 12)).pack(pady=5)
        self.entry_senha = tk.Entry(self, show="*", font=("Helvetica", 12), width=30)
        self.entry_senha.pack(pady=5)

        btn_login = tk.Button(
            self,
            text="Entrar",
            command=self.login,
            bg="#007acc",
            fg="#ffffff",
            font=("Helvetica", 12),
            width=15,
        )
        btn_login.pack(pady=15)

        btn_register = tk.Button(
            self,
            text="Registrar",
            command=self.abrir_tela_cadastro,
            bg="#41dc8e",
            fg="#007acc",
            font=("Helvetica", 12),
            width=15,
        )
        btn_register.pack(pady=15)

    def login(self):
        email = self.entry_email.get()
        senha = self.entry_senha.get()
        sucesso, msg = self.auth_controller.login(email, senha)
        if sucesso:
            messagebox.showinfo("Sucesso", msg)
            self.destroy()
            MainView()
        else:
            messagebox.showerror("Erro", msg)

    def abrir_tela_cadastro(self):
        self.destroy()
        RegisterView()
import sys
import os


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from view.register_view import RegisterView 
if __name__ == "__main__":
    app = LoginView()
    app.mainloop()
