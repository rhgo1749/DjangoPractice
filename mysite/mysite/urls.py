"""mysite URL Configuration
It is just practicing project
"""
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
]
