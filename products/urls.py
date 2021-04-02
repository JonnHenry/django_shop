from django.urls import path
from .views import *
from .create_product import *

urlpatterns = [
    path('', listado_productos, name='listado_productos'),
    path('category/<int:category_id>/', get_by_category, name='category'),
    path('search/', search_product, name='search'),
    path('show/<int:product_id>/<int:image>', show_product, name='show'),
    path('create/', create_product, name='create'),

]
