import json
from msilib.schema import Class
from urllib import response
from django import views
from django.shortcuts import render, redirect
from .models import *
from .forms import *
from .serializers import *
from rest_framework import viewsets
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import authenticate,login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import Group
from urllib.request import urlopen
import json
import requests


#API
class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProdcutoSerializer

class TipoProductoViewSet(viewsets.ModelViewSet):
    queryset = TipoProducto.objects.all()
    serializer_class = TipoProdcutoSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class TipoUsuarioViewSet(viewsets.ModelViewSet):
    queryset = TipoUsuario.objects.all()
    serializer_class = TipoUsuarioSerializer


# Create your views here.
#SECCION LISTAR
def index(request):
    productosAll = Producto.objects.all()
    datos={
        'listaProductos' : productosAll
    }

    if request.method =='POST':
        carrito = items_carrito()
        carrito.nombre_producto = request.POST.get('nombre_producto')
        carrito.precio_producto = request.POST.get('precio_producto')
        carrito.imagen = request.POST.get('imagen_producto')
        carrito.save()

    return render(request,'app/index.html', datos)


#SECCION AGREGAR

@permission_required('app.add_producto')
def agregar_producto(request):
    datos = {
        'form' : ProductoForm()
    }
    if request.method == 'POST':
        formulario = ProductoForm(request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = "Producto agregado correctamente!"
            
    return render(request,'app/agregar_producto.html',datos)

@permission_required('app.view_producto')
def listar(request):
    productosAll = Producto.objects.all()
    datos = {
        'listarProductos' : productosAll
    }
    return render(request, 'app/listar.html', datos)

@permission_required('app.change_producto')
def modificarproducto(request, codigo):
    producto = Producto.objects.get(codigo=codigo)
    datos = {
        'form' : ProductoForm(instance=producto)
    }
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, files=request.FILES, instance=producto)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Modificado Correctamente")
            return redirect(to = "listar")
        datos['form'] = formulario

    return render(request, 'app/modificar_producto.html', datos)

@permission_required('app.delete_producto')
def eliminarproducto(request,codigo):
    producto = Producto.objects.get(codigo=codigo)
    producto.delete()
    messages.success(request, "Eliminado Correctamente")
    return redirect(to = "listar")
    


@login_required
def carrito(request):
    carrito = items_carrito.objects.all()
    total  = sum(aux.precio_producto for aux in carrito)
    descuento = round((total)*0.05)
    totaldesc = total-descuento
    datos = {
        'listarCarrito' : carrito,
        'total' :   total,
        'descuento' : descuento ,
        'totaldesc' : totaldesc
    }
    
    if request.method =='POST':
        historial = HistorialCompras()
        historial.nombre_producto = request.POST.get('nombre_producto')
        historial.precio_producto = request.POST.get('precio_producto')
        historial.imagen = request.POST.get('imagen')
        historial.save()

    return render(request, 'app/carrito.html',datos)
    
def eliminatodocarrito(request,id):
    producto = items_carrito.objects.get(id=id)
    producto.delete()
    messages.success(request, "Productos Comprados")
    return redirect(to = "carrito")

def eliminarproductocarrito(request,id):
    producto = items_carrito.objects.get(id=id)
    producto.delete()
    messages.success(request, "Eliminado Correctamente")
    return redirect(to = "carrito")

def registro(request):
    datos = {
        'form' : RegistroUsuarioForm()
    }
    if request.method == 'POST':
        formulario = RegistroUsuarioForm(data=request.POST)
        if formulario.is_valid():
            user = formulario.save()
            groups = Group.objects.get(name='Cliente')
            user.groups.add(groups)
            usuario = authenticate(username=formulario.cleaned_data["username"],password=formulario.cleaned_data["password1"])
            login(request,usuario)
            messages.success(request,'Registrado correctamente!')
            return redirect(to="index")
        datos["form"] = formulario

    return render(request, 'registration/registro.html', datos)


def productos(request):
    productosAll = Producto.objects.all()
    datos={
        'listaProductos' : productosAll
    }

    if request.method =='POST':
        carrito = items_carrito()
        carrito.nombre_producto = request.POST.get('nombre_producto')
        carrito.precio_producto = request.POST.get('precio_producto')
        carrito.imagen = request.POST.get('imagen_producto')
        carrito.save()

    return render (request, 'app/productos.html', datos)

def cliente(request):
    return render (request, 'app/cliente.html')

def seguimiento(request):
    return render (request, 'app/seguimiento.html')

def api_catalogo(request):
    return render (request, 'app/api_catalogo.html')

def api_externa(request):
    response = requests.get('https://www.breakingbadapi.com/api/characters').json()
    datos =  {
        'listajson' : response
        }
    
    return render (request, 'app/api_externa.html',datos)

def template(request):
    return render (request, 'app/template.html')

def perfil(request):
    perfil = Usuario.objects.all()
    datos = {
        'listarusuarios' : perfil
    }
    return render (request, 'app/perfil.html', datos)


def historial(request):
    compras = HistorialCompras.objects.all()
    datos = {
        'Historial_Compras' : compras
    }
    return render (request, 'app/historial.html' ,datos)