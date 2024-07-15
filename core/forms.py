from django import forms
from django.forms import ModelForm, Form
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Categoria, Producto, Perfil


class ProductoForm(ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'
        widgets = {
            'descripcion': forms.Textarea(),
            'imagen': forms.FileInput(attrs={'class': 'd-none'}),
        }
        labels = {
        'nombre': 'Nombre',
        'descuento_subscriptor': 'Subscriptor(%)',
        'descuento_oferta': 'Oferta(%)'
        }

# El formulario de bodega está listo, no necesitas modificarlo
class BodegaForm(Form):
    categoria = forms.ModelChoiceField(queryset=Categoria.objects.all(), label='Categoría')
    producto = forms.ModelChoiceField(queryset=Producto.objects.none(), label='Producto')
    cantidad = forms.IntegerField(label='Cantidad')
    class Meta:
        fields = '__all__'

# El formulario de ingreso está listo, no necesitas modificarlo
class IngresarForm(Form):
    username = forms.CharField(widget=forms.TextInput(), label="Cuenta")
    password = forms.CharField(widget=forms.PasswordInput(), label="Contraseña")
    class Meta:
        fields = ['username', 'password']

# PARA LA PAGINA DE REGISTRO DE NUEVO CLIENTE:
# Crea RegistroUsuarioForm como una clase que hereda de UserCreationForm
# asocialo con el modelo User
# muestra los campos: 
#    'username', 'first_name', 'last_name', 'email', 'password1' y 'password2'
# renombra la etiqueta del campo 'email' por 'E-mail'

class RegistroUsuarioForm(UserCreationForm):
   class Meta:
        model = User
        fields =['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
        labels ={
                'email': 'E-mail'
        }



# PARA LA PAGINA DE REGISTRO DE NUEVO CLIENTE Y MIS DATOS:
# Crear RegistroPerfilForm como una clase que hereda de ModelForm
# asocialo con el modelo Perfil
# muestra los campos: 'rut', 'direccion', 'subscrito', 'imagen'
# excluye el campo 'tipo_usuario', pues sólo los administradores asignan el tipo
# crea los widgets para:
#   - direccion como Textarea,
#   - imagen como FileInput()
class RegistroPerfilForm(ModelForm):
    class Meta:
        model = Perfil
        fields = ['rut', 'direccion', 'subscrito', 'imagen']
        exclude =['tipo_usuario']
        widgets = {
            'direccion': forms.Textarea(),
            'imagen': forms.FileInput(),
        }

# PARA LA PAGINA MIS DATOS Y MANTENEDOR DE USUARIOS:
# Crear UsuarioForm como una clase que hereda de ModelForm
# asocialo con el modelo User
# muestra todos los campos: 'username', 'first_name', 'last_name' e 'email'
# renombra la etiqueta del campo 'email' por 'E-mail'
class UsuarioForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        labels = {
            'email': 'E-mail',
        }


# PARA LA PAGINA MANTENEDOR DE USUARIOS:
# Crear PerfilForm como una clase que hereda de ModelForm
# asocialo con el modelo Perfil
# muestra todos los campos: 
#    'tipo_usuario', 'rut', 'direccion', 'subscrito'e 'imagen'
# crea los widgets para:
#   - direccion como Textarea,
#   - imagen como FileInput()
class PerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ['tipo_usuario', 'rut', 'direccion', 'subscrito', 'imagen']
        widgets = {
            'direccion': forms.Textarea(),
            'imagen': forms.FileInput(),
        }
