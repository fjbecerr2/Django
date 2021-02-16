from django.contrib import admin

# Register your models here.
#Importar nuestra tablas

from .models import Clientes, Articulos, Pedidos

#Clase para visualizacion de los campos de
#la tabla de manera individual
#Deben incluirse los campos
#La clase se pone tambien en el admin.site.register
#Desactiva la funcion __str__ como sistema de visualizacion
class ClientesAdmin(admin.ModelAdmin):
    list_display=('nombre','direccion','email','telefono')
    #Casilla de busqueda en el admin, se indican los campos para buscar
    search_fields = ['nombre', 'telefono']

#incluir en el panel de administracion
admin.site.register(Clientes,ClientesAdmin)
admin.site.register(Articulos)
admin.site.register(Pedidos)
