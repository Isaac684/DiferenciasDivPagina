from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.

# ejemplo de prueba
# def hello(request):
#     return HttpResponse("<h1>Hello, world!</h1>")

def homepage(request):
    return render(request, 'homepageapp.html')

def login(request):
    return render(request, 'loginapp.html')

def signup(request):
    return render(request, 'signupapp.html')

def recover(request):
    return render(request, 'recoverpassword.html')