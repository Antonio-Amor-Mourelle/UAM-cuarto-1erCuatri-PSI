# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
Category(catName, catSlug)
catName  => string, not null, unique
catSlug  => string, not null, unique % usa en Django un SlugField


class Category(models.Model):
    catName=model.CharField(max_length=128, unique=True)#not null???
    catSlug=model.CharField(max_length=128, unique=True)#not null???

    def _str_(self):
        return self.catName + self.catSlug
    def unicode(self):
        return self.catName + self.catSlug


class Product(models.Model):
    ##cat= Category()##
    category = models.ForeignKey(Category)
    prodName = models.CharField(unique=True)
    prodSlug = models.SlugField(unique=True)
