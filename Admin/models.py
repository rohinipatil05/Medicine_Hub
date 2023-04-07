from django.db import models
from datetime import datetime

#from django.contrib.admin.widgets import AdminDateWidget
#from django.forms.fields import DateField
#from django import forms

# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=30)
    
    def __str__(self):
        return self.category_name

    class Meta:
        db_table='Category'
    
class Product(models.Model):
    prod_name=models.CharField(max_length=20)
    category_id=models.ForeignKey(to='Category',on_delete= models.CASCADE)
    supplier_id=models.ForeignKey(to='Supplier',on_delete= models.CASCADE)
    prod_photo=models.ImageField(default = 'no_img.jpg' ,upload_to='images/product/')
    prod_price=models.IntegerField(default = 200)
    prod_quantity = models.IntegerField(default=1)
    prod_description=models.CharField(max_length=100)
    prod_treatment = models.CharField(max_length=100)
    prod_compostion = models.CharField(max_length=100)
    prod_type = models.CharField(max_length=50)
    prod_exp = models.CharField(max_length=50)

    def __str__(self):
        return self.prod_name
        
    class Meta:
        db_table='Product'
    
class UserInfo(models.Model):
    uname = models.CharField(max_length=20,primary_key=True)
    phone=models.BigIntegerField()
    email = models.EmailField(max_length = 100)
    password = models.CharField(max_length=20)
    class Meta:
        db_table = 'UserInfo'
        
class Supplier(models.Model):
    sname = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=20)
    mobile = models.BigIntegerField()
    email = models.EmailField(max_length=30)
    password = models.CharField(max_length=50)
        
    def __str__(self):
        return self.sname

    class Meta:
        db_table='Supplier'

class PaymentMaster(models.Model):
    cardno = models.CharField(max_length=20)
    cvv = models.CharField(max_length=4)
    expiry = models.CharField(max_length=20)
    balance = models.FloatField(default=10000)

    class Meta:
        db_table = "PaymentMaster"

class Contact(models.Model):
    uname = models.CharField(max_length=20,primary_key=True)
    email=models.EmailField(max_length=30)
    subject = models.EmailField(max_length = 25)
    messege = models.CharField(max_length=100)

    class Meta:
        db_table = 'Contact'

class Shipping(models.Model):
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    address = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    postal= models.CharField(max_length=10)
    phone= models.CharField(max_length=10)

    class Meta:
        db_table = 'Shipping'

        
