from django.shortcuts import render,redirect
from forms import OrderCreateForm
from models import Order, OrderLine
from forms import OrderCreateForm
from shoppingcart.shoppingcart import ShoppingCart
from django.db.utils import IntegrityError
from django.core.exceptions import ValidationError

# Create your views here.
def createOrder(request):
    form = OrderCreateForm()
    return render(request, 'placeorder/createOrder.html', {'form': form})

def confirmOrder(request):
    shoppingcart = ShoppingCart(request)
    
    if request.method =='POST':
        form=OrderCreateForm(request.POST)               

    else:
        form=OrderCreateForm()
    
    if form.is_valid():
        try:
            order = form.save(commit=True)
            for item in shoppingcart:
                product=item["product"];
                product.stock -= item["units"];
                product.save()
                OrderLine.objects.get_or_create(order=order, product=item["product"], 
                                                units=item["units"], pricePerUnit=item["price"])
        except IntegrityError:
            error = "Error creating order"
            return render(request, "placeorder/createOrder.html", {"form": form, "error": error})
            
        except ValidationError:
            error="Product stock isn't enough"
            return render(request, "placeorder/createOrder.html", {"form": form, "error": error})
    else:
        return render(request, "placeorder/createOrder.html", {"form": form})
    
    shoppingcart.clear()
    return render(request, "placeorder/confirmOrder.html", {"ordernumber": order.id})
