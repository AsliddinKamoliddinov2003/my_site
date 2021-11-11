from project.models import *


def context(request):
    post = Blog.objects.all().first()
    return {
        "post":post,
    }