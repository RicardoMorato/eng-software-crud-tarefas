import pytest

from tarefas.use_cases import validate_tarefa_body


class TestValidateTarefaBody:
    @pytest.mark.parametrize(
        "data",
        [
            {"titulo": "Teste", "status": "pendente"},
            {"titulo": "Teste", "descricao": "descricao teste", "status": "pendente"},
            {
                "titulo": "Título",
                "descricao": "Descrição",
                "status": "concluida",
                "data_vencimento": "2025-02-12",
            },
        ],
    )
    def test_validate_tarefa_body_deve_retornar_nada_quando_dados_validos(self, data):
        assert validate_tarefa_body(data) is None

    @pytest.mark.parametrize(
        "data",
        [
            {},  # dados vazios
            {"titulo": "Título da tarefa", "status": ""},  # status é obrigatório
            {"titulo": "Título da tarefa", "status": "invalido"},  # status inválido
            {"titulo": "", "status": "pendente"},  # título é obrigatório
            {"status": "pendente"},  # título é obrigatório
            {"titulo": "Título da tarefa"},  # status é obrigatório
        ],
    )
    def test_validate_tarefa_body_deve_retornar_excecao_quando_dados_invalidos(
        self, data
    ):
        with pytest.raises(ValueError):
            validate_tarefa_body(data)
