from django import forms
from django.forms import fields

from project.models import Blog



class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ["title", "body"]

    def __init__(self, *args, **kwargs):
        super(BlogForm,self).__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs["class"] = "form-control"


