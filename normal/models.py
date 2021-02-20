from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
# Create your models here.


class Offer(models.Model):
    image=models.ImageField(null=True,blank=True)
    name=models.CharField(max_length=100)
    price=models.FloatField(max_length=100)

    

class Customer(models.Model):#user profile
    user=models.OneToOneField(User,null=True,blank=True,on_delete=models.CASCADE)
    name=models.CharField(max_length=100,null=True)
    email=models.CharField(max_length=100)
    #def __str__(self):
     #   return self.name

   
    
class Product(models.Model): #product
    name=models.CharField(max_length=100)
    price=models.FloatField(max_length=100)
    digital=models.BooleanField(default=False, null=True)
    image=models.ImageField(null=True,blank=True)

    #def __str__(self):      
     #   return self.name

    @property
    def imageURl(self):
        try:
            url=self.image.url
        except:
            url=''
        return url

    

class Order(models.Model):
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE,null=True,blank=True)
    date_of_order=models.DateTimeField(auto_now_add=True)
    complete=models.BooleanField(default=False)
    transition_id=models.CharField(max_length=100,null=True)
    #def __str__(self):
     #   return str(self.id)
    
        
    

class OrderItem(models.Model):#
    Product=models.ForeignKey(Product, on_delete=models.CASCADE,null=True,blank=True)
    Quantity=models.IntegerField(default=0,null=True)
    #def __str__(self):
     #   return self

class ShippingAddress(models.Model):
    name=models.ForeignKey(Customer,on_delete=models.CASCADE,null=True)
    Order=models.ForeignKey(Order,on_delete=models.CASCADE,null=True)
    Address=models.CharField(max_length=200)
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    zipcode=models.IntegerField()
    #def __str__(self):
     #   return self.addresss

