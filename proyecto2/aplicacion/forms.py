from django import forms

from .models import PostModel
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class PostModelForm(forms.ModelForm):
    class Meta:
        model = PostModel
        fields = [
            'title',
            'content'
        ]
