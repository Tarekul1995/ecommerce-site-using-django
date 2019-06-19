from decimal import Decimal
from django.shortcuts import get_object_or_404, redirect, render
from Product.models import Product
from django.contrib import messages
from .models import Createcart
from Account.models import Customer_Account


def add_cart(request, object_id):
    item = get_object_or_404(Product, pk=object_id)

    if request.session.has_key('username'):
        user_name = Customer_Account.objects.get(name=request.session['username'])
        try:
            cart = Createcart.objects.get(user=user_name)
            if item in cart.products.all():
                messages.warning(request, 'Warning : Item already Added')
            else:
                cart.products.add(item)

        except Exception as e:
            cart = Createcart(user=user_name)
            cart.save()
            cart.products.add(item)
        return redirect('product:home')


def total_price_fn(quantity, product_price):
    return Decimal(quantity) * product_price


def cart_detail(request):
    item = None
    quantity_list = []
    if request.session.has_key('username'):
        username = request.session['username']
        user_name = Customer_Account.objects.get(name=request.session['username'])
        cart = Createcart.objects.get(user=user_name)
        item = cart.products.all()
        product_price = [Decimal(pice.price) for pice in item]
    if request.method == 'POST':
        for i in range(len(item)):
            quantity_list.append(request.POST['quantity' + str(i + 1)])
        request.session['quantity'] = quantity_list
        request.session.modified = True
        total_price = list(map(total_price_fn, request.session['quantity'], product_price))
    else:
        if request.session.has_key('quantity'):
            quantity_list = request.session['quantity']
            while len(item) != len(quantity_list):
                quantity_list.append('1')
            total_price = list(map(total_price_fn, quantity_list, product_price))
        else:
            while len(item) != len(quantity_list):
                quantity_list.append('1')
            total_price = list(map(total_price_fn, quantity_list, product_price))
    if request.session.has_key('quantity') and len(request.session['quantity']) == len(item):
        context = [{'items': t[0], 'quantity': t[1], 'total_price': t[2]} for t in
                   zip(item, request.session['quantity'], total_price)]
    else:
        context = [{'items': t[0], 'quantity': t[1], 'total_price': t[2]} for t in
                   zip(item, quantity_list, total_price)]
    print(request.session['quantity'])
    return render(request, 'Cart/cart_detail.html', {'context': context, 'username': username, 'total_price': sum(total_price)})


def cart_remove(request, object_id, index):
    if request.session.has_key('username'):
        p_remove = Product.objects.get(id=object_id)
        user_name = Customer_Account.objects.get(name=request.session['username'])
        cart = Createcart.objects.get(user=user_name)
        cart.products.remove(p_remove)
    if request.session.has_key('quantity'):
        request.session['quantity'].pop(index-1)
        request.session.modified = True

    return redirect('cart:cart_detail')
