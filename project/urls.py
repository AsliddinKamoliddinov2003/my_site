from django.urls import path

from .views import *

urlpatterns = [
    path("", index, name="index"),
    path("detail/<int:pk>/", detail, name="detail"),
    path("about/", about, name="about"),
    path("profil/", profil, name="profil"),
]