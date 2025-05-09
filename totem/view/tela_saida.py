import tkinter as tk
from tkinter import messagebox
from datetime import datetime
from model import persistencia
from model.ticket import Ticket

class TelaSaida(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Totem de Saída")
        self.configure(bg="black")
        self._centralizar_janela(500, 400)

        self._criar_interface()

    def _centralizar_janela(self, largura, altura):
        self.geometry(f"{largura}x{altura}")
        self.update_idletasks()
        largura_tela = self.winfo_screenwidth()
        altura_tela = self.winfo_screenheight()
        x = (largura_tela // 2) - (largura // 2)
        y = (altura_tela // 2) - (altura // 2)
        self.geometry(f"+{x}+{y}")

    def _criar_interface(self):
        self._limpar_tela()
        tk.Label(self, text="\U0001F6AA Verificação de Saída", font=("Arial", 18, "bold"), bg="black", fg="white").pack(pady=30)

        tk.Label(self, text="Digite o código do ticket:", font=("Arial", 14), bg="black", fg="white").pack(pady=10)

        self.entry_ticket = tk.Entry(self, font=("Arial", 16), justify="center")
        self.entry_ticket.pack(pady=10)

        tk.Button(
            self,
            text="Verificar Saída",
            font=("Arial", 14, "bold"),
            command=self._verificar_saida,
            bg="green",
            fg="white",
            width=18,
            height=2
        ).pack(pady=20)

        tk.Button(
            self,
            text="Voltar",
            font=("Arial", 12),
            command=self.destroy,
            bg="red",
            fg="white",
            width=10
        ).pack(pady=10)

    def _verificar_saida(self):
        codigo = self.entry_ticket.get().strip().upper()
        tickets = persistencia.carregar_tickets()
        for t in tickets:
            if t.ticket_id.upper() == codigo and t.pago == "sim":
                liberado_ate = datetime.strptime(t.liberado_ate, "%Y-%m-%d %H:%M:%S")
                agora = datetime.now()
                if agora <= liberado_ate:
                    messagebox.showinfo("Saída autorizada", "Saída liberada com sucesso. Obrigado!")
                    self.entry_ticket.get().delete(0, tk.END)
                else:
                    messagebox.showwarning("Tempo expirado", "Tempo de tolerância expirado. Favor dirigir-se ao totem.")
                return

        messagebox.showerror("Ticket inválido", "Ticket não encontrado ou não pago.")

    def _limpar_tela(self):
        for widget in self.winfo_children():
            widget.destroy()
