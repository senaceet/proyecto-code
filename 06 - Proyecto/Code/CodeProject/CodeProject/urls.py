"""CodeProject URL Configuration

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
    path('', views.index, name='index'),
    path('login', views.login_view, name='login'),
    path('dashboardproductos', views.dashboardproductos, name='dashproductos'),
    path('dashboardventas', views.dashboardventas, name='dashventas'),
    path('dashboardcategorias', views.dashboardcategorias, name='dashcategoria'),
    path('dashboardclientes', views.dashboardclientes, name='dashclientes'),
    path('dashboardestado', views.dashboardestado, name='dashestado'),
    path('dashboardmarcas', views.dashboardmarcas, name='dashmarcas'),
    path('dashboardmateriales', views.dashboardmateriales, name='dashmateriales'),
    path('dashboardpaisorigen', views.dashboardpaisorigen, name='dashpais'),
    path('dashboardproveedores', views.dashboardproveedores, name='dashproveedores'),
    path('dashboardroles', views.dashboardroles, name='dashroles'),
    path('dashboardtipodoc', views.dashboardtipodoc, name='dashtipodoc'),
    path('dashboardusuarios', views.dashboardusuarios, name='dashusuarios'),
    # Forms
    path('createusuarios', views.createusuarios, name='createusuarios'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


