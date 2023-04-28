from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


# Create your models here.
class Clothing(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=50, default=" ")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='Images/', default='images/none/noimg.jpg')
    desc = models.CharField(max_length=500, default="")


'''class User(models.Model):
    def __str__(self):
        return self.userName

    email = models.CharField(max_length=500, default="")
    password = models.(max_length=100, default="")'''


class Payment(models.Model):
    def __str__(self):
        return self.cardHolder

    cardHolder = models.CharField(max_length=500, default=" ")
    cardNumber = models.IntegerField()
    expDate = models.DateField(auto_now_add=False)
    cvv = models.IntegerField()
    address = models.CharField(max_length= 1000, default="")