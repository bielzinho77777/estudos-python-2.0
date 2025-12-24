from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator

# Create your models here.
class Numbers(models.Model):
    inicio = models.IntegerField(null=False, validators=[MinValueValidator(0, message='O valor mínimo é 0')])
    fim = models.IntegerField(null=False, validators=[MinValueValidator(1, message='O valor mínimo é 1')])
    quantidade = models.IntegerField(null=False, validators=[MinValueValidator(1, message='O valor mínimo é 1')])
    gerarnovo = models.BooleanField(default=False)
    def clean(self):
        if self.inicio >= self.fim:
            raise ValidationError(
                {'inicio': 'Início deve ser menor que o fim.'}
            )

        total = self.fim - self.inicio + 1
        if self.quantidade > total:
            raise ValidationError(
                {'quantidade': 'Quantidade maior que o intervalo.'}
            )