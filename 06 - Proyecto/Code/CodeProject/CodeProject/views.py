from django.shortcuts import render
from django.contrib.auth import authenticate
from django.shortcuts import redirect
from django.contrib.auth import login 
from django.contrib.auth import logout #Logout pendiente
from django.contrib.auth import authenticate
from django.contrib import messages
# Importo los modelos de la app.
from ProjectApp.models import Estado
from ProjectApp.models import Ventas
from ProjectApp.models import Productos
from ProjectApp.models import Categorias
from ProjectApp.models import Clientes
from ProjectApp.models import Marcas
from ProjectApp.models import Materiales
from ProjectApp.models import PaisOrigen
from ProjectApp.models import Proveedores
from ProjectApp.models import Roles
from ProjectApp.models import TipoDocumento
from ProjectApp.models import Usuarios
# Forms 
from ProjectApp.forms import UsuariosForm
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

