from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return HttpResponse('<h1>BLOG HOME</h1>')
def about(requuest):
    return HttpResponse('<h1>blog about</h1>')