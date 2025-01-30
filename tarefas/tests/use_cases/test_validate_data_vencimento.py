import pytest

from tarefas.use_cases import validate_data_vencimento


class TestValidateDataVencimento:
    @pytest.mark.parametrize(
        "data_vencimento",
        [
            "",
            "202191929",
            123,
            "202119-0212-2912",
            "2025-02-42",
        ],
    )
    def test_data_de_vencimento_invalida_resulta_em_erro_lancado(self, data_vencimento):
        with pytest.raises(ValueError):
            validate_data_vencimento(data_vencimento)

    @pytest.mark.parametrize(
        "data_vencimento",
        [
            None,
            "2025-02-12",
        ],
    )
    def test_validate_data_vencimento_deve_retornar_nada_quando_dados_validos(
        self, data_vencimento
    ):
        assert validate_data_vencimento(data_vencimento) is None
