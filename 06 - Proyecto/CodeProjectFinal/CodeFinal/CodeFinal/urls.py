"""CodeFinal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # Index URL
    path('', views.index, name='index'),
    # Login URL
    path('login', views.login_view, name='login'),
    # Dashboard de Categorias + Métodos
    path('dashboardcategorias', views.dashboardcategorias, name='dashcategoria'), # Vista de Dashboard de Categorias.
    path('formregcategorias', views.formregcategorias, name='formregcategorias'), # Vista de Formulario de Registro de Categorias.
    path('edicionCategoria/<DescripcionCategoria>', views.edicionCategoria, name='edicionCategoria'), # Vista de Formulario de Edición de Categorias.
    path('registrarCategoria/', views.registrarCategoria, name='formregclientes'), # Método de Registro de Categorias.
    path('eliminacionCategoria/<id>', views.eliminacionCategoria, name='eliminacionCategoria'), # Método de Eliminación de Categorias.
    path('editarCategoria/', views.editarCategoria, name='editarCategoria'), # Método de Edición de Categorias.
    # Dashboard de Clientes + Métodos
    path('dashboardclientes', views.dashboardclientes, name='dashclientes'), # Vista de Dashboard de Clientes.
    path('formregclientes', views.formregclientes, name='formregclientes'), # Vista de Formulario de Registro de Clientes.
    path('registrarClientes/', views.registrarClientes, name='formregclientes'), # Método de Registro de Categorias.
    # Dashboard de Estado + Métodos
    path('dashboardestado', views.dashboardestado, name='dashestado'),
    # Dashboard de Marcas + Métodos
    path('dashboardmarcas', views.dashboardmarcas, name='dashmarcas'),
    # Dashboard de Materiales + Métodos
    path('dashboardmateriales', views.dashboardmateriales, name='dashmateriales'),
    # Dashboard de Pais de Origen + Métodos
    path('dashboardpaisorigen', views.dashboardpaisorigen, name='dashpais'),
    # Dashboard de Proveedores + Métodos
    path('dashboardproveedores', views.dashboardproveedores, name='dashproveedores'),
    # Dashboard de Roles + Métodos
    path('dashboardroles', views.dashboardroles, name='dashroles'),
    # Dashboard de Tipo de Documento + Métodos	
    path('dashboardtipodoc', views.dashboardtipodoc, name='dashtipodoc'),
    # Dashboard de Usuarios + Métodos
    path('dashboardusuarios', views.dashboardusuarios, name='dashusuarios'),
    path('formregusuarios', views.formregusuarios, name='formregusuarios'), # Vista de Formulario de Registro de Usuarios.
    path('registrarUsuario/', views.registrarUsuario, name='formregusuarios'), # Método de Registro de Usuarios.
    # Dashboard de Productos + Métodos
    path('dashboardproductos', views.dashboardproductos, name='dashproductos'),
    # Dashboard de Ventas + Métodos
    path('dashboardventas', views.dashboardventas, name='dashventas'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
