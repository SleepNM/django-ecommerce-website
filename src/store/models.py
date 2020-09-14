from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(null=True, max_length=254)
    email = models.EmailField(max_length=254)

    def __str__(self):
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length=254)
    price = models.FileField()
    digital = models.BooleanField(default=False, null=True, blank=False)
    #image

    def __str__(self):
        return self.name

class Order(models.Model):
    customer = models.ForeignKey(Customer, null=True, blank=True, on_delete=models.SET_NULL)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    transaction_id = models.CharField(null=True, max_length=254)

    def __str__(self):
        return str(self.id)
    
class OrderItem(models.Model):
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    order = models.ForeignKey(Order, null=True, on_delete=models.SET_NULL)
    quantity = models.IntegerField(default=0, blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, null=True, blank=True, on_delete=models.SET_NULL)
    order = models.ForeignKey(Order, null=True, on_delete=models.SET_NULL)
    address = models.CharField(null=False, max_length=254)
    city = models.CharField(null=False, max_length=254)
    state = models.CharField(null=False, max_length=254)
    zipcode = models.CharField(null=False, max_length=254)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address
    