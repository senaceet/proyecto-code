from pipes import Template
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('login', auth_views.LoginFormView.as_view(template_name='login.html'), name='login'),
    path('logout', auth_views.LogoutView.as_view(template_name='login.html'), name='logout'),
    path('dashboardproductos', views.dashboardproductos, name='dashproductos'), # Registro creado
    path('dashboardmovimientos', views.dashboardmovimientos, name='dashmovimientos'), # Registro creado
    path('dashboardcategorias', views.dashboardcategorias, name='dashcategoria'), # Registro creado
    path('dashboardclientes', views.dashboardclientes, name='dashclientes'), # Registro creado
    path('dashboardestado', views.dashboardestado, name='dashestado'), # Registro creado
    path('dashboardmarcas', views.dashboardmarcas, name='dashmarcas'), # Registro creado
    path('dashboardmateriales', views.dashboardmateriales, name='dashmateriales'), # Registro creado
    path('dashboardpaisorigen', views.dashboardpaisorigen, name='dashpais'), # Registro creado
    path('dashboardproveedores', views.dashboardproveedores, name='dashproveedores'), # Registro creado
    path('dashboardroles', views.dashboardroles, name='dashroles'), # Registro creado
    path('dashboardtipodoc', views.dashboardtipodoc, name='dashtipodoc'), # Registro creado
    path('dashboardusuarios', views.dashboardusuarios, name='dashusuarios'), # Registro creado
    path('dashboardinventario', views.dashboardinventario, name='dashinventario'), # Registro creado
    path('dashboardtipomovimiento', views.dashboardtipomovimiento, name='dashtipomovimiento'), # Registro creado
    # Forms create
    path('createusuarios', views.createusuarios, name='createusuarios'),
    path('createproductos', views.createproductos, name='createproductos'),
    path('createclientes', views.createclientes, name='createclientes'),
    path('createproveedores', views.createproveedores, name='createproveedores'),
    path('createroles', views.createroles, name='createroles'),
    path('createtipodoc', views.createtipodoc, name='createtipodoc'),
    path('createcategorias', views.createcategorias, name='createcategorias'),
    path('createmovimientos', views.createmovimientos, name='createmovimientos'),
    path('createmateriales', views.createmateriales, name='createmateriales'),
    path('createestados', views.createestados, name='createestados'),
    path('createmarcas', views.createmarcas, name='createmarcas'),
    path('createpaisorigen', views.createpaisorigen, name='createpaisorigen'),
    path('createtipomovimiento', views.createtipomovimiento, name='createtipomovimiento'),
    path('createentrada', views.createentrada, name='createentrada'),
    path('createsalida', views.createsalida, name='createsalida'),
    # Forms delete 
    path('eliminarusuarios/<id>', views.eliminarusuarios, name='eliminarusuarios'),
    path('eliminarproductos/<id>', views.eliminarproductos, name='eliminarproductos'),
    path('eliminarclientes/<id>', views.eliminarclientes, name='eliminarclientes'),
    path('eliminarproveedores/<id>', views.eliminarproveedores, name='eliminarproveedores'),
    path('eliminarroles/<id>', views.eliminarroles, name='eliminarroles'),
    path('eliminartipodoc/<id>', views.eliminartipodoc, name='eliminartipodoc'),
    path('eliminarcategorias/<id>', views.eliminarcategorias, name='eliminarcategorias'),
    path('eliminarmovimientos/<id>', views.eliminarmovimientos, name='eliminarmovimientos'),
    path('eliminarmateriales/<id>', views.eliminarmateriales, name='eliminarmateriales'),
    path('eliminarestados/<id>', views.eliminarestados, name='eliminarestados'),
    path('eliminarmarcas/<id>', views.eliminarmarcas, name='eliminarmarcas'),
    path('eliminarpaisorigen/<id>', views.eliminarpaisorigen, name='eliminarpaisorigen'),
    path('eliminartipomovimiento/<id>', views.eliminartipomovimiento, name='eliminartipomovimiento'),
    # Forms update
    path('updatecategorias/<id>/', views.updatecategorias, name='updatecategorias'),
    path('updateclientes/<id>/', views.updateclientes, name='updateclientes'),
    path('updateestados/<id>/', views.updateestados, name='updateestados'),
    path('updatemarcas/<id>/', views.updatemarcas, name='updatemarcas'),
    path('updatemateriales/<id>/', views.updatemateriales, name='updatemateriales'),
    path('updatepaisorigen/<id>/', views.updatepaisorigen, name='updatepaisorigen'),
    path('updateproductos/<id>/', views.updateproductos, name='updateproductos'),
    path('updateproveedores/<id>/', views.updateproveedores, name='updateproveedores'),
    path('updateroles/<id>/', views.updateroles, name='updateroles'),
    path('updatetipodoc/<id>/', views.updatetipodoc, name='updatetipodoc'),
    path('updateusuarios/<id>/', views.updateusuarios, name='updateusuarios'),
    path('updatemovimientos/<id>/', views.updatemovimientos, name='updatemovimientos'),
    path('updatetipomovimiento/<id>/', views.updatetipomovimiento, name='updatetipomovimiento'),
]