from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=99999999, decimal_places=2)
    image = models.ImageField(default='default.png')


    def __str__(self):
        return self.name

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True )
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField()


    def __str__(self):
        return str(self.user.username)
    

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    

    def __str__(self):
        return f"Orderby: {self.customer.name}"
    
    @property
    def cart_total_price(self):
        orderitems = self.orderitems.all()
        total = sum([item.total for item in orderitems])
        return total
    

    @property
    def cart_total_item(self):
        orderitems = self.orderitems.all()
        total = sum([item.quantity for item in orderitems])
        return total
    


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, related_name='orderitems')
    quantity  = models.IntegerField(default=0, null=True)   

    def __str__(self):
        return self.product.name
    
    @property
    def total(self):
        total_price = self.product.price * self.quantity
        return total_price


class Shipping(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=200)
    city= models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    aipcode = models.CharField(max_length=200)


    def __str__(self):
        return self.address
    



