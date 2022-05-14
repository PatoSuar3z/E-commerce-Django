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
