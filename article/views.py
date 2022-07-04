from django.shortcuts import render,HttpResponse

# Create your views here.

def index(request):
    context = {
        "number1":20
            }
    return render(request,"index.html",context)

def about(request):
    return render(request,"about.html")

