from django.db import models
from django.urls import reverse
# Create your models here.
class Categoria(models.Model):
    nome = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, unique=True, db_index=True)

    class Meta:
        ordering = ('nome',)
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'

    def __str__(self):
        return self.nome
    
    def get_absolute_url(self):
        return reverse('main:listar_produtos_por_categoria', args=[self.slug])
class Produto(models.Model):
    categoria = models.ForeignKey(Categoria, related_name="produtos", null=True, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100, db_index=True)
    estoque = models.PositiveIntegerField(default=0)
    imagem = models.ImageField(upload_to="imagens-produtos", blank=True)

    class Meta:
        ordering = ('nome',)
        indexes = [models.Index(fields=['id']),]


    def __str__(self):
        return self.nome
    def get_absolute_url(self):
        return reverse('main:detalhes_produto', args=[self.id])