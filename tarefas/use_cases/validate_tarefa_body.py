from tarefas.common import STATUS_VALIDOS


def validate_tarefa_body(data: dict) -> None:
    """
    Valida os dados de uma tarefa.

    Args:
        data: dados da tarefa

    Raises:
        ValueError: se os dados da tarefa forem inválidos
    """
    if not data.get("titulo"):
        raise ValueError("O título da tarefa é obrigatório")

    if not data.get("status"):
        raise ValueError("O status da tarefa é obrigatório")

    if data.get("status") not in STATUS_VALIDOS:
        raise ValueError("O status da tarefa é inválido")
