from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('login', views.login_view, name='login'),
    path('dashboardproductos', views.dashboardproductos, name='dashproductos'), # Registro creado
    path('dashboardventas', views.dashboardventas, name='dashventas'), # Registro creado
    path('dashboardcategorias', views.dashboardcategorias, name='dashcategoria'), # Registro creado
    path('dashboardclientes', views.dashboardclientes, name='dashclientes'), # Registro creado
    path('dashboardestado', views.dashboardestado, name='dashestado'), # Registro creado
    path('dashboardmarcas', views.dashboardmarcas, name='dashmarcas'), # Registro creado
    path('dashboardmateriales', views.dashboardmateriales, name='dashmateriales'), # Registro creado
    path('dashboardpaisorigen', views.dashboardpaisorigen, name='dashpais'),
    path('dashboardproveedores', views.dashboardproveedores, name='dashproveedores'), # Registro creado
    path('dashboardroles', views.dashboardroles, name='dashroles'), # Registro creado
    path('dashboardtipodoc', views.dashboardtipodoc, name='dashtipodoc'), # Registro creado
    path('dashboardusuarios', views.dashboardusuarios, name='dashusuarios'), # Registro creado
    # Forms
    path('createusuarios', views.createusuarios, name='createusuarios'),
    path('createproductos', views.createproductos, name='createproductos'),
    path('createclientes', views.createclientes, name='createclientes'),
    path('createproveedores', views.createproveedores, name='createproveedores'),
    path('createroles', views.createroles, name='createroles'),
    path('createtipodoc', views.createtipodoc, name='createtipodoc'),
    path('createcategorias', views.createcategorias, name='createcategorias'),
    path('createventas', views.createventas, name='createventas'),
    path('createmateriales', views.createmateriales, name='createmateriales'),
    path('createestados', views.createestados, name='createestados'),
    path('createmarcas', views.createmarcas, name='createmarcas'),
    path('createpaisorigen', views.createpaisorigen, name='createpaisorigen'),
]
