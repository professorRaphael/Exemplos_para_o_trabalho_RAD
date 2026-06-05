import logging
from datetime import datetime
import sqlite3
from models.producao_model import ProducaoModel
from core.exceptions import BusinessError, LoteDuplicadoError, DatabaseConnectionError

# Configuração do Logger do sistema
logger = logging.getLogger(__name__)

class ProducaoController:
    def __init__(self, model: ProducaoModel):
        self.model = model

    def registrar_saida(self, lote: str, operador: str, qtd_str: str, status: str, motivo: str):
        """Processa as regras de negócio, valida os dados e envia para o Model."""
        lote = lote.strip().upper()
        operador = operador.strip()
        motivo = motivo.strip() if status == "Reprovado" else None

        # Validações de Entrada básica
        if not lote or not operador or not qtd_str:
            raise BusinessError("Todos os campos obrigatórios devem ser preenchidos.")

        try:
            quantidade = int(qtd_str)
            if quantidade <= 0:
                raise ValueError()
        except ValueError:
            raise BusinessError("A quantidade deve ser um número inteiro estritamente positivo.")

        if status == "Reprovado" and not motivo:
            raise BusinessError("Lotes reprovados exigem a justificativa do defeito.")

        # Validação de Regra de Negócio (Duplicidade)
        try:
            if self.model.lote_existe(lote):
                raise LoteDuplicadoError(f"O lote operacional '{lote}' já consta no sistema.")
        except DatabaseConnectionError:
            raise

        # Processamento de Data e Persistência
        data_atual = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        
        try:
            self.model.salvar(lote, operador, quantidade, status, motivo, data_atual)
            logger.info(f"Sucesso: Lote {lote} registrado pelo operador {operador} (Qtd: {quantidade} | Status: {status}).")
        except sqlite3.IntegrityError:
            raise LoteDuplicadoError(f"Concorrência detectada: O lote '{lote}' já foi inserido.")
        except DatabaseConnectionError:
            raise

    def obter_historico(self):
        """Busca dados para atualizar a View."""
        return self.model.listar_ultimos_registros()