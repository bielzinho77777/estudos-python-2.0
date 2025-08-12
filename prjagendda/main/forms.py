from django import forms
from .models import DatasEventos

class Minha_Forms(forms.ModelForm):
    class Meta:
        model = DatasEventos
        fields = ["titulo", "prioridade", "descricao", "data_fim"]
'''
titulo = models.CharField(max_length=200)
    prioridade = models.CharField(max_length=20, choices=PROPRIEDADES, default='N')
    descricao = models.TextField()
    data_fim = models.DateField()'''