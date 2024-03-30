from django.views.generic import ListView, DetailView
from django.urls import path, include
from .models import Post
from . import views

app_name = 'bandtour'
urlpatterns = [
    path('', ListView.as_view(
            queryset=
            Post.objects.all().order_by("date")[:25],
            template_name="bandtour/tour.html"
            )
        ),
    path('', ListView.as_view, name='tour'),
    path('<int:pk>/',
         DetailView.as_view(
             model = Post,
             template_name="bandtour/tour_item.html"
            )
        ),
]