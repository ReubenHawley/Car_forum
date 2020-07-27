from django.shortcuts import render
from .models import Post


def home(request):
    context = {
        "posts": Post.objects.all()
    }
    return render(request, "forum/Home.html", context)
# Create your views here.


def about(request):
    context = {
        "posts": Post.objects.all()
    }
    return render(request, "forum/About.html",context)


def Mycar(request):
    context = {
        "posts": Post.objects.all()
    }
    return render(request, "forum/Mycar.html", context)
