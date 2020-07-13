from django.db import models
from django.shortcuts import reverse

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=50,null=True)
    phone = models.IntegerField(null=True)
    email = models.EmailField(null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')
    

class Tag(models.Model):
    name = models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.name

class Product(models.Model):

    CHOICES = (
        ('Indoor','Indoor'),
        ('Outdoor','Outdoor'),
        ('Sports','Sports')
    )
    name = models.CharField(max_length=50,null=True)
    price = models.FloatField(null=True)
    description = models.CharField(max_length=50,null=True,blank=True)
    category = models.CharField(max_length=200,choices=CHOICES)
    date_created = models.DateTimeField(auto_now_add=True)
    tag = models.ManyToManyField(Tag)

    
    def get_absolute_url(self):
        return reverse('product')
    
    def __str__(self):
        return self.name
    
class Order(models.Model):
    STATUS = (
        ('Pending','Pending'),
        ('Delivered','Delivered'),
        ('Out for Delivery','Out for Delivery')
    )

    customer = models.ForeignKey(Customer,null=True,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,null=True,on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(null=True,max_length=200,choices=STATUS)

    def __str__(self):
        return self.product.name

    