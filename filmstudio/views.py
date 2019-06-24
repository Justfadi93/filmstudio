from django.http import HttpResponse
from django.shortcuts import render
from .models import Design

# Create your views here.

def home(response):

    designobj = Design.objects.all()

    return render(response, 'Front-Site/Home.html', {'obj': designobj})
