"""
    URL configuration for MyBand project.
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('MyBand.bandhome.urls')),
    path('bandhome/', include('MyBand.bandhome.urls')),
    path('bandblog/', include('MyBand.bandblog.urls')),
    path('bandtour/', include('MyBand.bandtour.urls')),
]
