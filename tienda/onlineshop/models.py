# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
Category(catName, catSlug)
catName  => string, not null, unique
catSlug  => string, not null, unique % usa en Django un SlugField


class Category(models.Model):
    catName=model.CharField(unique=True)#not null??? #add max_length?? dara eficiencia
    catSlug=model.CharField(unique=True)#not null???

    def _str_(self):
        return self.catName + self.catSlug
    def unicode(self):
        return self.catName + self.catSlug


class Product(models.Model):
    ##cat= Category()##
    category = models.ForeignKey(Category)
    prodName = models.CharField(unique=True)
    prodSlug = models.SlugField(unique=True)
    image = models.ImageField(upload_to= ' image/products')
    description = models.CharField()
    price = models.DecimalField(max_digits=5, decimal_places=2)# comprobar max_digits = 5
    stock = models.IntegerField(default=1)#not null
    availability = models.BooleanField(default=True)  #comprobar NO acepta NULLS
    created = models.DateTimeField(default=default=timezone.now) #ok
    updated = models.DateTimeField(default=default=timezone.now) #ok
