
# Create your models here.
from django.db import models
from django.db.models.fields import BigAutoField, CharField, DateField, EmailField
from django.http import request

# Create your models here.
class User(models.Model):


    first_name=models.CharField(max_length=10)
    last_name=models.CharField(max_length=10)
    age=models.PositiveSmallIntegerField() 
    email=models.EmailField(max_length=30)
    passport_photo=models.ImageField(upload_to= "images/" ,null=True,blank=True)
    password=models.CharField(max_length=10)


class RegisteredUser(models.Model):
    User.email=models.ForeignKey(User,on_delete=models.CASCADE)
    User.password=models.ForeignKey(User,on_delete=models.CASCADE)