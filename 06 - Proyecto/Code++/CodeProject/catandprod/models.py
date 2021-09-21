from django.db import models

# Actividad Models
# A continuación se crean los dos modelos

class Category(models.Model):
    Name = models.CharField('Nombre de la Categoría', max_length = 100)
    Description = models.CharField('Descripción de la Categoría', max_length = 100)
    
    def __str__(self):
        return self.Name
    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        db_table = 'category'
        ordering = ['id']
        
class Product(models.Model):
    Name = models.CharField('Nombre del Producto', max_length = 100)
    Price = models.DecimalField(verbose_name='Precio', max_digits = 10, decimal_places = 2)
    Stock = models.PositiveIntegerField(verbose_name='Stock')
    Description = models.CharField('Descripción del Producto', max_length = 100)
    State = models.CharField('Estado del Producto', max_length = 20)
    Category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.Name
    
    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        db_table = 'product'
        ordering = ['id']
        
