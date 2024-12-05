from django.contrib import admin
from .models import Produto

# Register your models here.
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nome', 'descricao', 'preco', 'quantidade_estoque', 'data_criacao') 
    search_fields = ('codigo', 'nome')  
    list_filter = ('data_criacao',)  
    ordering = ('-data_criacao',)

admin.site.register(Produto, ProdutoAdmin)
# Register your models here.
