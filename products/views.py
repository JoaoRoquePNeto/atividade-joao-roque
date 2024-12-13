from django.shortcuts import render, get_object_or_404
from .models import Produto, Categoria, Fornecedor


def lista_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'products/lista_produtos.html', {'produtos': produtos})


def lista_categorias(request):
    categorias = Categoria.objects.all()
    return render(request, 'products/lista_categorias.html', {'categorias': categorias})


def lista_fornecedores(request):
    fornecedores = Fornecedor.objects.all()
    return render(request, 'products/lista_fornecedores.html', {'fornecedores': fornecedores})


def detalhe_produto(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)
    return render(request, 'products/detalhe_produto.html', {'produto': produto})
