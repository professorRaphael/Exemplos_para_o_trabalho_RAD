class BusinessError(Exception):
    """Exceção base para erros de regra de negócio."""
    pass

class LoteDuplicadoError(BusinessError):
    """Lançada quando o lote já existe no banco de dados."""
    pass

class DatabaseConnectionError(Exception):
    """Lançada quando há uma falha crítica de conexão com o SQLite."""
    pass