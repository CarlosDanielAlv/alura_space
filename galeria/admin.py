from django.contrib import admin
from galeria.models import Fotografia

class ListandoFotografias(admin.ModelAdmin):
    list_display = ("id", "nome", "legenda", "publicada") # Colunas da lista
    list_display_links = ("id", "nome") # Onde os links de edição aparecem
    search_fields = ("nome",) # Campos filtráveis
    list_filter = ("categoria",) # Categorias filtráveis
    list_editable = ("publicada", ) # Celulas que podem ser editáveis
    list_per_page = 10 # itens por página


admin.site.register(Fotografia, ListandoFotografias)