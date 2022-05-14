from django import forms
from django.forms import ModelForm
from .models import *

#CREAMOS TEMPLATES DE LOS FORMULARIOS
class ProductoForm(ModelForm):

    nombre = forms.CharField(min_length=10,max_length=20)
    precio = forms.IntegerField(min_value=400)

    class Meta:
        model = Producto
        fields =  ['codigo','nombre','precio','stock','tipo','imagen']

      