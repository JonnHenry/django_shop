from django.db import models
from django.utils.text import slugify

# Category Model
class Category(models.Model):
    name = models.CharField(max_length=300,verbose_name='Nombre del categoria',unique=True)
    featured = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'categories'
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'
        ordering = ['-id']

# Product Model
class Product(models.Model):
    name = models.CharField(max_length=300,verbose_name='Nombre del producto',unique=True,blank=False)
    url = models.SlugField(max_length=255, unique=True,blank=True) #slug is a field to more friendly navigation, It is used in the url pattern
    category = models.ForeignKey(Category, on_delete=models.CASCADE,verbose_name='Categoria')
    main_image = models.CharField(max_length=300,verbose_name='Imagen principal',unique=True,blank=False,default='https://firebasestorage.googleapis.com/v0/b/e-commerce-19b59.appspot.com/o/default%2Fdefault.jpg?alt=media&token=90f710d3-1d62-4e4a-87b1-506a3b9c042a')
    secondary_image = models.CharField(max_length=300,verbose_name='Imagen principal',unique=True,blank=False,default='https://firebasestorage.googleapis.com/v0/b/e-commerce-19b59.appspot.com/o/default%2Fdefault.jpg?alt=media&token=90f710d3-1d62-4e4a-87b1-506a3b9c042a')
    thirth_image = models.CharField(max_length=300,verbose_name='Imagen principal',unique=True,blank=False,default='https://firebasestorage.googleapis.com/v0/b/e-commerce-19b59.appspot.com/o/default%2Fdefault.jpg?alt=media&token=90f710d3-1d62-4e4a-87b1-506a3b9c042a')
    excerpt = models.TextField(max_length=200, verbose_name='Extracto del producto') #This field is to
    detail = models.TextField(max_length=1000, verbose_name='Información del producto')
    price = models.FloatField(verbose_name='Precio')
    available = models.BooleanField(default=True,verbose_name='Disponible',blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'products'
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['id']

    def save(self, *args, **kwargs):
        self.url = slugify(self.name)
        super(Product, self).save(*args, **kwargs)