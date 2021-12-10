from django.db import models
from django.db.models.base import Model
from django.db.models.fields import CharField


class Product(models.Model):
    product_name = models.CharField(max_length=255)
    unit_sold = models.IntegerField(null=True,blank=True)
    in_stock = models.IntegerField(null=True,blank=True)
    description = models.TextField(null=True,blank=True)
    exp_date = models.DateField(null=True,blank=True)
    category = models.ForeignKey("product.Category",on_delete=models.CASCADE,null=True,blank=True)
    image = models.ImageField(upload_to="media/products",null=True,blank=True)
    
    def __str__(self):
        return self.product_name


class Category(models.Model):
    name = CharField(max_length=255)

    def __str__(self):
        return  self.name


