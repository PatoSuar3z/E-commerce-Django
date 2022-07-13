from django.contrib import admin
from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()

router.register('Producto', ProductoViewSet)
router.register('Tipoproducto', TipoProductoViewSet)
router.register('User', UsuarioViewSet)
router.register('TipoUsuario', TipoUsuarioViewSet)


urlpatterns = [
    path('', index, name="index"),
    path('carrito', carrito, name="carrito"),
    path('agregar_producto',agregar_producto, name="agregar_producto"),
    path('modificar/<codigo>', modificarproducto, name="modificarproducto"),
    path('listar/',listar, name="listar"),
    path('eliminarproductocarrito/<id>/',eliminarproductocarrito, name="eliminarproductocarrito"),
    path('eliminarproducto/<codigo>/',eliminarproducto, name="eliminarproducto"),
    path('registro',registro, name="registro"),
    path('productos',productos, name="productos"),
    path('cliente',cliente, name="cliente"),
    path('seguimiento',seguimiento, name="seguimiento"),
    path('api/', include(router.urls)),
    path('api_catalogo',api_catalogo, name="api_catalogo"),
    path('template', template, name="template"),
    path('perfil', perfil, name="perfil"),
    path('historial', historial, name="historial"),
    path('eliminatodocarrito/<id>/',eliminatodocarrito, name="eliminatodocarrito"),
    path('api_externa',api_externa, name="api_externa"),
]
