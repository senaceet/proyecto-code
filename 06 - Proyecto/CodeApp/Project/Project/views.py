from django.shortcuts import render
from django.contrib.auth import authenticate
from django.shortcuts import redirect
from django.contrib.auth import login 
from django.contrib.auth import logout #Logout pendiente
from django.contrib.auth import authenticate
from django.contrib import messages
# Importo los modelos de la app.
from InventoryApp.models import Estado
from InventoryApp.models import Ventas
from InventoryApp.models import Productos
from InventoryApp.models import Categorias
from InventoryApp.models import Clientes
from InventoryApp.models import Marcas
from InventoryApp.models import Materiales
from InventoryApp.models import PaisOrigen
from InventoryApp.models import Proveedores
from InventoryApp.models import Roles
from InventoryApp.models import TipoDocumento
from InventoryApp.models import Usuarios
# Forms 
from InventoryApp.forms import UsuariosForm
from InventoryApp.forms import ProductosForm
from InventoryApp.forms import ClientesForm
from InventoryApp.forms import ProveedoresForm
from InventoryApp.forms import RolesForm
from InventoryApp.forms import TipoDocumentoForm
from InventoryApp.forms import CategoriasForm
from InventoryApp.forms import VentasForm
from InventoryApp.forms import MaterialesForm
from InventoryApp.forms import EstadosForm
from InventoryApp.forms import MarcasForm
from InventoryApp.forms import PaisesForm
# ORM - Object Relational Mapping.

def dashboardventas(request):
    ventas = (Ventas.objects.all()) # Creo variable que traiga todos los datos de la tabla Ventas.
    return render(request, 'dashboardventas.html', {
        'ventas' : ventas # Con este código busco todos los datos de la tabla Ventas y los envío a la vista. 
} )
    
def dashboardproductos(request):
    productos = (Productos.objects.all()) # Creo variable que traiga todos los datos de la tabla Productos.
    return render(request, 'dashboardproductos.html', {
        'productos' : productos # Con este código busco todos los datos de la tabla Productos y los envío a la vista.
} )
    
def dashboardcategorias(request):
    categorias = (Categorias.objects.all()) # Creo variable que traiga todos los datos de la tabla Categorias.
    return render(request, 'dashboardcategorias.html', {
        'categorias' : categorias # Con este código busco todos los datos de la tabla Categorias y los envío a la vista.
} )
    
def dashboardclientes(request):
    clientes = (Clientes.objects.all()) # Creo variable que traiga todos los datos de la tabla Clientes.
    return render(request, 'dashboardclientes.html', {
        'clientes' : clientes # Con este código busco todos los datos de la tabla Clientes y los envío a la vista.
} )

def dashboardestado(request):
    estados = (Estado.objects.all()) # Creo variable que traiga todos los datos de la tabla Estado.
    return render(request, 'dashboardestado.html', {
        'estado' : estados # Con este código busco todos los datos de la tabla Estado y los envío a la vista.
} )
    
def dashboardmarcas(request):
    marcas = (Marcas.objects.all()) # Creo variable que traiga todos los datos de la tabla Marcas.
    return render(request, 'dashboardmarcas.html', {
        'marcas' : marcas # Con este código busco todos los datos de la tabla Marcas y los envío a la vista.
} )
    
def dashboardmateriales(request):
    materiales = (Materiales.objects.all()) # Creo variable que traiga todos los datos de la tabla Materiales.
    return render(request, 'dashboardmateriales.html', {
        'materiales' : materiales # Con este código busco todos los datos de la tabla Materiales y los envío a la vista.
} )
    
def dashboardpaisorigen(request):
    paisorigen = (PaisOrigen.objects.all()) # Creo variable que traiga todos los datos de la tabla PaisOrigen.
    return render(request, 'dashboardpaisorigen.html', {
        'paisorigen' : paisorigen # Con este código busco todos los datos de la tabla PaisOrigen y los envío a la vista.
} )
    
def dashboardproveedores(request):
    proveedores = (Proveedores.objects.all()) # Creo variable que traiga todos los datos de la tabla Proveedores.
    return render(request, 'dashboardproveedores.html', {
        'proveedores' : proveedores # Con este código busco todos los datos de la tabla Proveedores y los envío a la vista.
} )
    
def dashboardroles(request):
    roles = (Roles.objects.all()) # Creo variable que traiga todos los datos de la tabla Roles.
    return render(request, 'dashboardroles.html', {
        'roles' : roles # Con este código busco todos los datos de la tabla Roles y los envío a la vista.
} )
    
def dashboardtipodoc(request):
    tipodoc = (TipoDocumento.objects.all()) # Creo variable que traiga todos los datos de la tabla TipoDoc.
    return render(request, 'dashboardtipodoc.html', {
        'tipodoc' : tipodoc
} )
    
def dashboardusuarios(request):
    usuarios = (Usuarios.objects.all()) # Creo variable que traiga todos los datos de la tabla Usuarios.
    return render(request, 'dashboardusuarios.html', {
        'usuarios' : usuarios
} )
    
# Funciones utilizando Forms.py

def createusuarios(request):
    cusuarios = UsuariosForm()
    if request.method == 'POST':
        formulario = UsuariosForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Usuario creado correctamente')
            return redirect('dashusuarios')
        
    return render(request, 'createusuarios.html', {
        'cusuarios' : cusuarios
})

def createproductos(request):
    cproductos = ProductosForm()
    if request.method == 'POST':
        formulario = ProductosForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Producto creado correctamente')
            return redirect('dashproductos')
        
    return render(request, 'createproductos.html', {
        'cproductos' : cproductos
})

def createclientes(request):
    cclientes = ClientesForm()
    if request.method == 'POST':
        formulario = ClientesForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Cliente creado correctamente')
            return redirect('dashclientes')
        
    return render(request, 'createclientes.html', {
        'cclientes' : cclientes
})

def createproveedores(request):
    cproveedores = ProveedoresForm()
    if request.method == 'POST':
        formulario = ProveedoresForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Proveedor creado correctamente')
            return redirect('dashproveedores')
        
    return render(request, 'createproveedores.html', {
        'cproveedores' : cproveedores
})

def createroles(request):
    croles = RolesForm()
    if request.method == 'POST':
        formulario = RolesForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Rol creado correctamente')
            return redirect('dashroles')
        
    return render(request, 'createroles.html', {
        'croles' : croles
})

def createtipodoc(request):
    ctipodoc = TipoDocumentoForm()
    if request.method == 'POST':
        formulario = TipoDocumentoForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Tipo de documento creado correctamente')
            return redirect('dashtipodoc')
        
    return render(request, 'createtipodoc.html', {
        'ctipodoc' : ctipodoc
})

def createcategorias(request):
    ccategorias = CategoriasForm()
    if request.method == 'POST':
        formulario = CategoriasForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Categoría creada correctamente')
            return redirect('dashcategoria')
        
    return render(request, 'createcategorias.html', {
        'ccategorias' : ccategorias
})

def createventas(request):
    cventas = VentasForm()
    if request.method == 'POST':
        formulario = VentasForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Venta creada correctamente')
            return redirect('dashventas')
        
    return render(request, 'createventas.html', {
        'cventas' : cventas
})

def createmateriales(request):
    cmateriales = MaterialesForm()
    if request.method == 'POST':
        formulario = MaterialesForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Material creado correctamente')
            return redirect('dashmateriales')
        
    return render(request, 'createmateriales.html', {
        'cmateriales' : cmateriales
})

def createestados(request):
    cestados = EstadosForm()
    if request.method == 'POST':
        formulario = EstadosForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Estado creado correctamente')
            return redirect('dashestado')
    return render(request, 'createestados.html', {
        'cestados' : cestados
})

def createmarcas(request):
    cmarcas = MarcasForm()
    if request.method == 'POST':
        formulario = MarcasForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Marca creada correctamente')
            return redirect('dashmarcas')
        
    return render(request, 'createmarcas.html', {
        'cmarcas' : cmarcas
})

def createpaisorigen(request):
    cpaises = PaisesForm()
    if request.method == 'POST':
        formulario = PaisesForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'País creado correctamente')
            return redirect('dashpais')
        
    return render(request, 'createpaises.html', {
        'cpaises' : cpaises
})

def index(request):
    return render(request, 'index.html', {
} )
    
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
    
    return render(request, 'login.html', {
        # Context
} )

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request)
            messages.success(request, 'Bienvenido {}'.format(user.username))
            return redirect('dashventas')
        else: 
            messages.error(request, 'Usuario o contraseña incorrecta')
    return render(request, 'login.html',{
})

def logout_view(request):
    logout(request)
    messages.success(request, 'Sesión finalizada')
    return redirect('login')