import tkinter as tk
from tkinter import ttk, messagebox
from controllers.producao_controller import ProducaoController
from core.exceptions import BusinessError, DatabaseConnectionError

class ProducaoView:
    def __init__(self, root: tk.Tk, controller: ProducaoController):
        self.root = root
        self.controller = controller
        
        self.root.title("ProCheck Industrial")
        self.root.geometry("780x620")
        
        # Elementos observáveis do Tkinter (Váriaveis de Controle)
        self.var_lote = tk.StringVar()
        self.var_operador = tk.StringVar()
        self.var_qtd = tk.StringVar()
        self.var_status = tk.StringVar(value="Aprovado")
        self.var_motivo = tk.StringVar()

        self._desenhar_layout()
        self._atualizar_grid_dados()

    def _desenhar_layout(self):
        # Painel do Formulário
        frame_form = tk.LabelFrame(self.root, text=" Checkout de Lote Industrial ", font=("Arial", 11, "bold"), padx=15, pady=15)
        frame_form.pack(fill="x", padx=15, pady=10)

        tk.Label(frame_form, text="Código do Lote (Bipagem):", font=("Arial", 10)).grid(row=0, column=0, sticky="w", pady=5)
        self.input_lote = tk.Entry(frame_form, textvariable=self.var_lote, font=("Arial", 11), width=30)
        self.input_lote.grid(row=0, column=1, pady=5, padx=5)
        self.input_lote.focus_set()

        tk.Label(frame_form, text="Operador Logístico:", font=("Arial", 10)).grid(row=1, column=0, sticky="w", pady=5)
        tk.Entry(frame_form, textvariable=self.var_operador, font=("Arial", 11), width=30).grid(row=1, column=1, pady=5, padx=5)

        tk.Label(frame_form, text="Quantidade de Peças:", font=("Arial", 10)).grid(row=2, column=0, sticky="w", pady=5)
        tk.Entry(frame_form, textvariable=self.var_qtd, font=("Arial", 11), width=10).grid(row=2, column=1, sticky="w", pady=5, padx=5)

        tk.Label(frame_form, text="Controle de Qualidade:", font=("Arial", 10)).grid(row=3, column=0, sticky="w", pady=5)
        frame_radio = tk.Frame(frame_form)
        frame_radio.grid(row=3, column=1, sticky="w", pady=5)
        
        tk.Radiobutton(frame_radio, text="Aprovado", variable=self.var_status, value="Aprovado", command=self._evento_mudanca_status).pack(side="left", padx=5)
        tk.Radiobutton(frame_radio, text="Reprovado", variable=self.var_status, value="Reprovado", command=self._evento_mudanca_status).pack(side="left", padx=5)

        tk.Label(frame_form, text="Motivo do Defeito / Refugo:", font=("Arial", 10)).grid(row=4, column=0, sticky="w", pady=5)
        self.entry_motivo = tk.Entry(frame_form, textvariable=self.var_motivo, font=("Arial", 11), width=40, state="disabled")
        self.entry_motivo.grid(row=4, column=1, sticky="w", pady=5, padx=5)

        btn_registrar = tk.Button(frame_form, text="REGISTRAR SAÍDA", bg="#27ae60", fg="white", font=("Arial", 10, "bold"), padx=15, command=self._processar_registro)
        btn_registrar.grid(row=5, column=1, sticky="e", pady=10)

        # Atalhos Globais
        self.root.bind('<Return>', lambda event: self._processar_registro())

        # Painel Histórico (Treeview)
        frame_tabela = tk.LabelFrame(self.root, text=" Monitoramento em Tempo Real (Últimos 10 Lotes) ", font=("Arial", 11, "bold"), padx=10, pady=10)
        frame_tabela.pack(fill="both", expand=True, padx=15, pady=5)

        colunas = ("lote", "operador", "qtd", "status", "data")
        self.tabela = ttk.Treeview(frame_tabela, columns=colunas, show="headings")
        self.tabela.heading("lote", text="Cód. Lote")
        self.tabela.heading("operador", text="Operador")
        self.tabela.heading("qtd", text="Qtd")
        self.tabela.heading("status", text="Qualidade")
        self.tabela.heading("data", text="Timestamp")
        self.tabela.column("qtd", width=80, anchor="center")
        self.tabela.column("status", width=120, anchor="center")
        self.tabela.pack(fill="both", expand=True)

    def _evento_mudanca_status(self):
        if self.var_status.get() == "Reprovado":
            self.entry_motivo.config(state="normal")
            self.entry_motivo.focus_set()
        else:
            self.var_motivo.set("")
            self.entry_motivo.config(state="disabled")

    def _processar_registro(self):
        try:
            # Captura dados da View e envia ao controller
            self.controller.registrar_saida(
                lote=self.var_lote.get(),
                operador=self.var_operador.get(),
                qtd_str=self.var_qtd.get(),
                status=self.var_status.get(),
                motivo=self.var_motivo.get()
            )
            
            # Se deu certo, atualiza a interface e limpa o form
            self._atualizar_grid_dados()
            self._limpar_formulario()
            
        except BusinessError as e:
            # Erros previsíveis de validação ou de lógica de negócios
            messagebox.showwarning("Validação de Processo", str(e))
        except DatabaseConnectionError as e:
            # Erros de infraestrutura local crísticos
            messagebox.showerror("Erro Crítico de Infraestrutura", f"{e}\nO terminal operará em modo de espera de sincronização.")
        except Exception as e:
            # Captura de falhas não mapeadas para proteção do app
            messagebox.showerror("Erro Inesperado", "Contate o suporte técnico de TI.")

    def _atualizar_grid_dados(self):
        for r in self.tabela.get_children():
            self.tabela.delete(r)
        for registro in self.controller.obter_historico():
            self.tabela.insert("", "end", values=registro)

    def _limpar_formulario(self):
        self.var_lote.set("")
        self.var_qtd.set("")
        self.var_motivo.set("")
        self.var_status.set("Aprovado")
        self.entry_motivo.config(state="disabled")
        self.input_lote.focus_set()