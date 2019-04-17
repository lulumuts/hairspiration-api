from django.db import models
from django.conf import settings
import os
# Create your models here.
class Type(models.Model):
    name=models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Hairstyle(models.Model):

    image = models.ImageField(upload_to="")
    type=models.ForeignKey(Type, on_delete=models.CASCADE)



class Hairstylist(models.Model):
    name=models.CharField(max_length=200)
    image = models.ImageField(upload_to="")
    type=models.ManyToManyField('type')

    def __str__(self):
        return self.name

class Products(models.Model):

    image = models.ImageField(upload_to="", blank=True)
    brand = models.CharField(max_length=200)

    def __str__(self):
        return self.brand
