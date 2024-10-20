from db.database import Database
from model.user import User


class AuthController:
    def __init__(self):
        self.db = Database()

    def login(self, email, senha):
        """Verifica se as credenciais são válidas no banco de dados"""
        user = self.db.buscar_usuario_por_email(email)
        if user and user.senha == senha:
            return True, "Login realizado com sucesso!"
        return False, "Email ou senha incorretos!"

    def register(self, nome, email, senha):
        """Registra um novo usuário no banco de dados"""
        user_existente = self.db.buscar_usuario_por_email(email)
        if user_existente:
            return False, "Email já registrado!"
        novo_usuario = User(nome=nome, email=email, senha=senha)
        self.db.inserir_usuario(novo_usuario)
        return True, "Usuário registrado com sucesso!"
