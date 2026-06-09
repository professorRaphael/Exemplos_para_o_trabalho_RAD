import re
from datetime import datetime

class ValidadorRegex:
    
    @staticmethod
    def validar_nome(nome: str) -> bool:
        # Exige pelo menos duas palavras (Nome e Sobrenome), apenas letras e acentos
        padrao = r"^[A-Za-záàâãéèêíïóôõöúçñÁÀÂÃÉÈÍÏÓÔÕÖÚÇÑ]+\s+[A-Za-záàâãéèêíïóôõöúçñÁÀÂÃÉÈÍÏÓÔÕÖÚÇÑ\s]+$"
        return bool(re.match(padrao, nome.strip()))

    @staticmethod
    def validar_cpf_formato(cpf: str) -> bool:
        # Aceita com ou sem pontuação
        padrao = r"^\d{3}\.?\d{3}\.?\d{3}-?\d{2}$"
        return bool(re.match(padrao, cpf.strip()))

    @staticmethod
    def validar_cpf_matematica(cpf: str) -> bool:
        """Bônus Técnico: Validação real do dígito verificador."""
        numeros = [int(digito) for digito in cpf if digito.isdigit()]
        if len(numeros) != 11 or len(set(numeros)) == 1:
            return False
        
        # Validação do 1º dígito
        soma_1 = sum(n * peso for n, peso in zip(numeros[:9], range(10, 1, -1)))
        digito_1 = (soma_1 * 10 % 11) % 10
        if numeros[9] != digito_1: return False
        
        # Validação do 2º dígito
        soma_2 = sum(n * peso for n, peso in zip(numeros[:10], range(11, 1, -1)))
        digito_2 = (soma_2 * 10 % 11) % 10
        return numeros[10] == digito_2

    @staticmethod
    def validar_email(email: str, dominio_esperado: str) -> bool:
        # Escapa o domínio para a regex e valida o formato
        dominio_escapado = re.escape(dominio_esperado)
        padrao = rf"^[a-zA-Z0-9._%+-]+{dominio_escapado}$"
        return bool(re.match(padrao, email.strip()))

    @staticmethod
    def validar_telefone(telefone: str) -> bool:
        # Formatos: (11) 98888-8888, 11988888888, (11)988888888
        padrao = r"^\(?\d{2}\)?\s?(9\d{4})-?\d{4}$"
        return bool(re.match(padrao, telefone.strip()))

    @staticmethod
    def validar_data(data_nasc: str) -> bool:
        # Regex básica para formato DD/MM/AAAA
        padrao = r"^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/\d{4}$"
        if not re.match(padrao, data_nasc.strip()):
            return False
        
        # Verificação lógica profunda (anos bissextos, meses com 30/31)
        try:
            datetime.strptime(data_nasc.strip(), "%d/%m/%Y")
            return True
        except ValueError:
            return False

    @staticmethod
    def formatar_cpf(cpf: str) -> str:
        """Limpa o CPF e formata no padrão XXX.XXX.XXX-XX para o banco."""
        apenas_numeros = re.sub(r"\D", "", cpf)
        return f"{apenas_numeros[:3]}.{apenas_numeros[3:6]}.{apenas_numeros[6:9]}-{apenas_numeros[9:]}"