from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from cart.cart import Cart
from .models import Product, Category
from django.db.models import Count, Q
from .create_product import VistaCrearProducto, VistaCrearCategoria
from django.contrib import messages
from app.firebase_settings import storage,firebase
import datetime


@login_required(login_url='/autenticacion/acceder')
def listado_productos(request):
    products = Product.objects.all()
    categories = Category.objects.select_related('products').values('name', 'id').annotate(
        count=Count('product__category'))
    return render(request, "products/listado.html", {
        "products": products,
        "categories": categories
    })


@login_required(login_url='/autenticacion/acceder')
def get_by_category(request, category_id):
    products = Product.objects.filter(category=category_id)
    categories = Category.objects.select_related('products').values('name', 'id').annotate(
        count=Count('product__category'))
    return render(request, "products/listado.html", {
        "products": products,
        "categories": categories
    })


@login_required(login_url='/autenticacion/acceder')
def search_product(request):
    if "query" in request.GET:
        query = request.GET["query"].strip()
        products = Product.objects.filter(Q(name__istartswith=query) | Q(excerpt__icontains=query)).all()
        categories = Category.objects.select_related('products').values('name', 'id').annotate(
            count=Count('product__category'))
        return render(request, "products/listado.html", {
            "products": products,
            "categories": categories
        })
    else:
        products = None
        categories = Category.objects.select_related('products').values('name', 'id').annotate(
            count=Count('product__category'))
        return render(request, "products/listado.html", {
            "products": products,
            "categories": categories
        })


@login_required(login_url='/autenticacion/acceder')
def show_product(request, product_id, image):
    product = Product.objects.filter(id=product_id)[0]
    if (image == 1):
        image_main = product.main_image
    elif (image == 2):
        image_main = product.secondary_image
    else:
        image_main = product.thirth_image

    return render(request, "products/show_product.html", {
        "product": product,
        "top_image": image_main
    })


@login_required(login_url='/autenticacion/acceder')
def create_product(request):
    if request.method == "POST":
        contador = 0
        if ('price' in request.POST):  # It is used for products
            formProducto = VistaCrearProducto(request.POST or None,request.FILES)
            if formProducto.is_valid():
                if 'files' in request.FILES:
                    producto = formProducto.save(commit=False)
                    for image in request.FILES.getlist('files'):
                        name_upload = 'products/'+nameImages(formProducto.cleaned_data['category'].name,
                                                             datetime.datetime.now().strftime('%d-%m-%Y-%H-%M_%S'),
                                                             str(contador))
                        storage.child(name_upload).put(image)
                        url = storage.child(name_upload).get_url(None)
                        if contador==0:
                            producto.main_image = url
                        elif contador==1:
                            producto.secondary_image = url
                        else:
                            producto.thirth_image=url
                        contador+=1
                        #storage.child('products/imagen.jpg').put(request.FILES['main_image'])
                        #url_val = storage.child('products/imagen.jpg').get_url(None)
                producto.save()
                return redirect(listado_productos)
            else:
                messages.error(request, 'El producto tiene campos incompletos')
                return redirect("create")

        elif ('name' in request.POST):  # It is used for categories
            formCategory = VistaCrearCategoria(request.POST)

            if formCategory.is_valid():
                formCategory.save()
                return redirect("create")
            else:
                messages.error(request, 'La categoria ya existe')
                return redirect("create")
    else:
        formCategory = VistaCrearCategoria()
        formProducto = VistaCrearProducto()
        return render(request, "products/create.html", {"formCategory": formCategory, "formProduct": formProducto})


def nameImages(*args):
    return "_".join(args)