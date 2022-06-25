from django import forms
from .models import Categoria, Post

class formCat(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = '__all__'

class formPost(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'