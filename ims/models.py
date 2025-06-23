from django.db import models

class ProductType(models.Model):
    name = models.CharField(max_length=300)

class Product(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    stock = models.IntegerField()
    type = models.ForeignKey(ProductType, on_delete=models.SET_NULL, null=True)
    department = models.ManyToManyField('Department')
    
class Purchase(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.FloatField()
    vendor = models.ForeignKey('Vendor', on_delete=models.CASCADE)

class Sell(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE)

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
    comapny_address = models.CharField(max_length=300)

class Department(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField()
    floor = models.IntegerField()

 