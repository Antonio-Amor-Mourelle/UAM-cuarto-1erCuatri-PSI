from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Order(models.Model):
    firstName=models.CharField( unique=False, null=False)
    familyName=models.CharField( unique=False, null=False)
    email=models.EmailField()
    address=models.CharField(unique=False, null=False)
    zip=models.CharField(unique=False, null=False)#postal code
    city=models.CharField(unique=False, null=False)#postal code
    created=models.DateTimeField(default=now)
    updated=models.DateTimeField(default=now)
    paid=models.BooleanField(default=False)
