from django.shortcuts import render
from django.contrib.auth import authenticate
from django.shortcuts import redirect
from django.contrib.auth import login 
from django.contrib.auth import logout #Logout pendiente
from django.contrib.auth import authenticate
from django.contrib import messages

def dashboardventas(request):
    return render(request, 'dashboardventas.html', {
        'message': 'Mensaje desde el contexto.',
        'list': [1,2,3]
        # Context
} )
    
def dashboardproductos(request):
    return render(request, 'dashboardproductos.html', {
        # Context
} )
    
def dashboardcategorias(request):
    return render(request, 'dashboardcategorias.html', {
        # Context
} )
    
def dashboardclientes(request):
    return render(request, 'dashboardclientes.html', {
        # Context
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
        # Context
} )
    
def dashboardtipodoc(request):
    return render(request, 'dashboardtipodoc.html', {
        # Context
} )
    
def dashboardusuarios(request):
    return render(request, 'dashboardusuarios.html', {
        # Context
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