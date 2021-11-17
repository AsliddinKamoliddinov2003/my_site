from django.urls import path
from .views import *



urlpatterns = [
    path("", index, name="index"),
    path("detail/<int:pk>/", detail, name="detail"),
    path("nextdetail/<int:pk>/", nextdetail, name="nextdetail"),
    path("previousdetail/<int:pk>/", previousdetail, name="previousdetail"),
    path("about/", about, name="about"),
    path("profil/", profil, name="profil"),
    path("list/", list, name="list"),
    path("create/", createblog, name="create-blog"),
    path("update/<int:pk>/", updateblog, name="update-blog"),
    path("delete/<int:pk>/", deleteblog, name="delete-blog"),
]