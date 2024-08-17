from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def basic_view(request):
    return HttpResponse("Hello World!!! Welcome to Polling Application")



