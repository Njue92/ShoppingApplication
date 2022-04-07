from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Customer(models.Model):
    customer = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=40, blank=True, null=True)
    mobile = models.CharField(max_length=15, null=True)

    def __str__(self):
        return self.name


class Vendor(models.Model):
    name= models.CharField( max_length=100, null=True, blank=False)
    location= models.CharField( max_length=100, null=True, blank=False)
    business_type= models.CharField(max_length=80, null=True)
    mobile= models.CharField( max_length=100, null=True, blank=False)

    def __str__(self):
        return self.name


class VendorProduct(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.SET_NULL, blank=True, null=True)
    product_name = models.CharField(max_length=50, null=True)
    product_price = models.FloatField()
    # image =

    def __str__(self):
        return self.vendor


class Product(models.Model):
    name = models.CharField(max_length=50, null=True)
    price = models.FloatField()
    digital = models.BooleanField(default=False, null=True, blank=False)
    # image =

    def __str__(self):
        return self.name


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True )
    date_ordered = models.DateField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=False)
    transaction_id = models.CharField(max_length=100, null=True)

    def __str__(self):
        return str(self.id)


class OrderedItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateField(auto_now_add=True)


class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True )
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True )
    date_added = models.DateField(auto_now_add=True)
    city = models.CharField(max_length=200, null=False)
    location = models.CharField(max_length=200, null=False)
    nearest_location = models.CharField(max_length=300, null=True)

    def __str__(self):
        return self.location

