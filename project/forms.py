from django.forms import ModelForm, fields
from .models import Blog

class Post(ModelForm):
    class Meta:
        model = Blog
        fields = ['body']