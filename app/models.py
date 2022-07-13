from distutils.command.upload import upload
from unicodedata import name
from django.db import models


# Create your models here.
class TipoProducto(models.Model):
    tipo= models.CharField(max_length=20)
    def __str__(self):
        return self.tipo
    class Meta:
        db_table= 'db_tipo_producto'        

class Producto(models.Model):
    codigo=models.IntegerField()
    nombre=models.CharField(max_length=20)
    precio =models.IntegerField()
    stock=models.IntegerField()
    tipo= models.ForeignKey(TipoProducto,on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="productos", null=True)
    created_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)

    

    def __str__(self):
        return self.nombre
    
    class Meta:
        db_table= 'db_producto'

class items_carrito(models.Model):
    nombre_producto = models.CharField(max_length=40)
    precio_producto = models.IntegerField()
    imagen = models.ImageField(upload_to="items_carrito",null=True)

    def __str__(self):
        return self.nombre_producto
    
    class Meta:
        db_table = 'db_items_carrito'

class Descuento(models.Model):
    idesc=models.IntegerField()
    porcentaje=models.IntegerField()

    class Meta:
        db_table= 'db_descuento' 

class TipoUsuario(models.Model):
    user=models.CharField(max_length=15)
    def __str__(self):
        return self.user   

    class Meta:
        db_table= 'db_tipo_usuario'  

class Usuario(models.Model):
    codigo=models.IntegerField()
    nombres=models.CharField(max_length=40)
    apellidos=models.CharField(max_length=50)
    tipo=models.ForeignKey(TipoUsuario,on_delete=models.CASCADE)
    imagen=models.ImageField(upload_to="administrador", null=True)
    direccion=models.CharField(max_length=100 ,null=True)
    suscrito=models.BooleanField(default=False)

    class Meta:
        db_table= 'db_usuario' 



class HistorialCompras(models.Model):
    nombre_producto = models.CharField(max_length=40)
    precio_producto = models.IntegerField()
    imagen = models.ImageField(upload_to="",null=True)

    def __str__(self):
        return self.nombre_producto

    class Meta:
        db_table= 'db_historialcompras'

