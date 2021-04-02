from django.shortcuts import redirect
from products.models import Product
from django.contrib.auth.decorators import login_required
from .cart import Cart


@login_required(login_url="/autenticacion/login")
def add_product(request, product_id):
    cart = Cart(request)
    product = Product.objects.get(id=product_id)
    cart.add(product=product)
    return redirect("listado_productos")


@login_required(login_url="/autenticacion/login")
def remove_product(request, product_id):
    cart = Cart(request)
    product = Product.objects.get(id=product_id)
    cart.remove(product)
    return redirect("listado_productos")


@login_required(login_url="/autenticacion/login")
def decrement_product(request, product_id):
    cart = Cart(request)
    product = Product.objects.get(id=product_id)
    cart.decrement(product=product)
    return redirect("listado_productos")


@login_required(login_url="/autenticacion/login")
def clear_cart(request):
    cart = Cart(request)
    cart.clear()
    return redirect("listado_productos")
