from django.shortcuts import render

# Create your views here.
def createOrder(request):
    return render(request, 'placeorder/createOrder.html')
