from django.db import models


class Tarefa(models.Model):
    """
    Modelo de tarefas

    Atributos:
        - titulo: título da tarefa
        - descricao: descrição da tarefa
        - created_at: data de criação da tarefa
        - updated_at: data de atualização da tarefa
        - status: status da tarefa (pendente, realizando, concluída)
        - data_vencimento: data de vencimento da tarefa
    """

    STATUS_CHOICES = (
        ("pendente", "Pendente"),
        ("realizando", "Realizando"),
        ("concluida", "Concluída"),
    )

    titulo = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, max_length=500)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="pendente")
    data_vencimento = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.titulo} - {self.status}"

    def to_dict(self):
        return {
            "id": self.id,
            "titulo": self.titulo,
            "descricao": self.descricao,
            "status": self.status,
            "data_vencimento": self.data_vencimento,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }

    @property
    def esta_concluida(self):
        return self.status == "concluida"
