from tarefas.models import Tarefa


STATUS_VALIDOS = {valor[0] for valor in Tarefa.STATUS_CHOICES}
