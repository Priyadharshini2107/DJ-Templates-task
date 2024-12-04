from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def veg(request):
    return HttpResponse('<h3> i like veg beriyani very much </h3>')

def nonveg(request):
    return render(request,'nonveg.html')
