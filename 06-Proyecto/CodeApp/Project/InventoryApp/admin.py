from django.contrib import admin
from .models import Productos
# from .models import Ventas
from .models import Roles
from .models import Estado
from .models import Marcas
from .models import Categorias
from .models import Materiales
from .models import PaisOrigen
from .models import TipoDocumento
from .models import Roles
from .models import Clientes
from .models import Proveedores
from .models import MyUser
from .forms import CustomUserCreationForm
from django.contrib.auth.admin import UserAdmin

class CustomUserAdmin(UserAdmin):
    model = MyUser
    add_form = CustomUserCreationForm


admin.site.register(Productos)
# admin.site.register(Ventas)
admin.site.register(Roles)
admin.site.register(Estado)
admin.site.register(Marcas)
admin.site.register(Categorias)
admin.site.register(Materiales)
admin.site.register(PaisOrigen)
admin.site.register(TipoDocumento)
admin.site.register(Clientes)
admin.site.register(Proveedores)
admin.site.register(MyUser, CustomUserAdmin)

