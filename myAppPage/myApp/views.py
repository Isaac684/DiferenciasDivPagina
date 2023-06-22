from django.shortcuts import render, redirect
from .models import usuarios
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

def registrar(request):
    if request.method == 'POST':
        userInsert = usuarios()
        userInsert.usuario = request.POST['user']
        userInsert.correo = request.POST['email']
        userInsert.contraseña = request.POST['password']
        userInsert.save()

        return redirect('/loginapp')
    else:
        return render(request, "signupapp.html")
    #     user = request.POST.get('user')
    #     email = request.POST.get('email')
    #     password = request.POST.get('password')

    #     # Crear una instancia del modelo usuarios
    #     new_user = usuarios(usuario=user, correo=email, contraseña=password)
    #     new_user.save()

    #     # Redirigir a una página de éxito o a donde desees
    #     return redirect('loginapp.html')

    # return render(request, 'signupapp.html')