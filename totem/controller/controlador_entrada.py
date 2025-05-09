import uuid
import random
import string
from datetime import datetime
from model.ticket import Ticket
from model import persistencia


class ControladorEntrada:
    """
    Controlador responsável pela entrada de veículos e geração de ticket.
    """

    def gerar_ticket(self) -> Ticket:
        ticket_id = str(uuid.uuid4())[:8].upper()
        placa = self._gerar_placa_aleatoria()
        hora_entrada = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        ticket = Ticket(
            ticket_id=ticket_id,
            placa=placa,
            hora_entrada=hora_entrada
        )

        tickets = persistencia.carregar_tickets()
        tickets.append(ticket)
        persistencia.salvar_tickets(tickets)
        persistencia.registrar_log(f"Ticket gerado: {ticket_id} - Placa: {placa}")
        return ticket

    @staticmethod
    def _gerar_placa_aleatoria() -> str:
        letras = ''.join(random.choices(string.ascii_uppercase, k=3))
        numeros = ''.join(random.choices(string.digits, k=4))
        return f"{letras}{numeros}"
