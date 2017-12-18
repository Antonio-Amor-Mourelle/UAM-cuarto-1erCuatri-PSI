from __future__ import unicode_literals

from django.db import models
from shop.models import Product
from django.utils.timezone import now

# Create your models here.
class Order(models.Model):
    """
    Clase que define un pedido de un usuario
    Autor: Antonio Amor
    """
    firstName=models.CharField(max_length=50, unique=False, null=False)
    familyName=models.CharField(max_length=50, unique=False, null=False)
    email=models.EmailField()
    address=models.CharField(max_length=50, unique=False, null=False)
    zip=models.CharField(max_length=20, unique=False, null=False)#postal code
    city=models.CharField(max_length=50, unique=False, null=False)#postal code
    created=models.DateTimeField(default=now)
    updated=models.DateTimeField(default=now)
    paid=models.BooleanField(default=False)
    
    def __str__(self):
        return "%d" % self.id
    def __unicode__(self):
        return "%d" % self.id
    
    def getTotalCost(self):
        total=0
        for orderline in OrderLine.objects.filter(order=self):
            total+=orderline.getProductCost()
        return total
            
        

class OrderLine(models.Model):
    """
    Define la informacion que tiene el detalle de un pedido
    Autor: Esther Lopez    
    """
    order=models.ForeignKey(Order, related_name='orderLines', null=False)
    product=models.ForeignKey(Product, related_name='productLines', null=False)
    units=models.IntegerField(default=0, null=False)
    pricePerUnit=models.DecimalField(decimal_places=2, max_digits=5)
    
    def __str__(self):
        return self.order.__str__() + " " + self.product.__str__()
    def __unicode__(self):
        return self.order.__unicode__() + " " + self.product.__unicode__()
    
    def getProductCost(self):
        return self.pricePerUnit * self.units

