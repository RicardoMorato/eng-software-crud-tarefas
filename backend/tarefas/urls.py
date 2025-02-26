from django.urls import path

from . import views

urlpatterns = [
    path("", views.tarefas_general_view),
    path("<int:tarefa_id>", views.tarefa_detail_view),
    path("<int:tarefa_id>/", views.tarefa_detail_view),
]
