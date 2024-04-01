"""
    URL configuration for MyBand project.
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('bandhome.urls')),
    path('bandhome/', include('bandhome.urls')),
    path('bandblog/', include('bandblog.urls')),
    path('bandtour/', include('bandtour.urls')),
]
