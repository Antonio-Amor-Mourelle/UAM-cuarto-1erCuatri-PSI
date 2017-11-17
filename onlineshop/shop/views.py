from django.shortcuts import render
from shop.models import Category, Product

# Create your views here.
def base(request):
    return render(request, 'shop/base.html')
    
def product_list(request, catSlug=None):
    #Your code goes here
    #queries that fill, category, categories and products
    categories = Category.objects.all()

    
    if catSlug:
        try: 
            category = Category.objects.get(catSlug=catSlug)
            products = Product.objects.filter(category=category)
        except:
            category = None
            products = None
    else:
        products = []
        for category in categories:
            products += Product.objects.filter(category=category)
            
        category = None
        

    return render(request,'shop/list.html',
    {'category': category,
    'categories': categories,
    'products': products})
    
def product_detail(request, id, prodSlug):
    #Your code goes here
    #query that returns a product with id=protId
    try:
        product = Product.objects.get(prodSlug=prodSlug, id=id)
    except:
        product = None
        
    return render(request, 'shop/detail.html', {'product': product})