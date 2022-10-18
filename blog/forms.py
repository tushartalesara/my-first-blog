from pyexpat import model
from socket import fromshare
from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=('title','text',)