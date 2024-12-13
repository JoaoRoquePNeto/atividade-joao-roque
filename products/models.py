from django.db import models


class Categoria(models.Model):
    nome = models.CharField(max_length=150, blank=False, null=False)

    def __str__(self):
        return self.nome

class Fornecedor(models.Model):
    nome = models.CharField(max_length=250, blank=False, null=False)
    endereco = models.CharField(max_length=300, blank=True, null=True)
    telefone = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return self.nome

class Produto(models.Model):
    nome = models.CharField(max_length=250, blank=False, null=False)
    codigo = models.CharField(max_length=50, unique=True, null=False, blank=False)
    descricao = models.TextField(null=True, blank=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade_estoque = models.PositiveIntegerField()
    data_criacao = models.DateTimeField(auto_now_add=True)
    categorias = models.ManyToManyField(Categoria, related_name='produtos', blank=True)
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.SET_NULL, null=True, blank=True, related_name='produtos')

    def __str__(self):
        return self.nome
