import logging
import json

from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_http_methods

from tarefas.common import STATUS_VALIDOS
from tarefas.models import Tarefa
from tarefas.use_cases import (
    validate_tarefa_body,
    create_tarefa as create_tarefa_use_case,
    validate_data_vencimento,
    update_tarefa as update_tarefa_use_case,
)


LOGGER = logging.getLogger(__name__)


def get_tarefas(request):
    status_filter = request.GET.get("status", None)

    tarefas = Tarefa.objects.all()

    if status_filter and status_filter in STATUS_VALIDOS:
        tarefas = tarefas.filter(status=status_filter)

    return JsonResponse([tarefa.to_dict() for tarefa in tarefas], safe=False)


def create_tarefa(request):
    body_data = request.body.decode("utf-8")
    data = json.loads(body_data)

    try:
        validate_tarefa_body(data)

        validate_data_vencimento(data.get("data_vencimento", None))
    except ValueError as error:
        LOGGER.error("Erro ao validar dados da tarefa: %s", error)
        return JsonResponse(
            {"erro": "Erro ao validar os dados da tarefa", "detalhe": str(error)},
            status=400,
        )

    titulo = data.get("titulo")
    descricao = data.get("descricao")
    data_vencimento = data.get("data_vencimento")
    status = data.get("status")

    tarefa = create_tarefa_use_case(titulo, descricao, data_vencimento, status)

    return JsonResponse(tarefa.to_dict(), status=201)


def update_tarefa(request, tarefa: Tarefa):
    body_data = request.body.decode("utf-8")
    data = json.loads(body_data)

    try:
        # Essa etapa de validação está sendo repetida em create_tarefa e update_tarefa
        # Poderíamos criar um validador genérico para ser usado em ambos os casos
        # No entanto, como a validação é simples e não será reutilizada novamente, não acho que seja necessário
        # Seria um caso de otimização prematura, um anti-pattern
        validate_tarefa_body(data)

        validate_data_vencimento(data.get("data_vencimento", None))
    except ValueError as error:
        LOGGER.error("Erro ao validar dados da tarefa: %s", error)
        return JsonResponse(
            {"erro": "Erro ao validar os dados da tarefa", "detalhe": str(error)},
            status=400,
        )

    titulo = data.get("titulo")
    descricao = data.get("descricao")
    data_vencimento = data.get("data_vencimento")
    status = data.get("status")

    updated_tarefa = update_tarefa_use_case(
        tarefa, titulo, descricao, data_vencimento, status
    )

    return JsonResponse(updated_tarefa.to_dict(), status=200)


# O ideal seria usar o Django Rest Framework para criar uma API RESTful
# Mas não é o foco do desafio, por isso segui esse método mais simples
@require_http_methods(["GET", "POST"])
def tarefas_general_view(request):
    if request.method == "GET":
        return get_tarefas(request)
    elif request.method == "POST":
        return create_tarefa(request)
    else:
        return HttpResponse(status=405)


@require_http_methods(["GET", "PUT", "DELETE"])
def tarefa_detail_view(request, tarefa_id):
    try:
        tarefa = Tarefa.objects.get(id=tarefa_id)
    except Tarefa.DoesNotExist:
        return JsonResponse(
            {
                "erro": "Erro ao processar requisição",
                "detalhe": "Tarefa não encontrada",
            },
            status=404,
        )

    if request.method == "GET":
        return JsonResponse(tarefa.to_dict())
    elif request.method == "PUT":
        return update_tarefa(request, tarefa)
    elif request.method == "DELETE":
        # Poderíamos criar um use case para deletar uma tarefa, mas é uma operação simples
        # Seria útil se tivéssemos mais regras de negócio envolvidas, como autorização de usuários e etc
        # Como não é o caso, sigo com a forma mais simples
        tarefa.delete()
        return HttpResponse(status=204)
    else:
        return HttpResponse(status=405)
