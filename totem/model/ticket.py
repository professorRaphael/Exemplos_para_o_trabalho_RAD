from datetime import datetime
from typing import Optional


class Ticket:
    """
    Representa um ticket de estacionamento.
    """

    def __init__(
        self,
        ticket_id: str,
        placa: str,
        hora_entrada: str,
        pago: str = "nao",
        hora_pagamento: Optional[str] = "",
        valor: Optional[str] = "",
        liberado_ate: Optional[str] = ""
    ):
        self.ticket_id = ticket_id
        self.placa = placa
        self.hora_entrada = hora_entrada
        self.pago = pago
        self.hora_pagamento = hora_pagamento
        self.valor = valor
        self.liberado_ate = liberado_ate

    def calcular_permanencia(self) -> int:
        """
        Retorna o tempo de permanência em minutos.
        """
        entrada = datetime.strptime(self.hora_entrada, "%Y-%m-%d %H:%M:%S")
        agora = datetime.now()
        return int((agora - entrada).total_seconds() // 60)

    def to_dict(self) -> dict:
        """
        Converte o ticket para dicionário serializável.
        """
        return {
            "ticket_id": self.ticket_id,
            "placa": self.placa,
            "hora_entrada": self.hora_entrada,
            "pago": self.pago,
            "hora_pagamento": self.hora_pagamento,
            "valor": self.valor,
            "liberado_ate": self.liberado_ate
        }

    @staticmethod
    def from_dict(d: dict) -> "Ticket":
        """
        Cria um objeto Ticket a partir de um dicionário.
        """
        return Ticket(
            ticket_id=d["ticket_id"],
            placa=d["placa"],
            hora_entrada=d["hora_entrada"],
            pago=d.get("pago", "nao"),
            hora_pagamento=d.get("hora_pagamento", ""),
            valor=d.get("valor", ""),
            liberado_ate=d.get("liberado_ate", "")
        )
