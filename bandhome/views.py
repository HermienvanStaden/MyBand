from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.shortcuts import render, redirect
from django.views import generic
from .forms import SignUpForm

# Create your views here.
def index(request):
    """ A function that receives a user request and renders
        the "bandhome/authentication/index.html" view.

        :return: View rendering
        :rtype: html view
    """
    return render(request, "bandhome/authentication/index.html")

# Request information from new user
def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('bandhome:welcome_user')
    else:
        form = SignUpForm()
    return render(request, 'bandhome/authentication/signup.html', {'form': form})

# Request login information from user
def user_login(request):
    print(request.user.username)
    return render(request, 'bandhome/authentication/login.html')

# Make sure that information given in login form is correct, else request re-login
def authenticate_user(request):
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    email = request.POST['email']
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(
        first_name=first_name, last_name=last_name, email=email, 
        username=username, password=password
        )
    if user is None:
        return HttpResponseRedirect(
            reverse('bandhome:login')
        )
    else:
        login(request, user)
        return HttpResponseRedirect(
            reverse('bandhome:welcome_user')
        )
    
# Display user's details once they have logged in
def welcome_user(request):
    print(request.user.username)
    return render(request, 'bandhome/band/welcome.html', {
        "first_name": request.user.first_name,
        "last_name": request.user.last_name,
        "email": request.user.email,
        "username": request.user.username,
        "password": request.user.password,
    })

# Display home page
def show_home(request):
    return render(request, "bandhome/band/home.html")

# Display about page
def show_about(request):
    return render(request, "bandhome/band/about.html")
