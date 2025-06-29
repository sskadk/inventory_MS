from django.db import models

# Create your models here.
class ProductType(models.Model):
    name = models.CharField(max_length=300)

class Product(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField()
    price = models.FloatField()
    stock = models.IntegerField()
    type = models.ForeignKey(ProductType, on_delete=models.SET_NULL,null=True)
    department = models.ManyToManyField('Department', blank=True)

class Purchase(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.FloatField()
    vendor = models.ForeignKey('Vendor',on_delete=models.CASCADE)

class Sell(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.FloatField()
    customer = models.ForeignKey('Customer',on_delete=models.CASCADE)

class Customer(models.Model):
    name = models.CharField(max_length=300)
    email = models.EmailField()
    number = models.CharField(max_length=15)
    address = models.CharField(max_length=300)

class Vendor(models.Model):
    name = models.CharField(max_length=300)
    company_name = models.CharField(max_length=300)
    email = models.EmailField()
    number = models.CharField(max_length=15)
    company_address = models.CharField(max_length=300)

class Department(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    floor = models.IntegerField()