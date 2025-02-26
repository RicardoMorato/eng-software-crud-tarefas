from datetime import datetime
from typing import Optional


def validate_data_vencimento(data_vencimento: Optional[str]) -> None:
    """
    Valida a data de vencimento de uma tarefa.

    Args:
        data_vencimento: data de vencimento da tarefa

    Raises:
        ValueError: se a data de vencimento for inválida
    """
    if isinstance(data_vencimento, str) and not data_vencimento:
        # Se a data de vencimento for uma string vazia, retornamos um erro
        raise ValueError("A data de vencimento é inválida")

    if not data_vencimento:
        # A data de vencimento é opcional, então se não for passada, podemos retornar
        return

    try:
        datetime.strptime(data_vencimento, "%Y-%m-%d")
    except (ValueError, TypeError):
        raise ValueError("A data de vencimento é inválida")
