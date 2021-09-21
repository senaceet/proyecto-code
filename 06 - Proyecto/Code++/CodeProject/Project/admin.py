from django.contrib import admin
from .models import Productos
from .models import Ventas
from .models import Roles
from .models import Estado
from .models import Marcas
from .models import Categorias
from .models import Materiales
from .models import PaisOrigen
from .models import TipoDocumento
from .models import Roles
from .models import Clientes
from .models import Usuarios
from .models import Proveedores


#admin.site.register(Productos)
#admin.site.register(Ventas)
admin.site.register(Roles)
admin.site.register(Estado)
admin.site.register(Marcas)
admin.site.register(Categorias)
admin.site.register(Materiales)
admin.site.register(PaisOrigen)
admin.site.register(TipoDocumento)
admin.site.register(Clientes)
admin.site.register(Usuarios)
admin.site.register(Proveedores)

@admin.register(Productos) 
class Productos(admin.ModelAdmin):
    list_display = ["DescripcionProducto", "Categorias", "Estado"]
    
@admin.register(Ventas) 
class Ventas(admin.ModelAdmin):
    list_display = ["Fecha", "Clientes", "Productos"]