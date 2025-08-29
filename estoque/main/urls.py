from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name= 'index' ),

    path('<str:tipocategoria>/', views.index, name= 'index' ),
    path('adicionar/', views.adicionar_produto,  name= "adicionar" ),
    path('detalhes/<int:id>/', views.detalhes_produto,  name= "detalhes" ),
    path('excluir/<int:id>/', views.excluir_produto,  name= "excluir" ),
] 