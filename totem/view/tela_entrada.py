import tkinter as tk
from controller.controlador_entrada import ControladorEntrada

class TelaEntrada(tk.Tk):
    """
    Interface gráfica para entrada de veículos no estacionamento.
    """
    def __init__(self):
        super().__init__()
        self.title("Entrada de Veículos")
        self.configure(bg="black")
        self._centralizar_janela(500, 400)

        self.controlador = ControladorEntrada()

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
        tk.Label(self, text="\U0001F697 Bem-vindo ao Estacionamento", font=("Arial", 18, "bold"), bg="black", fg="white").pack(pady=30)

        tk.Button(
            self,
            text="Gerar Ticket",
            font=("Arial", 14, "bold"),
            command=self._gerar_ticket,
            bg="green",
            fg="white",
            width=20,
            height=3
        ).pack(pady=30)

        self.resultado = tk.Label(self, text="", font=("Arial", 12), bg="black", fg="white")
        self.resultado.pack(pady=10)

        tk.Button(
            self,
            text="Voltar",
            font=("Arial", 12),
            command=self.destroy,
            bg="red",
            fg="white",
            width=10
        ).pack(pady=20)

    def _gerar_ticket(self):
        ticket = self.controlador.gerar_ticket()
        self.resultado.config(
            text=f"Ticket: {ticket.ticket_id}\nPlaca: {ticket.placa}\nEntrada: {ticket.hora_entrada}"
        )

    def _limpar_tela(self):
        for widget in self.winfo_children():
            widget.destroy()
