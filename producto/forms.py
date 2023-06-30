from django.forms import ModelForm
from .models import Producto

class produForm(ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'precio', 'categoria']
        