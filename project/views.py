from django.shortcuts import render

from .models import *


def index(request):
    posts = Blog.objects.all()
    context = {
        'posts':posts
    }
    return render(request, "index.html", context)



def detail(request, pk):
    post = Blog.objects.get(id=pk)
    context = {
        "post":post
    }
    return render(request, "detail.html", context)


def about(request):
    post = AboutMe.objects.all().first()
    context = {
        "post":post,
    }
    return render(request, "about.html", context)


def profil(request):
    link = Profil.objects.all()
    context = {
        "link":link,
    }
    return render(request, "profil.html", context)