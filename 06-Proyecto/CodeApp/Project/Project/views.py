from curses.ascii import HT
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.contrib.auth import authenticate
from django.shortcuts import redirect
from django.contrib.auth import login 
from django.contrib.auth import logout #Logout pendiente
from django.contrib.auth import authenticate
from django.contrib import messages
# Importo los modelos de la app.
from InventoryApp.models import Estado
from InventoryApp.models import Movimientos
from InventoryApp.models import Productos
from InventoryApp.models import Categorias
from InventoryApp.models import Clientes
from InventoryApp.models import Marcas
from InventoryApp.models import Materiales
from InventoryApp.models import PaisOrigen
from InventoryApp.models import Proveedores
from InventoryApp.models import Roles
from InventoryApp.models import TipoDocumento
from InventoryApp.models import TipoMovimiento
from InventoryApp.models import MyUser
from InventoryApp.models import Inventario
# Forms 
from InventoryApp.forms import ProductosForm
from InventoryApp.forms import ClientesForm
from InventoryApp.forms import ProveedoresForm
from InventoryApp.forms import RolesForm
from InventoryApp.forms import TipoDocumentoForm
from InventoryApp.forms import CategoriasForm
# from InventoryApp.forms import MovimientosForm
from InventoryApp.forms import MaterialesForm
from InventoryApp.forms import EstadosForm
from InventoryApp.forms import MarcasForm
from InventoryApp.forms import PaisesForm
from InventoryApp.forms import CustomUserCreationForm
from django.core.paginator import Paginator
from django.http import Http404
# ORM - Object Relational Mapping.

def dashboardinventario(request):
    inventario = (Inventario.objects.all()) # Creo variable que traiga todos los datos de la tabla Ventas.
    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(inventario, 5)
        inventario = paginator.page(page)
    except:
        raise Http404

    return render(request, 'dashboardinventario.html', {
        'entity' : inventario,
        'paginator' : paginator # Con este c??digo busco todos los datos de la tabla Ventas y los env??o a la vista. 
} )
    
def dashboardproductos(request):
    productos = (Productos.objects.all()) # Creo variable que traiga todos los datos de la tabla Productos.
    return render(request, 'dashboardproductos.html', {
        'productos' : productos # Con este c??digo busco todos los datos de la tabla Productos y los env??o a la vista.
} )
    
def dashboardcategorias(request):
    categorias = (Categorias.objects.all()) # Creo variable que traiga todos los datos de la tabla Categorias.
    page = request.GET.get('page', 1)

    try: 
        paginator = Paginator(categorias, 5)
        categorias = paginator.page(page)
    except:
        raise Http404

    return render(request, 'dashboardcategorias.html', {
        'entity' : categorias,
        'paginator': paginator # Con este c??digo busco todos los datos de la tabla Categorias y los env??o a la vista.
} )
    
def dashboardclientes(request):
    clientes = (Clientes.objects.all()) # Creo variable que traiga todos los datos de la tabla Clientes.
    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(clientes, 5)
        clientes = paginator.page(page)
    except:
        raise Http404

    return render(request, 'dashboardclientes.html', {
        'entity' : clientes,
        'paginator': paginator # Con este c??digo busco todos los datos de la tabla Clientes y los env??o a la vista.
} )

def dashboardestado(request):
    estados = (Estado.objects.all()) # Creo variable que traiga todos los datos de la tabla Estado.
    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(estados, 5)
        estados = paginator.page(page)
    except:
        raise Http404

    return render(request, 'dashboardestado.html', {
        'entity' : estados,
        'paginator': paginator # Con este c??digo busco todos los datos de la tabla Estado y los env??o a la vista.
} )
    
def dashboardmarcas(request):
    marcas = (Marcas.objects.all()) # Creo variable que traiga todos los datos de la tabla Marcas.
    page = request.GET.get('page', 1)

    try: 
        paginator = Paginator(marcas, 5)
        marcas = paginator.page(page)
    except:
        raise Http404

    return render(request, 'dashboardmarcas.html', {
        'entity' : marcas,
        'paginator' : paginator # Con este c??digo busco todos los datos de la tabla Marcas y los env??o a la vista.

} )
    
def dashboardmateriales(request):
    materiales = (Materiales.objects.all()) # Creo variable que traiga todos los datos de la tabla Materiales.
    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(materiales, 5)
        materiales = paginator.page(page)
    except:
        raise Http404

    return render(request, 'dashboardmateriales.html', {
        'entity' : materiales,
        'paginator' : paginator # Con este c??digo busco todos los datos de la tabla Materiales y los env??o a la vista.
} )
    
def dashboardpaisorigen(request):
    paisorigen = (PaisOrigen.objects.all()) # Creo variable que traiga todos los datos de la tabla PaisOrigen.
    page = request.GET.get('page', 1)
    
    try:
        paginator = Paginator(paisorigen, 5)
        paisorigen = paginator.page(page)
    except:
        raise Http404

    return render(request, 'dashboardpaisorigen.html', {
        'entity' : paisorigen,
        'paginator' : paginator # Con este c??digo busco todos los datos de la tabla PaisOrigen y los env??o a la vista.
} )
    
def dashboardproveedores(request):
    proveedores = (Proveedores.objects.all()) # Creo variable que traiga todos los datos de la tabla Proveedores.
    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(proveedores, 5)
        proveedores = paginator.page(page)
    except:
        raise Http404

    return render(request, 'dashboardproveedores.html', {
        'entity' : proveedores,
        'paginator' : paginator # Con este c??digo busco todos los datos de la tabla Proveedores y los env??o a la vista.
} )
    
def dashboardroles(request):
    roles = (Roles.objects.all()) # Creo variable que traiga todos los datos de la tabla Roles.
    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(roles, 5)
        roles = paginator.page(page)
    except:
        raise Http404

    return render(request, 'dashboardroles.html', {
        'entity' : roles,
        'paginator' : paginator # Con este c??digo busco todos los datos de la tabla Roles y los env??o a la vista.
} )
    
def dashboardtipodoc(request):
    tipodoc = (TipoDocumento.objects.all())
    page = request.GET.get('page', 1) # Creo variable que traiga todos los datos de la tabla TipoDoc.

    try:
        paginator = Paginator(tipodoc, 5)
        tipodoc = paginator.page(page)
    except:
        raise Http404

    return render(request, 'dashboardtipodoc.html', {
        'entity' : tipodoc,
        'paginator' : paginator
} )
    
def dashboardusuarios(request):
    usuarios = (MyUser.objects.all()) # Creo variable que traiga todos los datos de la tabla Usuarios.
    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(usuarios, 5)
        usuarios = paginator.page(page)
    except:
        raise Http404

    return render(request, 'dashboardusuarios.html', {
        'entity' : usuarios,
        'paginator' : paginator
} )
    
# Funciones de agregar utilizando Forms.py

def createusuarios(request):
    cusuarios = CustomUserCreationForm()
    if request.method == 'POST':
        formulario = CustomUserCreationForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Usuario registrado correctamente')
            return redirect('dashusuarios')
        else:
            messages.error(request, 'Aseg??rese de estar escribiendo bien los datos.')
        
    return render(request, 'createusuarios.html', {
        'cusuarios' : cusuarios
})

def createproductos(request):
    cproductos = ProductosForm()
    if request.method == 'POST':
        formulario = ProductosForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Producto registrado correctamente')
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
            messages.success(request, 'Cliente registrado correctamente')
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
            messages.success(request, 'Proveedor registrado correctamente')
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
            messages.success(request, 'Rol registrado correctamente')
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
            messages.success(request, 'Tipo de documento registrado correctamente')
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
            messages.success(request, 'Categor??a registrada correctamente')
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
            messages.success(request, 'Venta registrada correctamente')
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
            messages.success(request, 'Material registrado correctamente')
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
            messages.success(request, 'Estado registrado correctamente')
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
            messages.success(request, 'Marca registrada correctamente')
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
            messages.success(request, 'Pa??s registrado correctamente')
            return redirect('dashpais')
        
    return render(request, 'createpaises.html', {
        'cpaises' : cpaises
})

# Funciones de eliminar

def eliminarusuarios(request, id):
    usuarios = get_object_or_404(MyUser, id=id)
    usuarios.delete()
    messages.success(request, 'Usuario eliminado correctamente')
    return redirect(to='dashusuarios')
    
def eliminarproductos(request, id):
    productos = get_object_or_404(Productos, id=id)
    productos.delete()
    messages.success(request, 'Producto eliminado correctamente')
    return redirect(to='dashproductos')

def eliminarclientes(request, id):
    clientes = get_object_or_404(Clientes, id=id)
    clientes.delete()
    messages.success(request, 'Cliente eliminado correctamente')
    return redirect(to='dashclientes')

def eliminarproveedores(request, id):
    proveedores = get_object_or_404(Proveedores, id=id)
    proveedores.delete()
    messages.success(request, 'Proveedor eliminado correctamente')
    return redirect(to='dashproveedores')

def eliminarroles(request, id):
    roles = get_object_or_404(Roles, id=id)
    roles.delete()
    messages.success(request, 'Rol eliminado correctamente')
    return redirect(to='dashroles')

def eliminartipodoc(request, id):
    tipodoc = get_object_or_404(TipoDocumento, id=id)
    tipodoc.delete()
    messages.success(request, 'Tipo de documento eliminado correctamente')
    return redirect(to='dashtipodoc')

def eliminarcategorias(request, id):
    categorias = get_object_or_404(Categorias, id=id)
    categorias.delete()
    messages.success(request, 'Categor??a eliminada correctamente')
    return redirect(to='dashcategoria')

def eliminarventas(request, id):
    ventas = get_object_or_404(Ventas, id=id)
    ventas.delete()
    messages.success(request, 'Venta eliminada correctamente')
    return redirect(to='dashventas')

def eliminarmateriales(request, id):
    materiales = get_object_or_404(Materiales, id=id)
    materiales.delete()
    messages.success(request, 'Material eliminado correctamente')
    return redirect(to='dashmateriales')

def eliminarestados(request, id):
    estados = get_object_or_404(Estado, id=id)
    estados.delete()
    messages.success(request, 'Estado eliminado correctamente')
    return redirect(to='dashestado')

def eliminarmarcas(request, id):
    marcas = get_object_or_404(Marcas, id=id)
    marcas.delete()
    messages.success(request, 'Marca eliminada correctamente')
    return redirect(to='dashmarcas')

def eliminarpaisorigen(request, id):
    paises = get_object_or_404(PaisOrigen, id=id)
    paises.delete()
    messages.success(request, 'Pa??s de origen eliminado correctamente')
    return redirect(to='dashpais')

# Funciones de editar

def updatecategorias(request, id):
    categorias = get_object_or_404(Categorias, id=id)
    data =  {
        'formcategorias': CategoriasForm(instance=categorias)
    }
    if request.method == 'POST':
        formulario = CategoriasForm(data=request.POST, instance=categorias)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Categor??a modificada correctamente')
            return redirect(to='dashcategoria')
        data['formcategorias'] = formulario	
    return render(request, 'updatecategorias.html', data)

def updateclientes(request, id):
    clientes = get_object_or_404(Clientes, id=id)
    data =  {
        'formclientes': ClientesForm(instance=clientes)
    }
    if request.method == 'POST':
        formulario = ClientesForm(data=request.POST, instance=clientes)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Cliente modificado correctamente')
            return redirect(to='dashclientes')
        data['formclientes'] = formulario	
    return render(request, 'updateclientes.html', data)

def updateestados(request, id):
    estados = get_object_or_404(Estado, id=id)
    data =  {
        'formestado': EstadosForm(instance=estados)
    }
    if request.method == 'POST':
        formulario = EstadosForm(data=request.POST, instance=estados)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Estado modificado correctamente')
            return redirect(to='dashestado')
        data['formestado'] = formulario	
    return render(request, 'updateestado.html', data)

def updatemarcas(request, id):
    marcas = get_object_or_404(Marcas, id=id)
    data =  {
        'formmarca': MarcasForm(instance=marcas)
    }
    if request.method == 'POST':
        formulario = MarcasForm(data=request.POST, instance=marcas)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Marca modificado correctamente')
            return redirect(to='dashmarcas')
        data['formmarca'] = formulario	
    return render(request, 'updatemarcas.html', data)

def updatemateriales(request, id):
    materiales = get_object_or_404(Materiales, id=id)
    data =  {
        'formmateriales': MaterialesForm(instance=materiales)
    }
    if request.method == 'POST':
        formulario = MaterialesForm(data=request.POST, instance=materiales)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Material modificado correctamente')
            return redirect(to='dashmateriales')
        data['formmateriales'] = formulario	
    return render(request, 'updatemateriales.html', data)

def updatepaisorigen(request, id):
    paisorigen = get_object_or_404(PaisOrigen, id=id)
    data =  {
        'formpaisorigen': PaisesForm(instance=paisorigen)
    }
    if request.method == 'POST':
        formulario = PaisesForm(data=request.POST, instance=paisorigen)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Pa??s de Origen modificado correctamente')
            return redirect(to='dashpais')
        data['formpaisorigen'] = formulario	
    return render(request, 'updatepaisorigen.html', data)

def updateproductos(request, id):
    productos = get_object_or_404(Productos, id=id)
    data =  {
        'formproductos': ProductosForm(instance=productos)
    }
    if request.method == 'POST':
        formulario = ProductosForm(data=request.POST, instance=productos)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Producto modificado correctamente')
            return redirect(to='dashproductos')
        data['formproductos'] = formulario	
    return render(request, 'updateproductos.html', data)

def updateproveedores(request, id):
    proveedores = get_object_or_404(Proveedores, id=id)
    data =  {
        'formproveedores': ProveedoresForm(instance=proveedores)
    }
    if request.method == 'POST':
        formulario = ProveedoresForm(data=request.POST, instance=proveedores)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Proveedor modificado correctamente')
            return redirect(to='dashproveedores')
        data['formproveedores'] = formulario	
    return render(request, 'updateproveedores.html', data)

def updateroles(request, id):
    roles = get_object_or_404(Roles, id=id)
    data =  {
        'formroles': RolesForm(instance=roles)
    }
    if request.method == 'POST':
        formulario = RolesForm(data=request.POST, instance=roles)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Rol modificado correctamente')
            return redirect(to='dashroles')
        data['formroles'] = formulario	
    return render(request, 'updateroles.html', data)

def updatetipodoc(request, id):
    tipodoc = get_object_or_404(TipoDocumento, id=id)
    data =  {
        'formtipodoc': TipoDocumentoForm(instance=tipodoc)
    }
    if request.method == 'POST':
        formulario = TipoDocumentoForm(data=request.POST, instance=tipodoc)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Tipo de Documento modificado correctamente')
            return redirect(to='dashtipodoc')
        data['formtipodoc'] = formulario	
    return render(request, 'updatetipodoc.html', data)

def updateusuarios(request, id):
    usuarios = get_object_or_404(MyUser, id=id)
    data =  {
        'formusuarios': CustomUserCreationForm(instance=usuarios)
    }
    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST, instance=usuarios)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Usuario modificado correctamente')
            return redirect(to='dashusuarios')
        data['formusuarios'] = formulario	
    return render(request, 'updateusuarios.html', data)

def updateventas(request, id):
    ventas = get_object_or_404(Ventas, id=id)
    data =  {
        'formventas': VentasForm(instance=ventas)
    }
    if request.method == 'POST':
        formulario = VentasForm(data=request.POST, instance=ventas)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Venta modificado correctamente')
            return redirect(to='dashventas')
        data['formventas'] = formulario	
    return render(request, 'updateventas.html', data)

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
            messages.success(request, 'Hola, {} ?????????????'.format(user.username))
            return redirect('dashestado')
        else: 
            messages.error(request, '??? Usuario y/o contrase??a incorrectos.')
    return render(request, 'login.html',{
})

def logout_view(request):
    logout(request)
    messages.success(request, 'Sesi??n finalizada. Hasta pronto! ????')
    return redirect('login')