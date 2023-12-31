from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify


class Category(models.Model):
   name = models.CharField(max_length= 65)
    

   def __str__(self):
     return self.name


class Mural(models.Model):
 

 #cards
 title = models.CharField(max_length=65)
 description = models.CharField(max_length=165)
 contact = models.CharField(max_length=165)
 created_at = models.DateTimeField(auto_now_add=True)
 is_published = models.BooleanField(default=False)
 categoria = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
 usuario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
 oferece_ajuda = models.BooleanField(default=False)



