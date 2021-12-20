from django.db import models
from django.db.models.fields import CharField


class Login(models.Model):
    username = models.CharField(max_length=255,blank=True,null=True)
    password = models.CharField(max_length=255,blank=True,null=True)
    
    def __str__(self):
        return self.username 
        