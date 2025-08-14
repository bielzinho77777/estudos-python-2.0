from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('compromissos/', views.compromissos, name='compromissos'),
    
    path('detalhes/<int:id>', views.detalhes, name='detalhes_evento'),
    path('excluir/<int:id>', views.excluir, name='excluir_evento'),
    path('adicionar-eventos/', views.criar_eventos, name='adicionar_eventos'),

    # paths para a linha do tempo, era pra eu criar uma nova app, mas nao farei isso 
    path('linhadotempofalse/', views.linhadotempofalse, name="linha-tempo-false"),
    path('linhadotempotrue/', views.linhadotempotrue, name="linha-tempo-true"),
#
]