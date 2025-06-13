from django.db import models

class User(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=300)
    username = models.CharField(max_length=300)
    phone_no = models.IntegerField(max_length=10, null=True)
    address = models.CharField(max_length=300,null=True)

class Product(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField()
    stock = models.IntegerField()

class Customer(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    number = models.CharField(max_length=20)
    address = models.CharField(max_length=200)

class Supplier(models.Model):
    name = models.CharField(max_length=300)
    contact = models.IntegerField(max_length=10)
    address = models.CharField(max_length=300)
    email = models.EmailField()

class Purchase(models.Model):
    quantity = models.IntegerField()
    price  = models.IntegerField()
    product = models.ForeignKey(Product)
    supplier = models.ForeignKey(Supplier)

class Sale(models.Model):
    quantity = models.IntegerField()
    price  = models.IntegerField()
    product = models.ForeignKey(Product)
    customer = models.ForeignKey(Supplier)
