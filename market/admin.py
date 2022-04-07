from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Customer)
admin.site.register(Vendor)
admin.site.register(VendorProduct)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderedItem)
admin.site.register(ShippingAddress)




