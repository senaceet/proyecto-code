from django.shortcuts import render
from django.contrib.auth import authenticate
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth import login 
from django.contrib.auth import logout #Logout pendiente
from django.contrib.auth import authenticate
from django.contrib import messages
from FinalProject.models import TipoDocumento
from FinalProject.models import Categorias
from FinalProject.models import Productos
from FinalProject.models import Clientes
from FinalProject.models import Usuarios
from FinalProject.models import Estado
from FinalProject.models import Roles
from FinalProject.models import TipoDocumento

def dashboardventas(request):
    return render(request, 'dashboardventas.html', {
        'message': 'Mensaje desde el contexto.',
        'list': [1,2,3]
        # Context
} )
    
def dashboardproductos(request):
    productosListados = Productos.objects.all() #Lista de Productos
    return render(request, 'dashboardclientes.html', {
    "productos": productosListados
} )
    
def dashboardcategorias(request):
        categoriasListadas = Categorias.objects.all() #Lista de categorias
        return render(request, 'dashboardcategorias.html', {
        "categorias": categoriasListadas
} )
    
def dashboardclientes(request):
    clientesListados = Clientes.objects.all() #Lista de Clientes
    return render(request, 'dashboardclientes.html', {
    "clientes": clientesListados
} )
def dashboardestado(request):
    return render(request, 'dashboardestado.html', {
        # Context
} )
    
def dashboardmarcas(request):
    return render(request, 'dashboardmarcas.html', {
        # Context
} )
    
def dashboardmateriales(request):
    return render(request, 'dashboardmateriales.html', {
        # Context
} )
    
def dashboardpaisorigen(request):
    return render(request, 'dashboardpaisorigen.html', {
        # Context
} )
    
def dashboardproveedores(request):
    return render(request, 'dashboardproveedores.html', {
        # Context
} )
    
def dashboardroles(request):
    return render(request, 'dashboardroles.html', {
} )
    
def dashboardtipodoc(request):
    return render(request, 'dashboardtipodoc.html', {
        # Context
} )
    
def dashboardusuarios(request):
    usuariosListados = Usuarios.objects.all() #Lista de Clientes
    return render(request, 'dashboardusuarios.html', {
    "usuarios": usuariosListados
} )
    
def index(request):
    return render(request, 'index.html', {
        # Context
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

# Métodos para el dashboard de Categorias---------------------------------------------------------.

def formregcategorias(request):
    return render(request, 'formregistrarcategoria.html', {
        # Context
})

def registrarCategoria(request):
    DescripcionCategoria=request.POST['txtCategory']
    categoria=Categorias.objects.create(DescripcionCategoria=DescripcionCategoria)
    
    return redirect('dashcategoria')

def eliminacionCategoria(request, id):
    idcategoria=Categorias.objects.get(id=id)
    idcategoria.delete()
    return redirect('dashcategoria')

def edicionCategoria(request, DescripcionCategoria):
    categoria=Categorias.objects.get(DescripcionCategoria=DescripcionCategoria)
    return render(request, 'edicioncategoria.html', {"categoria":categoria})

def editarCategoria(request):
    DescripcionCategoria=request.POST['txtCategory']
    
    categoria=Categorias.objects.get(DescripcionCategoria=DescripcionCategoria)
    categoria.DescripcionCategoria=DescripcionCategoria
    categoria.save()
    return redirect('dashcategoria')

# Métodos para el dashboard de Clientes---------------------------------------------------------.

def formregclientes(request):
    clientesListados = Clientes.objects.all() #Lista de Productos
    return render(request, 'formregistrarclientes.html', {
    "clientes": clientesListados
})
    
def registrarClientes(request):
    NombreCliente=request.POST.get('txtNombreCliente')
    ApellidoCliente=request.POST.get('txtApellidoCliente')
    DireccionCliente=request.POST.get('txtDireccionCliente')
    TelefonoCliente=request.POST.get('txtTelefonoCliente')
    # Productos=request.POST.get['selectProduct']
    Cliente=Clientes.objects.create(NombreCliente=NombreCliente, ApellidoCliente=ApellidoCliente, DireccionCliente=DireccionCliente, TelefonoCliente=TelefonoCliente)
    return redirect('dashclientes')

# Métodos para el dashboard de Usuarios---------------------------------------------------------.

def formregusuarios(request):
    rolesListados = Roles.objects.all() #Lista de Clientes
    estadosListados = Estado.objects.all() #Lista de Estados
    tipodocListados = TipoDocumento.objects.all() #Lista de TipoDocumento
    return render(request, 'formregistrarusuarios.html', {
    "roles": rolesListados, "estados": estadosListados, "tipodocumento": tipodocListados
})
        
def registrarUsuario(request):
    NombreUsuario=request.POST.get('txtNombreUsuario')
    ApellidoUsuario=request.POST.get('txtApellidoUsuario')
    TelefonoUsuario=request.POST.get('txtTelefonoUsuario')
    EmailUsuario=request.POST.get('txtEmailUsuario')
    NumeroDocumento=request.POST.get('txtNumeroDocumento')
    Usuario=request.POST.get('txtUsuario')
    Contraseña=request.POST.get('txtContraseña')
    Estado=request.POST.get('selectEstado')
    Roles=request.POST.get('selectRoles')
    TipoDocumento=request.POST.get('selectTipoDocumento')
    Usuario=Usuarios.objects.create(NombreUsuario=NombreUsuario, 
                                    ApellidoUsuario=ApellidoUsuario, 
                                    TelefonoUsuario=TelefonoUsuario, 
                                    EmailUsuario=EmailUsuario, 
                                    NumeroDocumento=NumeroDocumento, 
                                    Usuario=Usuario, 
                                    Contraseña=Contraseña, 
                                    Estado=Estado, 
                                    Roles=Roles, 
                                    TipoDocumento=TipoDocumento)
    return redirect('dashclientes')