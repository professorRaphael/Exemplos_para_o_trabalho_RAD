import sqlite3
from config import EMPRESA_DOMINIO
from validators import ValidadorRegex
from models import DatabaseModel

class HRController:
    def __init__(self, model: DatabaseModel):
        self.model = model

    def processar_cadastro(self, dados: dict) -> tuple[bool, str]:
        # Extração
        nome = dados.get("nome", "")
        cpf = dados.get("cpf", "")
        email = dados.get("email", "")
        tel = dados.get("telefone", "")
        data_nasc = dados.get("data_nasc", "")

        # Fluxo de Validação
        if not ValidadorRegex.validar_nome(nome):
            return False, "Nome inválido. Insira nome e sobrenome (sem números)."
            
        if not ValidadorRegex.validar_cpf_formato(cpf):
            return False, "Formato de CPF inválido."
            
        if not ValidadorRegex.validar_cpf_matematica(cpf):
            return False, "CPF matematicamente inválido."
            
        if not ValidadorRegex.validar_email(email, EMPRESA_DOMINIO):
            return False, f"E-mail inválido. Obrigatório uso do domínio {EMPRESA_DOMINIO}"
            
        if not ValidadorRegex.validar_telefone(tel):
            return False, "Telefone inválido. Use (XX) 9XXXX-XXXX."
            
        if not ValidadorRegex.validar_data(data_nasc):
            return False, "Data inválida ou formato incorreto (DD/MM/AAAA)."

        # Sanitização de Dados para o Banco
        nome_limpo = nome.strip().title()
        cpf_formatado = ValidadorRegex.formatar_cpf(cpf)
        
        # Tenta persistir
        try:
            self.model.inserir_candidato(nome_limpo, cpf_formatado, email.strip().lower(), tel, data_nasc)
            return True, "Candidato cadastrado e validado com sucesso!"
        except sqlite3.IntegrityError:
            return False, "Erro: Este CPF já consta na base de dados (Candidato Duplicado)."
        except Exception as e:
            return False, f"Erro interno do banco: {str(e)}"

    def obter_cadastros(self):
        return self.model.buscar_cadastros_recentes()