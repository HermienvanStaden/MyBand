from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

''' Define sign-up form that requests firstname, surname, email, username, 
    password and password confirmation'''
class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, help_text='Required')
    last_name = forms.CharField(max_length=40, help_text='Required')
    email = forms.EmailField()

    class Meta:
        model = User
        fields = (
            'first_name', 'last_name', 'email', 'username', 'password1', 
            'password2'
            )