from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class SignUpForm(UserCreationForm):
    """sign-up form that requests firstname, surname, email, username, 
        password and password confirmation.

        :param first_name: A new user's first name. This is a string 
            with maximum length of 30 characters, defaults to None
        :type first_name: str, required
        :param last_name: A new user's surname. This is a string 
            with maximum length of 40 characters, defaults to None
        :type last_name: str, required
        :param email: A new user's email address. This is a string 
            with no length restriction, defaults to None
        :type email: Emailfield, optional
    """
    first_name = forms.CharField(max_length=30, help_text='Required')
    last_name = forms.CharField(max_length=40, help_text='Required')
    email = forms.EmailField()

    class Meta:
        """ Metaclass for SignupForm """

        model = User
        fields = (
            'first_name', 'last_name', 'email', 'username', 'password1', 
            'password2'
            )