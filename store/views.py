from django.shortcuts import render
from .models import *


def catalog(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'store/catalog.html', context)


def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}
    context = {'items':items, 'order':order}
    return render(request, 'store/cart.html', context)


def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}
    context = {'items': items, 'order': order}
    return render(request, 'store/checkout.html', context)


def catalog_silver(request):
    products = Product.objects.filter(category = "Срібло")
    context = {'products': products}
    return render(request, 'store/catalog_silver.html', context)


def catalog_gold(request):
    products = Product.objects.filter(category = "Золото")
    context = {'products': products}
    return render(request, 'store/catalog_gold.html', context)