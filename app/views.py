from django.shortcuts import render, redirect
from .models import *
from .forms import *

# Create your views here.
#SECCION LISTAR
def index(request):
    productosAll = Producto.objects.all()
    datos={
        'listaProductos' : productosAll
    }
    return render(request,'app/index.html',datos)

#SECCION AGREGAR
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

def listarproductos(request):
    productosAll = Producto.objects.all()
    datos = {
        'listarProductos' : productosAll
    }
    
    return render(request, 'app/listar_productos.html', datos)

def modificarproducto(request, codigo):
    producto = Producto.objects.get(codigo=codigo)
    datos = {
        'form' : ProductoForm(instance=producto)
    }
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, files=request.FILES, instance=producto)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = 'Producto modificado correctamente!'
            datos['form'] = formulario

    return render(request, 'app/modificar_producto.html', datos)

def eliminarproducto(request, codigo):
    producto = Producto.objects.get(codigo=codigo)
    producto.delete()

    return redirect(to="listarproductos")

def login(request):
    return render(request, 'app/login.html')

def carrito(request):
    return render(request, 'app/carrito.html')

def registro(request):
    return render (request, 'app/registro.html')

def productos(request):
    productosAll = Producto.objects.all()
    datos={
        'listaProductos' : productosAll
    }
    return render(request,'app/productos.html',datos)

def administrador(request):
    return render (request, 'app/administrador.html')

