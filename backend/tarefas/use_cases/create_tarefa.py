from typing import Optional

from tarefas.models import Tarefa


def create_tarefa(
    titulo: str, descricao: Optional[str], data_vencimento: Optional[str], status: str
) -> Tarefa:
    """
    Cria uma tarefa no banco de dados.

    Args:
        titulo: título da tarefa
        descricao: descrição da tarefa
        data_vencimento: data de vencimento da tarefa
        status: status da tarefa (pendente, realizando, concluída)

    Returns:
        Tarefa criada
    """
    tarefa = Tarefa.objects.create(
        titulo=titulo,
        descricao=descricao,
        data_vencimento=data_vencimento,
        status=status,
    )

    return tarefa
