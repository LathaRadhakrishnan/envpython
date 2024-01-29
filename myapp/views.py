from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.conf import settings

def my_view(request):
    name = settings.NAME
    return HttpResponse(f"Secret Key: {name}")