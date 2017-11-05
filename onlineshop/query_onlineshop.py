import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'onlineshop.settings')

import django
django.setup()

from django.core.files import File

from shop.models import Category, Product
from onlineshop.settings import MEDIA_ROOT
from django.db.utils import IntegrityError
from django.db.models import ObjectDoesNotExist

IMG_DIR = os.path.join(MEDIA_ROOT, 'shop')

def populate():
    ofertas_products = [
        {"prodName": "oferta 1",
         "image": "oferta1.jpg",
         "description": "Descripcion de la oferta 1",
         "price": 35,
         },
        {"prodName": "oferta 2",
         "image": "oferta2.jpg",
         "description": "Descripcion de la oferta 2",
         "price": 50,
         },
        {"prodName": "oferta 3",
         "image": "oferta3.jpg",
         "description": "Descripcion de la oferta 3",
         "price": 20,
         }]
    gangas_products = [
        {"prodName": "ganga 1",
         "image": "ganga1.jpg",
         "description": "Descripcion de la ganga 1",
         "price": 5,
         },
        {"prodName": "ganga 2",
         "image": "ganga2.jpg",
         "description": "Descripcion de la ganga 2",
         "price": 10,
         },
        {"prodName": "ganga 3",
         "image": "ganga3.jpg",
         "description": "Descripcion de la ganga 3",
         "price": 2,
         }]
        
    cats = {
            "ofertas": {"products": ofertas_products},
            "gangas": {"products": gangas_products},
            }
    
    for cat, cat_data in cats.items():
        c = add_cat(cat)
        for p in cat_data["products"]:
            add_prod(c, p["prodName"], p["image"], p["description"],
                        p["price"])
    for c in Category.objects.all():
        for p in Product.objects.filter(category=c):
            print("- {0} - {1}".format(str(c), str(p)))


def add_cat(name):
    try:
        c = Category.objects.get_or_create(catName=name)[0]
        return c
    except IntegrityError:
        print "Categoria duplicada"
        

def add_prod(category, name, img, description, price):
    try:
        imageObject = File(open(os.path.join(IMG_DIR, img), 'r'))
        p = Product.objects.get_or_create(category=category, prodName=name,
                                      description=description, price = price)[0];
        p.image.save(img, imageObject, save = True)
        return p
    except IntegrityError:
        print "Producto duplicado"

# Start execution here!
if __name__ == '__main__':
    print("Starting shop population script...")
    populate()
    
    # Queries
    print "Productos de la categoria gangas:"
    cat = Category.objects.get(catName="gangas")
    print Product.objects.filter(category=cat)
    
    print "Categoria de prodSlug=oferta-1"
    prod = Product.objects.get(prodSlug="oferta-1")
    print prod.category.catSlug
    
    
    try:
        print "Categoria de prodName=oferta_10"
        prod = Product.objects.get(prodName="oferta_10")
        print prod.category.catSlug
        
    except ObjectDoesNotExist:
        print "producto oferta_10 inexistente"
        
        

    
    
    
    
    
    
    