from email.mime import message
from django.shortcuts import redirect, render,HttpResponse,get_object_or_404
from matplotlib.style import context
from sqlalchemy import false

import article
from .forms import ArticleForm
from .models import Article
from django.contrib import messages

# Create your views here.

def about(request):
    return render(request,"about.html")
def dashboard(request):
     articles = Article.objects.filter(author = request.user)
     context = {
          "articles" : articles
     }
     return render(request,"dashboard.html",context)
def index(request):
     return render(request,"index.html")
def addArticle(request):
     form = ArticleForm(request.POST or None)
     if form.is_valid():
          article = form.save(commit=False)
          article.author = request.user
          article.save()

          messages.success(request,"Makale Başarıyla oluşturuldu")
          return redirect("index")
     return render(request,"addarticle.html",{"form":form})
def detail(request,id):
    # article = Article.objects.filter(id = id).first()
     article = get_object_or_404(Article,id = id)
     return render(request,"detail.html",{"article":article})
