from django.shortcuts import redirect, render
from django.urls import reverse

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


def nextdetail(request, pk):
    pk = pk + 1 
    post = Blog.objects.filter(id=pk)
    if post.exists():
        post = Blog.objects.get(id=pk)
        if post:
            context = {
                "post":post
            }
    else:
        return redirect(reverse("index"))
    return render(request, "detail.html", context)


def previousdetail(request, pk):
    pk = pk - 1 
    post = Blog.objects.filter(id=pk)
    if post.exists():
        post = Blog.objects.get(id=pk)
        if post:
            context = {
                "post":post
            }
    else:
        return redirect(reverse("index"))
    return render(request, "detail.html", context)


def about(request):
    post = AboutMe.objects.all().first()
    print(post)
    context = {
        "post":post,
    }
    return render(request, "about.html", context)


def profil(request):
    return render(request, "profil.html")