from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('detalhes/<int:id>', views.detalhes, name='detalhes_evento'),
    path('excluir/<int:id>', views.excluir, name='excluir_evento'),
    path('adicionar-eventos/', views.criar_eventos, name='adicionar_eventos'),
#

]