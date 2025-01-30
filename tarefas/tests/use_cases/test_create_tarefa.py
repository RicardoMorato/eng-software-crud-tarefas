import pytest

from tarefas.models import Tarefa
from tarefas.use_cases import create_tarefa


@pytest.mark.django_db
class TestCreateTarefa:
    def test_cria_tarefa_no_banco_quando_dados_validos(self):
        # Arrange
        tarefa_body = {
            "titulo": "Título da tarefa",
            "descricao": "Descrição da tarefa",
            "status": "pendente",
            "data_vencimento": None,
        }

        # Act
        tarefa_criada = create_tarefa(**tarefa_body)

        # Assert
        assert tarefa_criada.titulo == tarefa_body["titulo"]
        assert tarefa_criada.descricao == tarefa_body["descricao"]
        assert tarefa_criada.status == tarefa_body["status"]
        assert tarefa_criada.data_vencimento is None
        assert tarefa_criada.id is not None
        assert tarefa_criada.created_at is not None
        assert tarefa_criada.updated_at is not None

        assert Tarefa.objects.filter(id=tarefa_criada.id).exists()
