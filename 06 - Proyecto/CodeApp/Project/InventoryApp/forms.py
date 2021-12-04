from django import forms
from django.contrib.auth.models import AbstractUser
from .models import TipoDocumento, Usuarios, Estado, Productos, Materiales, Categorias, PaisOrigen, Marcas, Proveedores, Clientes, Roles, Ventas, PaisOrigen

class UsuariosForm(forms.ModelForm): # Formulario para crear usuarios
    NombreUsuario = forms.CharField(widget=forms.TextInput(attrs={'class':'input'}), label="Nombre del Usuario")
    ApellidoUsuario = forms.CharField(widget=forms.TextInput(attrs={'class':'input'}), label="Apellido del Usuario")
    TelefonoUsuario = forms.CharField(widget=forms.TextInput(attrs={'class':'input'}), label="Teléfono del Usuario")
    EmailUsuario = forms.CharField(widget=forms.TextInput(attrs={'class':'input'}), label="Email del Usuario")
    NumeroDocumento = forms.CharField(widget=forms.TextInput(attrs={'class':'input'}), label="Número de Documento")
    Usuario = forms.CharField(widget=forms.TextInput(attrs={'class':'input'}), label="Usuario")
    Contraseña = forms.CharField(widget=forms.TextInput(attrs={'class':'input'}), label="Contraseña")
    Estado = forms.ModelChoiceField(queryset=Estado.objects.all(), widget=forms.Select(attrs={'class':'input'}), label="Seleccione un Estado")
    Roles = forms.ModelChoiceField(queryset=Roles.objects.all(), widget=forms.Select(attrs={'class':'input'}), label="Seleccione un Rol")
    TipoDocumento = forms.ModelChoiceField(queryset=TipoDocumento.objects.all(), widget=forms.Select(attrs={'class':'input'}), label="Seleccione un Tipo de Documento")
    class Meta:
        model = Usuarios
        #fields = ['NombreUsuario', 'ApellidoUsuario', 'TelefonoUsuario', 'EmailUsuario', 'NumeroDocumento', 'Usuario', 'Contraseña', 'Estado', 'Roles', 'TipoDocumento']
        fields = '__all__' # sirve para listarlos todos

class ProductosForm(forms.ModelForm):
    NombreProducto = forms.CharField(widget=forms.TextInput(attrs={'class':'input'}), label="Nombre del Producto")
    DescripcionProducto = forms.CharField(widget=forms.TextInput(attrs={'class':'input'}), label="Descripción del Producto")
    PrecioCompra = forms.CharField(widget=forms.TextInput(attrs={'class':'input'}), label="Precio del Producto")
    PrecioVenta = forms.CharField(widget=forms.TextInput(attrs={'class':'input'}), label="Precio de venta del Producto")
    CantidadProductos = forms.CharField(widget=forms.TextInput(attrs={'class':'input'}), label="Cantidad de Productos")
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

class CategoriasForm(forms.ModelForm):
    DescripcionCategoria = forms.CharField(widget=forms.TextInput(attrs={'class':'input'}), label="Nombre de la Categoría")
    class Meta:
        model = Categorias
        fields = '__all__' # sirve para listarlos todos

class VentasForm(forms.ModelForm):
    Fecha = forms.CharField(widget=forms.TextInput(attrs={'class':'input'}), label="Fecha de la Venta")
    DescripcionVenta = forms.CharField(widget=forms.TextInput(attrs={'class':'input'}), label="Descripción de la Venta")
    Cantidad = forms.CharField(widget=forms.TextInput(attrs={'class':'input'}), label="Cantidad de Productos")
    PrecioFinal = forms.DecimalField(widget=forms.TextInput(attrs={'class':'input'}), label="Precio Final")
    Clientes = forms.ModelChoiceField(queryset=Clientes.objects.all(), widget=forms.Select(attrs={'class':'input'}), label="Seleccione un Cliente")
    # Productos = forms.ModelChoiceField(queryset=Productos.objects.all(), widget=forms.Select(attrs={'class':'input'}), label="Seleccione un Producto")
    class Meta:
        model = Ventas
        fields = '__all__' # sirve para listarlos todos

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
