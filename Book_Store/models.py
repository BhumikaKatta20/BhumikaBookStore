from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class User_customer(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
	Address = models.CharField(max_length=150, default='')
	city = models.CharField(max_length=50, default='')
	State = models.CharField(max_length=50, default='')
	Postal_code= models.IntegerField(default=0)
	Phone_number = models.IntegerField(default=0)
class StoreUser(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
	Address = models.CharField(max_length=150, default='')
	city = models.CharField(max_length=50, default='')
	State = models.CharField(max_length=50, default='')
	Postal_code= models.IntegerField(default=0)
	Phone_number = models.IntegerField(default=0)
class StoreBook(models.Model):
	Storeuser=models.CharField(max_length=50, default='')
	Book=models.CharField(max_length=50, default='')
	Author= models.CharField(max_length=50, default='')
	Quantity=models.IntegerField(default=0)
	first_name=  models.CharField(max_length=50, default='')
	last_name=  models.CharField(max_length=50, default='')
