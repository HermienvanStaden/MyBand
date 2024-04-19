from django.views.generic import ListView, DetailView
from django.urls import path, include
from MyBand.bandblog.models import Post
from . import views

app_name = 'bandblog'
urlpatterns = [
    path('', ListView.as_view(
            queryset=
            Post.objects.all().order_by("-date")[:25],
            template_name="bandblog/blog.html"
            )
        ),
    path('', ListView.as_view, name='blog'),
    path('<int:pk>/',
         DetailView.as_view(
             model = Post,
             template_name="bandblog/post.html"
            )
        ),
]