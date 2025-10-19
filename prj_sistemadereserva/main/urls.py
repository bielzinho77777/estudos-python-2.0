from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name= 'index' ),
    path('reservas/', views.reservas, name= 'reservas' ),
    path('agendamento/', views.agendamento, name= 'agendamento' ),
    path('detalhes/<int:id_quarto>/', views.detalhes, name= 'detalhes' ),
    path('disponiveis/', views.quartos_disponiveis, name= 'disponivel' ),
    path('reservar/<int:id_quarto>/', views.reservar, name= 'reservar' ),
]
