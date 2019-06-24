from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("<h1>This is music app </h1>")


def view_music(request):

    name= "fahad"

    return render(request, 'practice-forms.html', {'name': name})


def add(request):

    number1 = int(request.POST['num1'])
    number2 = int(request.POST['num2'])
    result = number1+number2

    return render(request, 'results.html', {'result': result})


def delete(request):

    number1 = int(request.GET['num1'])
    number2 = int(request.GET['num2'])
    result = number1 - number2

    return render(request,'results.html', {'result': result})
