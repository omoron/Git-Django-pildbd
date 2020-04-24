from django.contrib import admin
from pilddb.models import Clientes, Articulos, Pedidos

# Register your models here.

class ClientesAdmin(admin.ModelAdmin):
    list_display = ("id", "nombres", "direccion", "email", "telefono")
    search_fields = ("nombres", "telefono")

class ArticulosAdmin(admin.ModelAdmin):
    list_display = ("id", "nombres", "seccion", "precio")
    list_filter = ("seccion",)
    #search_fields = ("nombres", "seccion")

class PedidosAdmin(admin.ModelAdmin):
    list_display = ("id", "numero", "fecha", "entregado")
    list_filter = ("fecha",)
    date_hierarchy = "fecha"

admin.site.register(Clientes, ClientesAdmin)
admin.site.register(Articulos, ArticulosAdmin)
admin.site.register(Pedidos, PedidosAdmin)
