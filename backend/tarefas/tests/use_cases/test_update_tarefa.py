from datetime import datetime
import pytest
from tarefas.models import Tarefa
from tarefas.use_cases import update_tarefa


@pytest.mark.django_db
class TestUpdateTarefa:
    def test_atualiza_tarefa_no_banco_quando_dados_validos(self):
        # Arrange
        tarefa = Tarefa.objects.create(
            titulo="Título da tarefa",
            descricao="Descrição da tarefa",
            status="pendente",
            data_vencimento=None,
        )

        tarefa_body = {
            "titulo": "Título atualizado",
            "descricao": "Descrição atualizada",
            "status": "concluida",
            "data_vencimento": "2025-02-12",
        }

        # Act
        tarefa_atualizada = update_tarefa(tarefa, **tarefa_body)

        # Assert
        assert tarefa_atualizada.titulo == tarefa_body["titulo"]
        assert tarefa_atualizada.descricao == tarefa_body["descricao"]
        assert tarefa_atualizada.status == tarefa_body["status"]
        assert tarefa_atualizada.data_vencimento == str(datetime(2025, 2, 12).date())
        assert tarefa_atualizada.id == tarefa.id
        assert tarefa_atualizada.updated_at > tarefa.created_at

        assert Tarefa.objects.filter(id=tarefa.id).exists()
        assert Tarefa.objects.filter(
            id=tarefa.id,
            titulo=tarefa_body["titulo"],
            descricao=tarefa_body["descricao"],
            status=tarefa_body["status"],
            data_vencimento=tarefa_body["data_vencimento"],
        ).exists()
