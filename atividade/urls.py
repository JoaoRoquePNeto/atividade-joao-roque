"""
URL configuration for atividade project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from products import views

urlpatterns = [
    path('produtos/', views.lista_produtos, name='lista_produtos'),
    path('categorias/', views.lista_categorias, name='lista_categorias'),
    path('fornecedores/', views.lista_fornecedores, name='lista_fornecedores'),
    path('produtos/<int:produto_id>/', views.detalhe_produto, name='detalhe_produto'),
]
