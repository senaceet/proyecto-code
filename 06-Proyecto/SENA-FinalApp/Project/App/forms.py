from cProfile import label
from tkinter import Widget
from tokenize import group
from django import forms
from django.contrib.auth.models import AbstractUser
from .models import TipoDocumento, Estado, Productos, Materiales, Categorias, PaisOrigen, Marcas, Proveedores, Clientes, Roles, Movimientos, PaisOrigen, MyUser, TipoMovimiento, Inventario
from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'input'}), label='Usuario')
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input'}), label='Contraseña')
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input'}), label='Confirmar contraseña')
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'input'}), label='Nombre del usuario')
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'input'}), label='Apellido del usuario')
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'input'}), label='Correo electrónico')
    TelefonoUsuario = forms.CharField(widget=forms.TextInput(attrs={'class': 'input'}), label='Teléfono')
    NumeroDocumento = forms.CharField(widget=forms.TextInput(attrs={'class': 'input'}), label='Número de documento')
    TipoDocumento = forms.ModelChoiceField(queryset=TipoDocumento.objects.all(), widget=forms.Select(attrs={'class':'input'}), label="Seleccione un tipo de documento")
    Estado = forms.ModelChoiceField(queryset=Estado.objects.all(), widget=forms.Select(attrs={'class':'input'}), label="Seleccione un estado")
    Roles = forms.ModelChoiceField(queryset=Roles.objects.all(), widget=forms.Select(attrs={'class':'input'}), label="Seleccione un rol")

    class Meta:
        model = MyUser
        fields = ('username', 'password1', 'password2', 'first_name', 'last_name', 'email', 'TelefonoUsuario', 'NumeroDocumento', 'TipoDocumento', 'Estado', 'Roles', 'groups')
        widgets = {
            'groups': forms.SelectMultiple(attrs={'class': 'input'})
        }

class ProductosForm(forms.ModelForm):
    NombreProducto = forms.CharField(widget=forms.TextInput(attrs={'class':'input'}), label="Nombre del Producto")
    DescripcionProducto = forms.CharField(widget=forms.TextInput(attrs={'class':'input'}), label="Descripción del Producto")
    PrecioCompra = forms.CharField(widget=forms.TextInput(attrs={'class':'input'}), label="Precio del Producto (Docena)")
    PrecioVenta = forms.CharField(widget=forms.TextInput(attrs={'class':'input'}), label="Precio de venta del Producto (Docena)")
    FechaIngreso = forms.CharField(widget=forms.TextInput(attrs={'class':'input'}), label="Fecha de Ingreso")
    Talla = forms.CharField(widget=forms.TextInput(attrs={'class':'input'}), label="Talla del Producto")
    Estado = forms.ModelChoiceField(queryset=Estado.objects.all(), widget=forms.Select(attrs={'class':'input'}), label="Seleccione un Estado")
    Materiales = forms.ModelChoiceField(queryset=Materiales.objects.all(), widget=forms.Select(attrs={'class':'input'}), label="Seleccione un Material")
    Categorias = forms.ModelChoiceField(queryset=Categorias.objects.all(), widget=forms.Select(attrs={'class':'input'}), label="Seleccione una Categoría")
    PaisOrigen = forms.ModelChoiceField(queryset=PaisOrigen.objects.all(), widget=forms.Select(attrs={'class':'input'}), label="Seleccione un País de Origen")
    Marcas = forms.ModelChoiceField(queryset=Marcas.objects.all(), widget=forms.Select(attrs={'class':'input'}), label="Seleccione una Marca")
    Proveedores = forms.ModelChoiceField(queryset=Proveedores.objects.all(), widget=forms.Select(attrs={'class':'input'}), label="Seleccione un Proveedor")
    class Meta:
        model = Productos
        fields = '__all__' # sirve para listarlos todos

class ClientesForm(forms.ModelForm):
    NombreCliente = forms.CharField(widget=forms.TextInput(attrs={'class':'input'}), label="Nombre del Cliente")
    ApellidoCliente = forms.CharField(widget=forms.TextInput(attrs={'class':'input'}), label="Apellido del Cliente")
    TelefonoCliente = forms.CharField(widget=forms.TextInput(attrs={'class':'input'}), label="Teléfono del Cliente")
    DireccionCliente = forms.CharField(widget=forms.TextInput(attrs={'class':'input'}), label="Dirección del Cliente")
    BarrioCliente = forms.CharField(widget=forms.TextInput(attrs={'class':'input'}), label="Barrio del Cliente")
    ProductosFrecuentes = forms.CharField(widget=forms.TextInput(attrs={'class':'input'}), label="Productos frecuentes del Cliente")
    class Meta:
        model = Clientes
        fields = '__all__' # sirve para listarlos todos

class ProveedoresForm(forms.ModelForm):
    NombreProveedor = forms.CharField(widget=forms.TextInput(attrs={'class':'input'}), label="Nombre del Proveedor")
    DireccionProveedor = forms.CharField(widget=forms.TextInput(attrs={'class':'input'}), label="Dirección del Proveedor")
    TelefonoProveedor = forms.CharField(widget=forms.TextInput(attrs={'class':'input'}), label="Teléfono del Proveedor")
    EmailProveedor = forms.CharField(widget=forms.TextInput(attrs={'class':'input'}), label="Email del Proveedor")
    Estado = forms.ModelChoiceField(queryset=Estado.objects.all(), widget=forms.Select(attrs={'class':'input'}), label="Seleccione un Estado")
    class Meta:
        model = Proveedores
        fields = '__all__' # sirve para listarlos todos

class RolesForm(forms.ModelForm):
    DescripcionRol = forms.CharField(widget=forms.TextInput(attrs={'class':'input'}), label="Nombre del Rol")
    class Meta:
        model = Roles
        fields = '__all__' # sirve para listarlos todos

class TipoDocumentoForm(forms.ModelForm):
    DescripcionTipoDoc = forms.CharField(widget=forms.TextInput(attrs={'class':'input'}), label="Nombre del Tipo de Documento")
    class Meta:
        model = TipoDocumento
        fields = '__all__' # sirve para listarlos todos

class TipoMovimientoForm(forms.ModelForm):
    DescripcionMovimiento = forms.CharField(widget=forms.TextInput(attrs={'class':'input'}), label="Nombre del Tipo de movimiento")
    class Meta:
        model = TipoMovimiento
        fields = '__all__' # sirve para listarlmos todos

class CategoriasForm(forms.ModelForm):
    DescripcionCategoria = forms.CharField(widget=forms.TextInput(attrs={'class':'input'}), label="Nombre de la Categoría")
    class Meta:
        model = Categorias
        fields = '__all__' # sirve para listarlos todos

class MovimientosForm(forms.ModelForm):
    FechaMovimiento = forms.CharField(widget=forms.TextInput(attrs={'class':'input', 'placeholder': 'DD/MM/AAAA'}), label="Fecha del movimiento")
    TipoMovimiento = forms.ModelChoiceField(queryset=TipoMovimiento.objects.all(), widget=forms.Select(attrs={'class':'input'}), label="Seleccione un tipo de movimiento")
    CantidadProductos = forms.IntegerField(widget=forms.TextInput(attrs={'class':'input'}) , label="Cantidad de Productos")
    Clientes = forms.ModelChoiceField(queryset=Clientes.objects.all(), widget=forms.Select(attrs={'class':'input'}), label="Seleccione un Cliente")
    Productos = forms.ModelChoiceField(queryset=Productos.objects.all(), widget=forms.Select(attrs={'class':'input'}), label="Seleccione un Producto")
    class Meta:
        model = Movimientos
        fields = '__all__' # sirve para listarlos todos

class MovimientosEntradasForm(forms.ModelForm):
    FechaMovimiento = forms.CharField(widget=forms.TextInput(attrs={'class':'input', 'placeholder': 'DD/MM/AAAA'}), label="Fecha del movimiento")
    CantidadProductos = forms.IntegerField(widget=forms.TextInput(attrs={'class':'input'}) , label="Cantidad de Productos")
    Productos = forms.ModelChoiceField(queryset=Productos.objects.all(), widget=forms.Select(attrs={'class':'input'}), label="Seleccione un Producto")
    Proveedores = forms.ModelChoiceField(queryset=Proveedores.objects.all(), widget=forms.Select(attrs={'class':'input'}), label="Seleccione un Proveedor")
    
    class Meta:
        model = Movimientos
        fields = ('FechaMovimiento', 'CantidadProductos', 'Proveedores', 'Productos') # sirve para listarlos todos

class MovimientosSalidasForm(forms.ModelForm):
    FechaMovimiento = forms.CharField(widget=forms.TextInput(attrs={'class':'input', 'placeholder': 'DD/MM/AAAA'}), label="Fecha del movimiento")
    CantidadProductos = forms.IntegerField(widget=forms.TextInput(attrs={'class':'input'}) , label="Cantidad de Productos")
    Productos = forms.ModelChoiceField(queryset=Productos.objects.all(), widget=forms.Select(attrs={'class':'input'}), label="Seleccione un Producto")
    Clientes = forms.ModelChoiceField(queryset=Clientes.objects.all(), widget=forms.Select(attrs={'class':'input'}), label="Seleccione un Cliente")
    class Meta:
        model = Movimientos
        fields = ('FechaMovimiento', 'CantidadProductos', 'Productos', 'Clientes') # sirve para listarlos todos

class MaterialesForm(forms.ModelForm):
    DescripcionMateriales = forms.CharField(widget=forms.TextInput(attrs={'class':'input'}), label="Nombre del Material")
    class Meta:
        model = Materiales
        fields = '__all__' # sirve para listarlos todos

class EstadosForm(forms.ModelForm):
    DescripcionEstado = forms.CharField(widget=forms.TextInput(attrs={'class':'input'}), label="Nombre del Estado")
    class Meta:
        model = Estado
        fields = '__all__' # sirve para listarlos todos

class MarcasForm(forms.ModelForm):
    DescripcionMarca = forms.CharField(widget=forms.TextInput(attrs={'class':'input'}), label="Nombre de la Marca")
    class Meta:
        model = Marcas
        fields = '__all__' # sirve para listarlos todos

class PaisesForm(forms.ModelForm):
    DescripcionPais = forms.CharField(widget=forms.TextInput(attrs={'class':'input'}), label="Nombre del País")
    class Meta:
        model = PaisOrigen
        fields = '__all__' # sirve para listarlos todos
