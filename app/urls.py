from csv import list_dialects
from django.contrib import admin
from django.urls import path
from .views import *



urlpatterns = [
    path('', index, name="index"),
    path('login', login, name="login"),
    path('carrito', carrito, name="carrito"),
    path('agregar_producto',agregar_producto, name="agregar_producto"),
    path('modificar/<codigo>', modificarproducto, name="modificarproducto"),
    path('listar/',listarproductos, name="listar_productos"),
    path('eliminarproducto/<codigo>',eliminarproducto, name="eliminar_producto"),
    path('registro',registro, name="registro"),
    path('productos',productos, name="productos"),
    path('administrador',administrador, name="administrador"),

]
