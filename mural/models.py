from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
   name = models.CharField(max_length= 65)
    

   def __str__(self):
     return self.name


class Mural(models.Model):
 
 #cadastrar / login
 name = models.CharField(max_length=65)
 password = models.CharField(max_length=165)
 email = models.TextField(max_length=120)

 #cards
 title = models.CharField(max_length=65)
 description = models.CharField(max_length=165)
 contact = models.IntegerField()
 created_at = models.DateTimeField(auto_now_add=True)
 urgencia = models.IntegerField()
 categoria = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
 usuario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

