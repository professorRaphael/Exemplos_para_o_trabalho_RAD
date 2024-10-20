from dataclasses import dataclass


@dataclass
class User:
    nome: str
    email: str
    senha: str
