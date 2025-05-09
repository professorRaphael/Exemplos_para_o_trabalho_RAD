from typing import Optional
from model.ticket import Ticket
from model import persistencia
from model import pagamento


class ControladorTotem:
    """
    Classe controladora responsável por intermediar a View e os Models.
    """

    def __init__(self):
        self.tickets = persistencia.carregar_tickets()

    def buscar_ticket_valido(self, ticket_id: str) -> Optional[Ticket]:
        """
        Busca o ticket com o ID fornecido e verifica se ainda não foi pago.
        """
        for ticket in self.tickets:
            if ticket.ticket_id.upper() == ticket_id.upper() and ticket.pago == "nao":
                return ticket
        return None

    def realizar_pagamento(self, ticket: Ticket, metodo: str) -> Ticket:
        """
        Processa o pagamento, salva o ticket atualizado e gera comprovante.
        """
        ticket = pagamento.processar_pagamento(ticket, metodo)
        self._atualizar_ticket(ticket)
        persistencia.salvar_tickets(self.tickets)
        persistencia.gerar_comprovante(ticket, metodo)
        persistencia.registrar_log(
            f"Pagamento {metodo} registrado para ticket {ticket.ticket_id} - R$ {ticket.valor}"
        )
        return ticket

    def _atualizar_ticket(self, ticket_atualizado: Ticket) -> None:
        """
        Substitui o ticket na lista interna pela versão atualizada.
        """
        for i, t in enumerate(self.tickets):
            if t.ticket_id == ticket_atualizado.ticket_id:
                self.tickets[i] = ticket_atualizado
                break
            