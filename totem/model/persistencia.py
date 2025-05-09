import os
from pathlib import Path
import json
import logging
from typing import List
from model.ticket import Ticket

DATA_DIR = "data"
TICKETS_FILE = Path(__file__).resolve().parent / DATA_DIR / "tickets.json"
LOG_FILE = Path(__file__).resolve().parent / DATA_DIR / "log_estacionamento.log"
COMPROVANTES_DIR = Path(__file__).resolve().parent / DATA_DIR / "comprovantes"
'''TICKETS_FILE = os.path.join(DATA_DIR, "tickets.json")
LOG_FILE = os.path.join(DATA_DIR, "log_estacionamento.log")
COMPROVANTES_DIR = os.path.join(DATA_DIR, "comprovantes")'''

os.makedirs(COMPROVANTES_DIR, exist_ok=True)

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    encoding="utf-8"
)

def carregar_tickets() -> List[Ticket]:
    if not os.path.exists(TICKETS_FILE):
        return []
    with open(TICKETS_FILE, "r", encoding="utf-8") as f:
        dados = json.load(f)
    return [Ticket.from_dict(t) for t in dados]

def salvar_tickets(tickets: List[Ticket]) -> None:
    with open(TICKETS_FILE, "w", encoding="utf-8") as f:
        json.dump([t.to_dict() for t in tickets], f, indent=4, ensure_ascii=False)

def registrar_log(msg: str) -> None:
    logging.info(msg)

def gerar_comprovante(ticket: Ticket, metodo: str) -> None:
    caminho = os.path.join(COMPROVANTES_DIR, f"comprovante_{ticket.ticket_id}.txt")
    try:
        with open(caminho, "w", encoding="utf-8") as f:
            f.write("\t\t\t\tESTACIONAMENTO CENTRAL\n")
            f.write("\t\t\t\tCNPJ: 12.345.678/0001-99\n")
            f.write("\t\tAv. das Garagens, 123 - Centro\n")
            f.write("\t\t\t\tTel: (21) 99999-0000\n\n")
            f.write("-" * 31 + "\n")
            f.write(f"TICKET: {ticket.ticket_id}\n")
            f.write(f"PLACA: {ticket.placa}\n\n")
            f.write(f"ENTRADA: {ticket.hora_entrada}\n")
            f.write(f"PAGAMENTO: {ticket.hora_pagamento}\n\n")
            f.write(f"VALOR PAGO:       R$ {ticket.valor}\n")
            f.write(f"LIBERADO ATÉ: {ticket.liberado_ate}\n")
            f.write("-" * 31 + "\n\n")
            f.write(f"Pagamento via: {metodo}\n")
            f.write("Terminal: TOTEM-01\n\n")
            f.write("Obrigado por utilizar nossos serviços!\n")
    except Exception as e:
        logging.error(f"Erro ao gerar comprovante: {e}")
