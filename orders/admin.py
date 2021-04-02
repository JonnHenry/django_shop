from django.contrib import admin
from .models import OrderLine, Order

admin.site.register([Order, OrderLine])
