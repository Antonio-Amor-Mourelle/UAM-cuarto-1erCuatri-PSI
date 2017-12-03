from django.shortcuts import render
from django.shortcuts import redirect
from shoppingcart import ShoppingCart
from forms import CartAddProductForm
from shop.models import Product

# Create your views here.
def shoppingcart_list (request) :
    shoppingcart = ShoppingCart(request)
    return render(request, 'shoppingcart/list.html',{'shoppingcart': shoppingcart})


def shoppingcart_add(request, prod_id):
    shoppingcart= ShoppingCart(request)
    try:
        product=Product.objects.get(id=prod_id)
        
    except Product.DoesNotExist:
        product = None
        
    if request.method =='POST':
        form=CartAddProductForm(request.POST, prod_id)               

    else:
        form=CartAddProductForm(prod_id)

    if form.is_valid():
        if product: 
            units=form.cleaned_data['units']
            update_units=form.cleaned_data['update']
            shoppingcart.addProduct(product=product,
                            units=units,
                            update_units=update_units)                       
            shoppingcart.saveCart()
    else:
        print(form.errors)
            
    
    
    return redirect('shoppingcart_list')

def shoppingcart_remove(request, prod_id):
    shoppingcart= ShoppingCart(request)

    try:
        product=Product.objects.get(id=prod_id)
        shoppingcart.removeProduct(product=product)
        shoppingcart.saveCart()
        
    except Product.DoesNotExist:
        product = None
    
    return redirect('shoppingcart_list')

