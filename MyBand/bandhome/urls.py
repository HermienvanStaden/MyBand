from django.urls import path, include
from . import views
from django.conf.urls.static import static

app_name = 'bandhome'
urlpatterns = [
    path('', views.index, name="index"),
    path('authenticate_user/', views.authenticate_user,
         name='authenticate_user'),
    path('welcome_user/', views.welcome_user, name='welcome_user'),
    path('sign_up/', views.sign_up, name='signup'),
    path('show_home/', views.show_home, name='home-home'),
    path('show_about/', views.show_about, name='about'),
    path('log_in/', views.user_login, name='login'),
]