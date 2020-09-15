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
    price = models.FloatField()
    digital = models.BooleanField(default=False, null=True, blank=False)
    image = models.ImageField(upload_to='images', null=True, blank=True)

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ""
        return url

    def __str__(self):
        return self.name

class Order(models.Model):
    customer = models.ForeignKey(Customer, null=True, blank=True, on_delete=models.SET_NULL)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    transaction_id = models.CharField(null=True, max_length=254)

    def __str__(self):
        return str(self.id)

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total
    
    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total


class OrderItem(models.Model):
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    order = models.ForeignKey(Order, null=True, on_delete=models.SET_NULL)
    quantity = models.IntegerField(default=0, blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        return self.product.price * self.quantity

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
    