# hello_world_app/urls.py
from django.urls import path
from .views import my_view

urlpatterns = [
    path('', my_view, name='myapp'),
]