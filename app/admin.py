from django.contrib import admin
from .models import *

#AGREGAR CAMPO CODIGO
# Register your models here.
class ProductoAdmin(admin.ModelAdmin):
    list_display = ['nombre','precio','stock','tipo','imagen','created_at','update_at']
    search_fields= ['codigo']

admin.site.register(TipoProducto)
admin.site.register(Producto,ProductoAdmin)

