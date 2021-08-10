from django.db import models


# Create your models here.
class Product(models.Model):
    """
    This class represents a product
    with name, description, and
    price
    """
    name = models.CharField(max_length=80)
    description = models.CharField(max_length=200)
    price = models.FloatField(max_length=11)
