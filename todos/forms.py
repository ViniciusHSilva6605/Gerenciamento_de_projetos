from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User  # Importe o modelo User do Django




class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password')

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')
