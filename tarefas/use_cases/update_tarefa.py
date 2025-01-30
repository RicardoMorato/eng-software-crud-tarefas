from typing import Optional

from tarefas.models import Tarefa


def update_tarefa(
    tarefa_to_update: Tarefa,
    titulo: str,
    descricao: Optional[str],
    data_vencimento: [str],
    status: str,
) -> Tarefa:
    """
    Atualiza uma tarefa no banco de dados.

    Args:
        tarefa_to_update: tarefa a ser atualizada
        titulo: título da tarefa
        descricao: descrição da tarefa
        data_vencimento: data de vencimento da tarefa
        status: status da tarefa (pendente, realizando, concluída)

    Returns:
        Tarefa atualizada
    """
    tarefa_to_update.titulo = titulo
    tarefa_to_update.status = status

    if descricao:
        tarefa_to_update.descricao = descricao

    if data_vencimento:
        tarefa_to_update.data_vencimento = data_vencimento

    tarefa_to_update.save()

    return tarefa_to_update
