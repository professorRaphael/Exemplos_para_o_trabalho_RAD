import tkinter as tk
from tkinter import ttk, messagebox
from controllers import HRController

class HRView:
    def __init__(self, root: tk.Tk, controller: HRController):
        self.root = root
        self.controller = controller
        
        self.root.title("HR-Valida | Onboarding Offline")
        self.root.geometry("650x650")
        
        # Variáveis
        self.var_nome = tk.StringVar()
        self.var_cpf = tk.StringVar()
        self.var_email = tk.StringVar()
        self.var_tel = tk.StringVar()
        self.var_data = tk.StringVar()
        
        self._construir_ui()
        self._atualizar_grid()

    def _construir_ui(self):
        # Formulário
        frame_form = tk.LabelFrame(self.root, text=" Pré-Cadastro de Candidato ", font=("Helvetica", 10, "bold"), padx=20, pady=15)
        frame_form.pack(fill="x", padx=20, pady=15)

        tk.Label(frame_form, text="Nome Completo:").grid(row=0, column=0, sticky="w", pady=5)
        tk.Entry(frame_form, textvariable=self.var_nome, width=40).grid(row=0, column=1, pady=5)

        tk.Label(frame_form, text="CPF:").grid(row=1, column=0, sticky="w", pady=5)
        tk.Entry(frame_form, textvariable=self.var_cpf, width=40).grid(row=1, column=1, pady=5)

        tk.Label(frame_form, text="E-mail Corporativo:").grid(row=2, column=0, sticky="w", pady=5)
        tk.Entry(frame_form, textvariable=self.var_email, width=40).grid(row=2, column=1, pady=5)

        tk.Label(frame_form, text="Celular:").grid(row=3, column=0, sticky="w", pady=5)
        tk.Entry(frame_form, textvariable=self.var_tel, width=40).grid(row=3, column=1, pady=5)

        tk.Label(frame_form, text="Data de Nascimento:").grid(row=4, column=0, sticky="w", pady=5)
        tk.Entry(frame_form, textvariable=self.var_data, width=40).grid(row=4, column=1, pady=5)

        # Rótulo Dinâmico para Mensagens (Feedback de Validação)
        self.lbl_feedback = tk.Label(frame_form, text="Aguardando inserção...", fg="gray", font=("Helvetica", 9, "bold"))
        self.lbl_feedback.grid(row=5, column=0, columnspan=2, pady=10)

        # Botão
        tk.Button(frame_form, text="Validar Dados e Salvar", bg="#0052cc", fg="white", font=("Helvetica", 10, "bold"), command=self._submeter_dados).grid(row=6, column=0, columnspan=2, pady=10, sticky="we")

        # Tabela (Treeview)
        frame_grid = tk.LabelFrame(self.root, text=" Cadastros Aprovados Hoje ", font=("Helvetica", 10, "bold"), padx=10, pady=10)
        frame_grid.pack(fill="both", expand=True, padx=20, pady=5)

        self.tabela = ttk.Treeview(frame_grid, columns=("nome", "cpf", "email"), show="headings")
        self.tabela.heading("nome", text="Nome")
        self.tabela.heading("cpf", text="CPF")
        self.tabela.heading("email", text="E-mail")
        self.tabela.column("cpf", width=120)
        self.tabela.pack(fill="both", expand=True)

    def _submeter_dados(self):
        # Monta o Dicionário Bruto
        dados = {
            "nome": self.var_nome.get(),
            "cpf": self.var_cpf.get(),
            "email": self.var_email.get(),
            "telefone": self.var_tel.get(),
            "data_nasc": self.var_data.get()
        }

        # Envia para o Controller
        sucesso, mensagem = self.controller.processar_cadastro(dados)

        if sucesso:
            self.lbl_feedback.config(text=mensagem, fg="green")
            self._limpar_campos()
            self._atualizar_grid()
        else:
            self.lbl_feedback.config(text=f"❌ {mensagem}", fg="red")

    def _atualizar_grid(self):
        for row in self.tabela.get_children():
            self.tabela.delete(row)
        for cand in self.controller.obter_cadastros():
            self.tabela.insert("", "end", values=cand)

    def _limpar_campos(self):
        self.var_nome.set("")
        self.var_cpf.set("")
        self.var_email.set("")
        self.var_tel.set("")
        self.var_data.set("")