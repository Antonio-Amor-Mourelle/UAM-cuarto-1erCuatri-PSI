from __future__ import unicode_literals

from django.db import models
from shop.models import Product

# Create your models here.
class Order(models.Model):
    pass

class Orderline(models.Model):
    order=models.ForeignKey(Order, related_name='orderLines', null=False)
    product=models.ForeignKey(Product, related_name='productLines', null=False)
    unit=models.IntegerField(default=0, null=False)
    pricePerUnit=models.DecimalField()
    
    def __str__(self):
        return self.order + self.product
    def __unicode__(self):
        return self.order + self.product
    