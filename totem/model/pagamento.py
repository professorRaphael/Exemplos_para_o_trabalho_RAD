from datetime import datetime, timedelta
from typing import Tuple
from model.ticket import Ticket


def calcular_valor(t_min: int) -> Tuple[float, int]:
    """
    Retorna o valor a pagar e a tolerância de saída.
    """
    match t_min:
        case t_min if t_min <= 15:
            return 5.0, 15
        case t_min if t_min <= 30:
            return 8.0, 15
        case t_min if t_min <= 60:
            return 12.0, 20
        case t_min if t_min <= 120:
            return 18.0, 20
        case _:
            return 25.0, 30


def processar_pagamento(ticket: Ticket, metodo: str) -> Ticket:
    """
    Processa o pagamento, preenche os campos do ticket e retorna o ticket atualizado.
    """
    tempo = ticket.calcular_permanencia()
    valor, tolerancia = calcular_valor(tempo)
    agora = datetime.now()

    ticket.pago = "sim"
    ticket.valor = f"{valor:.2f}"
    ticket.hora_pagamento = agora.strftime("%Y-%m-%d %H:%M:%S")
    ticket.liberado_ate = (agora + timedelta(minutes=tolerancia)).strftime("%Y-%m-%d %H:%M:%S")
    return ticket
