class HttpConflictError(Exception):
    """Exceção para conflitos HTTP (409 Conflict)."""

    def __init__(self, message: str = "Conflict error", status_code: int = 409):
        """
        Inicializa a exceção com uma mensagem e código de status HTTP.
        
        :param message: Mensagem descritiva do erro.
        :param status_code: Código de status HTTP associado (padrão: 409).
        """
        super().__init__(message)
        self.message = message
        self.status_code = status_code

    def to_dict(self) -> dict:
        """Converte a exceção para um dicionário, útil para respostas JSON."""
        return {"error": self.message, "status_code": self.status_code}
