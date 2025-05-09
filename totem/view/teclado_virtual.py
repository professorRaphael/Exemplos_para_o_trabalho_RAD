import tkinter as tk
from tkinter import messagebox


class TelaTecladoVirtual(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Totem - Entrada de Placa")
        self.configure(bg="black")

        # Centraliza a janela
        self._centralizar_janela(600, 500)

        self.entrada = ""
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
        self.display = tk.Label(
            self,
            text="",
            font=("Arial", 24, "bold"),
            bg="white",
            width=16,
            height=2,
            relief="sunken"
        )
        self.display.pack(pady=10)

        teclado = [
            "1234567890",
            "QWERTYUIOP",
            "ASDFGHJKL",
            "ZXCVBNM"
        ]

        for linha in teclado:
            frame = tk.Frame(self, bg="black")
            frame.pack(pady=3)
            for char in linha:
                tk.Button(
                    frame,
                    text=char,
                    width=4,
                    height=2,
                    font=("Arial", 14),
                    command=lambda c=char: self._adicionar(c),
                    bg="#1e90ff",
                    fg="white",
                    activebackground="#4682b4"
                ).pack(side="left", padx=2)

        botoes = tk.Frame(self, bg="black")
        botoes.pack(pady=15)

        tk.Button(
            botoes,
            text="Cancelar",
            font=("Arial", 12, "bold"),
            width=10,
            height=2,
            bg="red",
            fg="white",
            command=self.destroy
        ).pack(side="left", padx=10)

        tk.Button(
            botoes,
            text="Corrigir",
            font=("Arial", 12, "bold"),
            width=10,
            height=2,
            bg="#00bfff",
            fg="white",
            command=self._corrigir
        ).pack(side="left", padx=10)

        tk.Button(
            botoes,
            text="Confirmar",
            font=("Arial", 12, "bold"),
            width=10,
            height=2,
            bg="green",
            fg="white",
            command=self._confirmar
        ).pack(side="left", padx=10)

    def _adicionar(self, char: str):
        if len(self.entrada) < 7:
            self.entrada += char
            self.display.config(text=self.entrada)

    def _corrigir(self):
        self.entrada = self.entrada[:-1]
        self.display.config(text=self.entrada)

    def _confirmar(self):
        if len(self.entrada) < 7:
            messagebox.showwarning("Placa inválida", "Digite uma placa válida com ao menos 7 caracteres.")
            return
        messagebox.showinfo("Placa recebida", f"Placa: {self.entrada}")
        self.destroy()


if __name__ == "__main__":
    app = TelaTecladoVirtual()
    app.mainloop()
