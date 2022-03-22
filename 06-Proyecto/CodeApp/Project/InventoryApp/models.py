from django.contrib.auth.models import AbstractUser, AbstractBaseUser
from django.db import models

class Estado(models.Model):
    DescripcionEstado = models.CharField('Descripción del estado', max_length = 100)
    
    def __str__(self):
        return self.DescripcionEstado
    
    class Meta: 
        verbose_name = 'Estado'
        verbose_name_plural = 'Estados'
        db_table = 'estados'
        ordering = ['id']

class TipoMovimiento(models.Model):
    DescripcionMovimiento = models.CharField('Descripción del movimiento', max_length = 100)
    
    def __str__(self):
        return self.DescripcionMovimiento
    
    class Meta: 
        verbose_name = 'TMovimiento'
        verbose_name_plural = 'TMovimientos'
        db_table = 'tipomovimiento'
        ordering = ['id']
        
class Marcas(models.Model):
    DescripcionMarca = models.CharField('Descripción de la marca', max_length = 100)
    
    def __str__(self):
        return self.DescripcionMarca 
    
    class Meta:
        verbose_name = 'Marca' 
        verbose_name_plural = 'Marcas'
        db_table = 'marcas' 
        ordering = ['id']
        
class Categorias(models.Model):
    DescripcionCategoria = models.CharField('Descripción de la categoría', max_length = 100)

    def __str__(self):
        return self.DescripcionCategoria
    
    class Meta: 
        verbose_name = 'Categoría' 
        verbose_name_plural = 'Categorías'
        db_table = 'categorias'
        ordering = ['id'] 
        
class Materiales(models.Model):
    DescripcionMateriales = models.CharField('Descripción del material', max_length = 100)
    
    def __str__(self):
        return self.DescripcionMateriales
    
    class Meta: 
        verbose_name = 'Material'
        verbose_name_plural = 'Materiales'
        db_table = 'materiales'
        ordering = ['id']
        
class PaisOrigen(models.Model):
    DescripcionPais = models.CharField('Descripción del país', max_length = 100)
    
    def __str__(self):
        return self.DescripcionPais
    
    class Meta: 
        verbose_name = 'País de Origen'
        verbose_name_plural = 'Países de Origen'
        db_table = 'paises'
        ordering = ['id']
        
class TipoDocumento(models.Model):
    DescripcionTipoDoc = models.CharField('Descripción del tipo de documento', max_length = 100)
    
    def __str__(self):
        return self.DescripcionTipoDoc
    
    class Meta: 
        verbose_name = 'Tipo de Documento'
        verbose_name_plural = 'Tipos de Documento'
        db_table = 'tipodoc'
        ordering = ['id']
        
class Roles(models.Model):
    DescripcionRol = models.CharField('Descripción del rol', max_length = 100)
    
    def __str__(self):
        return self.DescripcionRol
    
    class Meta: 
        verbose_name = 'Rol'
        verbose_name_plural = 'Roles'
        db_table = 'roles'
        ordering = ['id']
        
class Proveedores(models.Model):
    NombreProveedor = models.CharField('Nombre del proveedor', max_length = 100)
    DireccionProveedor = models.CharField('Dirección del proveedor', max_length = 100)
    TelefonoProveedor = models.CharField('Teléfono del proveedor', max_length = 100)
    EmailProveedor = models.EmailField('Email del proveedor', max_length = 100)
    Estado = models.ForeignKey(Estado, on_delete=models.CASCADE, default='')
    # Agregar foráneas
    
    def __str__(self):
        return self.NombreProveedor
    
    class Meta: 
        verbose_name = 'Proveedor'
        verbose_name_plural = 'Proveedores'
        db_table = 'proveedores'
        ordering = ['id']

class Clientes(models.Model):
    NombreCliente = models.CharField('Nombre del cliente', max_length = 100)
    ApellidoCliente = models.CharField('Apellido del cliente', max_length = 100)
    BarrioCliente = models.CharField('Barrio del cliente', max_length = 100)
    DireccionCliente = models.CharField('Dirección del cliente', max_length = 100)
    TelefonoCliente = models.CharField('Teléfono del cliente', max_length = 100)
    ProductosFrecuentes = models.CharField('Productos que frecuenta', max_length = 100)
    # Agregar foránea
    
    def __str__(self):
        return self.NombreCliente
    
    class Meta: 
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        db_table = 'clientes'
        ordering = ['id']
        
class Movimientos(models.Model):
    Fecha = models.DateField('Fecha del movimiento')
    Cantidad = models.PositiveIntegerField('Cantidad de productos vendidos')
    PrecioFinal = models.DecimalField('Precio final de la venta', max_digits = 10, decimal_places = 2)
    Clientes = models.ForeignKey(Clientes, on_delete=models.CASCADE, default='')
    TipoMovimiento = models.ForeignKey(TipoMovimiento, on_delete=models.CASCADE, default='')
    # Productos = models.ForeignKey(Productos, on_delete=models.CASCADE, default='')
    # Productos = models.ManyToManyField(Productos, default='', blank=True)
    # Si es necesario, agregar quién realizó la venta.
    
    def __str__(self):
        return str(self.Cantidad) #Poner Fecha, Producto, Cantidad y Cliente
    
    class Meta:
        verbose_name = 'Movimiento'
        verbose_name_plural = 'Movimientos'
        db_table = 'movimientos'
        ordering = ['id']

class Productos(models.Model):
    NombreProducto = models.CharField('Nombre del producto', max_length = 100)
    DescripcionProducto = models.CharField('Descripción del producto', max_length = 100)
    PrecioCompra = models.DecimalField('Precio de compra del producto', max_digits = 10, decimal_places = 2)
    PrecioVenta = models.DecimalField('Precio de venta del producto', max_digits = 10, decimal_places = 2)
    CantidadProductos = models.PositiveIntegerField('Cantidad de productos comprados', null=True)
    FechaIngreso = models.CharField('Fecha de ingreso del producto', max_length = 100)
    Talla = models.CharField('Talla del producto', max_length = 100)
    Estado = models.ForeignKey(Estado, on_delete=models.CASCADE, default='')
    Materiales = models.ForeignKey(Materiales, on_delete=models.CASCADE, default='')
    Categorias = models.ForeignKey(Categorias, on_delete=models.CASCADE, default='')
    PaisOrigen = models.ForeignKey(PaisOrigen, on_delete=models.CASCADE, default='')
    Marcas = models.ForeignKey(Marcas, on_delete=models.CASCADE, default='')
    Proveedores = models.ForeignKey(Proveedores, on_delete=models.CASCADE, default='')
    Clientes = models.ForeignKey(Clientes, on_delete=models.CASCADE, default='')
    Movimientos = models.ForeignKey(Movimientos, on_delete=models.CASCADE, default='')
    TipoMovimiento = models.ForeignKey(TipoMovimiento, on_delete=models.CASCADE, default='')
    
    def __str__(self):
        return self.NombreProducto 
    
    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        db_table = 'productos'
        ordering = ['id']
        
class Usuarios(models.Model):
    NombreUsuario = models.CharField('Nombre del usuario', max_length = 100)
    ApellidoUsuario = models.CharField('Apellido del usuario', max_length = 100)
    TelefonoUsuario = models.CharField('Teléfono del usuario', max_length = 100)
    EmailUsuario = models.EmailField('Email del usuario', max_length = 100)
    NumeroDocumento = models.CharField('Número de documento del usuario', max_length = 100)
    Usuario = models.CharField('Usuario', max_length = 100)
    Contraseña = models.CharField('Contraseña', max_length = 100)
    Estado = models.ForeignKey(Estado, on_delete=models.CASCADE, default='')
    Roles = models.ForeignKey(Roles, on_delete=models.CASCADE, default='')
    TipoDocumento = models.ForeignKey(TipoDocumento, on_delete=models.CASCADE, default='')
    
    def __str__(self):
        return self.NombreUsuario
    
    class Meta: 
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        db_table = 'usuarios'
        ordering = ['id']

class Inventario(models.Model):
    Productos = models.ForeignKey(Productos, on_delete=models.CASCADE, default='')
    Entradas = models.PositiveIntegerField('Cantidad de productos ingresados')
    Salidas = models.PositiveIntegerField('Cantidad de productos vendidos')
    TotalInventario = models.PositiveIntegerField('Cantidad de productos en inventario')
    
    def __str__(self):
        return str(self.TotalInventario) #Poner Fecha, Producto, Cantidad y Cliente
    
    class Meta:
        verbose_name = 'Inventario'
        verbose_name_plural = 'Inventarios'
        db_table = 'inventario'
        ordering = ['id']

class MyUser(AbstractUser):
    TelefonoUsuario = models.CharField('Teléfono del usuario', max_length = 100)
    NumeroDocumento = models.CharField('Número de documento del usuario', max_length = 100)
    TipoDocumento = models.ForeignKey(TipoDocumento, on_delete=models.CASCADE, default='', blank=True, null=True)
    Estado = models.ForeignKey(Estado, on_delete=models.CASCADE, default='', blank=True, null=True)
    Roles = models.ForeignKey(Roles, on_delete=models.CASCADE, default='', blank=True, null=True)

    REQUIRED_FIELDS = ['first_name', 'last_name', 'email', 'TelefonoUsuario', 'NumeroDocumento']

    class Meta: 
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        db_table = 'myuser'
        ordering = ['id']
    
    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        db_table = 'myuser'
        ordering = ['id']

