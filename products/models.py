from django.db import models

# Create your models here.


class Produto(models.Model):
    nome = models.CharField(max_length=250, blank=False, null=False)
    codigo = models.CharField(max_length=50, unique=True, null=False, blank=False)
    descricao = models.TextField(null=True, blank=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade_estoque = models.PositiveIntegerField()
    data_criacao = models.DateTimeField(auto_now_add=True)