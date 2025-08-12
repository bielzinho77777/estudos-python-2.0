from django.db import models
from django.core.exceptions import ValidationError
from datetime import date
# Create your models here.
class DatasEventos(models.Model):
    PROPRIEDADES = [
        ('1', 'Urgente'),
        ('2', 'Importante'),
        ('3', 'Normal'),
        ('4', 'Sem prioridade')
    ]
    
    titulo = models.CharField(max_length=200)
    prioridade = models.CharField(max_length=20, choices=PROPRIEDADES, default='N')
    descricao = models.TextField()
    data_fim = models.DateField()
    data_inicio = models.DateField(auto_now_add=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.id} - {self.titulo} - {self.prioridade}'