from .models import Product,Category
from django.forms import ModelForm, ModelChoiceField

class VistaCrearProducto(ModelForm):
    class Meta:
        model = Product
        exclude = ['url','available','main_image','secondary_image','thirth_image']

class VistaCrearCategoria(ModelForm):
    class Meta:
        model = Category
        fields = ['name']


