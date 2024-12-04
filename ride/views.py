from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def auto(request):
    return HttpResponse('<h3> auto is very easy to travel in local city </h3>')
