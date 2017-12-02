from django.shortcuts import render
from shoppingcart import ShoppingCart

# Create your views here.
def shoppingcart_list (request) :
    shoppingcart = ShoppingCart(request)
    return render(request, 'shoppingcart/list.html',{'shoppingcart': shoppingcart})

def shoppingcart_add(request, prod_id):
    shoppingcart= ShoppingCart(request)

    ?????


    if request.method =='POST':
        form=CartAddProductForm(resquest.POST, prod_id)
        if form.is_valid():
            ????

    else:


    ??????

    shoppingcart.addProduct(product=product,
                            units=units,
                            update_quantity=update_units)
    return redirect('shoppingcart_list')

def shoppingcart_remove(request):
    shoppingcart= ShoppingCart(request)

    ?????

    if request.method =='POST':
        form=CartRemoveProductForm(resquest.POST, prod_id)
        if form.is_valid():
            ????

    else:


    ????


    shoppingcart.removeProduct(product=product)
    return redirect('shoppingcart_list')

def shoppingcart_list(request):

    return
