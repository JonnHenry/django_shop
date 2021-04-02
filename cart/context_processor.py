from .cart import Cart

def cart_total_amount(request):
    total = 0.0
    cart = request.session.get("cart")
    if cart is None:
        cart = Cart(request)
        cart.save()
    else:
        if request.user.is_authenticated:
            for key, value in request.session['cart'].items():
                total = total + (float(value['price']) * value['quantity'])
    return {'cart_total_amount': total}
