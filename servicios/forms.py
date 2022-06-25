from dataclasses import fields
from django import forms
from .models import Servicio

class formServ(forms.ModelForm):
    class Meta:
        model = Servicio
        fields = '__all__'
