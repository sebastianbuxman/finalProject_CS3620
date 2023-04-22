from django.db import models


# Create your models here.
class Clothing(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=50, default=" ")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='Images', default='images/none/noimg.jpg')
    desc = models.CharField(max_length=500, default="")


class User(models.Model):
    def __str__(self):
        return self.userName

    userName = models.CharField(max_length=500, default="")
    address = models.CharField(max_length=500, default="")
    email = models.EmailField(max_length=100, default="")
    pNumber = models.CharField(max_length=100, default="")
