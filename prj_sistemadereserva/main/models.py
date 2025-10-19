from django.db import models

# Create your models here.
class Quarto(models.Model):
    id = models.AutoField(primary_key=True)
    numero = models.CharField(max_length=10, unique=True)
    capacidade = models.PositiveIntegerField(default=1)  # Quantas pessoas cabem

    def __str__(self):
        return f"{self.id} - Quarto {self.numero} (capacidade {self.capacidade})"


class Reserva(models.Model):
    id = models.AutoField(primary_key=True)
    quarto = models.ForeignKey(Quarto, on_delete=models.CASCADE, related_name="reservas")
    nome_hospede = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)
    data_entrada = models.DateField()
    data_saida = models.DateField()
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.id} - {self.nome_hospede} - {self.quarto.numero}"
