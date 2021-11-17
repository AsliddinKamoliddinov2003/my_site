from django.shortcuts import redirect, render
from django.urls import reverse

from project.forms import BlogForm
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


def list(request):
    blogs = Blog.objects.all()
    context = {
        "blogs":blogs,
    }
    return render(request, "forms/list.html", context)


def createblog(request):
    form = BlogForm()
    if request.method=="POST":
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse("list"))
    context = {
        "form":form
    }
    return render(request, "forms/create.html", context)


def updateblog(request, pk):
    blog = Blog.objects.filter(id=pk)
    if not blog.exists():
        return redirect(reverse("list"))
    else:
        blog = blog.first()
    form = BlogForm(instance=blog)

    if request.method=="POST":
        form = BlogForm(request.POST, request.FILES, instance = blog)
        if form.is_valid():
            form.save()
            return redirect(reverse("list"))
    context = {
        "form":form
    }
    return render(request, "forms/update.html", context)


def deleteblog(request, pk):
    try:
        blog = Blog.objects.get(id=pk)
        blog.delete()
    except Blog.DoesNotExist:
        pass
    return redirect(reverse("list"))



