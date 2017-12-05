from __future__ import unicode_literals
from django.contrib import admin

# Register your models here.

from placeorder.models import Order, Orderline

# Register your models here.
class OrderAdmin(admin.ModelAdmin):
    list_display = ("firstName", "familyName", "email", "address", "zip",
                    "city", "created", "updated", "paid")
    
class OrderlineAdmin(admin.ModelAdmin):
    list_display = ("order", "product", "unit", "pricePerUnit")
    
admin.site.register(Order, OrderAdmin)
admin.site.register(Orderline, OrderlineAdmin)