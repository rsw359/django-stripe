from unicodedata import name
from django.db import models

class Product(models.Model):
  name = models.CharField(max_length=100)
  price = models.IntegerField(default=0) # cents, can use decimal field or float

  def __str__(self):
    return self.name
