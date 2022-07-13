from django.contrib import admin
from django.utils.html import format_html
from .models import *

#AGREGAR CAMPO CODIGO
# Register your models here.
class ProductoAdmin(admin.ModelAdmin):
    list_display = ['codigo','nombre','precio','stock','tipo','imagen','created_at','update_at']
    search_fields= ['codigo']

    def imagen(self, obj):
            return format_html('<img src={} />, obj.imagen.url ')

class CarritoAdmin(admin.ModelAdmin):
    list_display = ['nombre_producto','precio_producto','imagen']

class TipoProductoAdmin(admin.ModelAdmin):
    list_display = ['tipo']

class DescuentoAdmin(admin.ModelAdmin):
    list_display = ['idesc']

class TipoUsuarioAdmin(admin.ModelAdmin):
    list_display = ['user']

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ['codigo','nombres','apellidos','tipo','imagen']

class HistorialCompras(admin.ModelAdmin):
    list_display = ['nombre_producto','precio_producto','imagen']



admin.site.register(TipoProducto,TipoProductoAdmin)
admin.site.register(Producto,ProductoAdmin)
admin.site.register(items_carrito,CarritoAdmin)
admin.site.register(Descuento,DescuentoAdmin)
admin.site.register(TipoUsuario,TipoUsuarioAdmin)
admin.site.register(Usuario,UsuarioAdmin)



