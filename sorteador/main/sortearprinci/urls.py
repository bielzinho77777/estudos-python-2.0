from django.urls import path, include
from . import views
urlpatterns = [
    path('',views.index, name="index"),
    path("sorteados/",views.sorteados,name='sorteados'),
    path("sorteados/dnv/",views.refresh,name='refresh'),
]
