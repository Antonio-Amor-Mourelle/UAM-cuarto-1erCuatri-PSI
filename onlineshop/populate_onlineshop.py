#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'onlineshop.settings')

import django
django.setup()

from django.core.files import File
from django.db.utils import IntegrityError

from shop.models import Category, Product
from onlineshop.settings import MEDIA_ROOT
from loremipsum import generate_paragraph
from random import uniform

IMG_DIR = os.path.join(MEDIA_ROOT, 'shop')
"""
Funcion que puebla la base de datos con tres categorias y 6 productos por categoria
Autor: Antonio Amor Mourelle
"""
def populate():
    products = {}
    names = ["refrigerator", "washing-machine", "dishwasher"]
    cats = ["refrigerators", "washing machines", "dishwashers"]
    
    for j in range(3):  
        products[names[j]] = []
        for i in range(1,7):
            dict = {}
            dict["prodName"] = names[j] + "-%d" % i
            dict["image"] = cats[j] + "/" + names[j] + "-%d.jpg" % i
            dict["description"] = generate_paragraph()[2]
            dict["price"] = uniform(50, 999)
            products[names[j]].append(dict)
        
    cats = {
            "Refrigerators": {"products": products["refrigerator"]},
            "Washing machines": {"products": products["washing-machine"]},
            "Dishwashers": {"products": products["dishwasher"]},
            }
    
    for cat, cat_data in cats.items():
        c = add_cat(cat)
        for p in cat_data["products"]:
            add_prod(c, p["prodName"], p["image"], p["description"],
                        p["price"])

"""
Funcion que annade una cagtegoria a la base de datos
Entrada: name: Nombre de la categoria 
Autor: Esther Lopez Ramos
"""
def add_cat(name):
    try:
        c = Category.objects.get_or_create(catName=name)[0]
        return c
    except IntegrityError:
        print "Categoria duplicada"
        
    
"""
Funcion que annade un producto a la base de datos
Entrada: category: Categoria a la que pertenece el producto
	name: Nombre del producto
	img: Ruta de la imagen del producto dentro del directorio media
	description: descripcion del producto
	price: precio del producto
Autor: Esther Lopez Ramos
"""
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

    
    
    
    
    
    
    
