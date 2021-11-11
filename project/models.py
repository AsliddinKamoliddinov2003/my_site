from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField



class Blog(models.Model):
    title = models.CharField(max_length=255)
    body = RichTextUploadingField(blank=True, null=True)
    image = models.ImageField(upload_to="images/", null=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class AboutMe(models.Model):
    body = RichTextUploadingField(blank=True, null=True)
    image = models.ImageField(upload_to="images/", null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Profil(models.Model):
    image = models.ImageField(upload_to="images/", null=True)
    github_link = models.CharField(max_length=255, null=True)
    telegram_link = models.CharField(max_length=255, null=True)
    linkedin_link = models.CharField(max_length=255, null=True)
    facebook_link = models.CharField(max_length=255, null=True)
    instagram_link = models.CharField(max_length=255, null=True)
