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

def populate():
    products = {}
    names = ["nevera", "frigorifico", "cafetera"]
    
    
    for name in names:  
        products[name] = []
        for i in range(1,7):
            dict = {}
            dict["prodName"] = name + " %d" % i
            dict["image"] = "nevera.jpg"
            dict["description"] = generate_paragraph()[2]
            dict["price"] = uniform(50, 999)
            products[name].append(dict)
        
    cats = {
            "neveras": {"products": products["nevera"]},
            "frigorificos": {"products": products["frigorifico"]},
            "cafeteras": {"products": products["cafetera"]},
            }
    
    for cat, cat_data in cats.items():
        c = add_cat(cat)
        for p in cat_data["products"]:
            add_prod(c, p["prodName"], p["image"], p["description"],
                        p["price"])


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

    
    
    
    
    
    
    