import tkinter as tk
from tkinter import messagebox
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from controller.auth_controller import AuthController


class RegisterView(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Cadastro")
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
            self, text="Cadastro de Novo Usuário", font=("Helvetica", 16), bg="#f0f0f0"
        )
        title_label.pack(pady=15)

        tk.Label(self, text="Nome:", bg="#f0f0f0", font=("Helvetica", 12)).pack(pady=5)
        self.entry_nome = tk.Entry(self, font=("Helvetica", 12), width=30)
        self.entry_nome.pack(pady=5)

        tk.Label(self, text="Email:", bg="#f0f0f0", font=("Helvetica", 12)).pack(pady=5)
        self.entry_email = tk.Entry(self, font=("Helvetica", 12), width=30)
        self.entry_email.pack(pady=5)

        tk.Label(self, text="Senha:", bg="#f0f0f0", font=("Helvetica", 12)).pack(pady=5)
        self.entry_senha = tk.Entry(self, show="*", font=("Helvetica", 12), width=30)
        self.entry_senha.pack(pady=5)

        btn_register = tk.Button(
            self,
            text="Registrar",
            command=self.registrar,
            bg="#007acc",
            fg="#ffffff",
            font=("Helvetica", 12),
            width=15,
        )
        btn_register.pack(pady=15)

        btn_back = tk.Button(
            self,
            text="Voltar",
            command=self.voltar_tela_login,
            bg="#f0f0f0",
            fg="#007acc",
            font=("Helvetica", 10),
        )
        btn_back.pack()

    def registrar(self):
        nome = self.entry_nome.get()
        email = self.entry_email.get()
        senha = self.entry_senha.get()
        sucesso, msg = self.auth_controller.register(nome, email, senha)
        if sucesso:
            messagebox.showinfo("Sucesso", msg)
            self.destroy()
            LoginView()
        else:
            messagebox.showerror("Erro", msg)

    def voltar_tela_login(self):
        self.destroy()
        LoginView()


from view.login_view import LoginView
