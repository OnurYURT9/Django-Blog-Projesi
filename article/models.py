from pyexpat import model
from django.db import models
from sympy import content
from ckeditor.fields import RichTextField
# Create your models here.


class Article(models.Model):
    author = models.ForeignKey("auth.User",on_delete = models.CASCADE,verbose_name="yazar" ) #model.cascade amacı yazar silinirse makaleyi de sil demek
    title = models.CharField(max_length=50,verbose_name="başlık")
    content = RichTextField()
    created_date = models.DateTimeField(auto_now_add=True,verbose_name="olusturma_tarih")
    article_image = models.FileField(blank = True,null=True,verbose_name="Fotoğraf ekleyin")
    def __str__ (self):
       return self.title
