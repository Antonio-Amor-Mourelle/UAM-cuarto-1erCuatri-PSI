from django.shortcuts import render
from shoppingcart import ShoppingCart

# Create your views here.
def shoppingcart_list (request) :
    shoppingcart = ShoppingCart(request)
    return render(request, 'shoppingcart/list.html',{'shoppingcart': shoppingcart})