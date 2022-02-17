from django.db import models


# Create your models here.
class Person(models.Model):
    username = models.CharField(max_length=25)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)
    cpassword = models.CharField(max_length=50)

class News(models.Model):
    email = models.EmailField(max_length=25)
    address = models.CharField(max_length=25)
    address2 = models.CharField(max_length=25)
    city = models.CharField(max_length=50)
    zip = models.IntegerField()
    check=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    password = models.CharField(max_length=50)


