from pyexpat import model
from .models import *
from rest_framework import serializers


class ProdcutoSerializer(serializers.ModelSerializer):
    class  Meta:
        model = Producto
        fields = '__all__'

class TipoProdcutoSerializer(serializers.ModelSerializer):
    class  Meta:
        model = TipoProducto
        fields = '__all__'

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model= Usuario
        fields = '__all__'
        

class TipoUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model= TipoUsuario
        fields = '__all__'
        