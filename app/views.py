from django.shortcuts import render
from .models import *


def index(request):
    baner = Baner.objects.all()
    context = {
        "baner" : baner
    }
    return render(request, "index.html",context)


def about(request):
    return render(request, "about.html" )
    
def projects(request):
    return render(request, "project.html" )    


def services(request):
    return render(request, "services.html")

def blog(request):
    return render(request, "blog.html" )    

def contact(request):
    return render(request, "contact.html" )

def blog(request):
    return render(request,"blog.html")







