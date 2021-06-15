from django import forms
from django.forms import ModelForm
from .models import Tag

class TagForm(ModelForm):
    class Meta:
        model = Tag
        fields = ['name']