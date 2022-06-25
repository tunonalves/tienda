from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User  

class CustomUserChangeForm(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ('username','email', 'first_name', 'last_name',)