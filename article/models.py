from pyexpat import model
from django.db import models
from sympy import content

# Create your models here.


class Article(models.Model):
    author = models.ForeignKey("auth.User",on_delete = models.CASCADE ) #model.cascade amacı yazar silinirse makaleyi de sil demek
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    
