# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.template.defaultfilters import slugify
from django.utils.timezone import now

# Create your models here.
class Category(models.Model):
    catName=models.CharField(max_length=128, unique=True, null=False)#not null???
    catSlug=models.SlugField(max_length=128, unique=True, null=False)#not null???
    
    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.catName
    def __unicode__(self):
        return self.catName

    def save(self, *args, **kwargs):
        self.catSlug = slugify(self.catName)
        super(Category, self).save(*args, **kwargs)


class Product(models.Model):
    ##cat= Category()##
    category = models.ForeignKey(Category)
    prodName = models.CharField(max_length=128, null=False, unique=True)
    prodSlug = models.SlugField(max_length=128, null=False, unique=True)
    image = models.ImageField(upload_to = 'images/products')
    description = models.TextField(max_length=1024, null=False)
    price = models.DecimalField(decimal_places=2, max_digits=5, null=False)
    stock = models.IntegerField(default=0)
    availability = models.BooleanField(default=True)
    created = models.DateTimeField(default=now)
    updated = models.DateTimeField(default=now)

    def __str__(self):
        return self.prodName
    def __unicode__(self):
        return self.prodName

    
    def save(self, *args, **kwargs):
        self.prodSlug = slugify(self.prodName)
        super(Product, self).save(*args, **kwargs)
