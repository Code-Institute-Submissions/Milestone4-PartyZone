from django.shortcuts import render, redirect, reverse
from products.models import Theme

# Create your views here.
def view_cart(request):
    """A View that renders the cart contents page"""
    categories = Theme.objects.all()
    return render(request, "cart.html", {"categories": categories})


def add_to_cart(request, id):
    """Add a quantity of the specified product to the cart"""
    quantity = int(request.POST.get('quantity'))
    
    str_x = request.POST.get('select')
    cart = request.session.get('cart', {})

    if str_x == "add":
        
        if cart.get(id) is not None:
            temp = cart.get(id)
            print(temp)
        else:
            temp = 0
            
        if quantity > 0:
            cart[id] = quantity + temp
            print(cart[id])
    else:
        cart.pop(id)

    request.session['cart'] = cart
    return redirect(reverse('index'))


def adjust_cart(request, id):
    """
    Adjust the quantity of the specified product to the specified
    amount
    """
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[id] = quantity
    else:
        cart.pop(id)
    
    request.session['cart'] = cart
    return redirect(reverse('view_cart'))
