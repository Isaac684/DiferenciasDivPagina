from django.shortcuts import render, redirect
from .models import usuarios
from django.contrib import messages

# Create your views here.
def homepage(request):
    return render(request, 'homepageapp.html')

def login(request):
    #del request.session['usuario']
    return render(request, 'loginapp.html')

def signup(request):
    return render(request, 'signupapp.html')

def recover(request):
    return render(request, 'recoverpassword.html')

def registerUser(request):
    if request.method == 'POST':
        userInsert = usuarios()
        userInsert.nombreCompleto = request.POST['fullName']
        userInsert.usuario = request.POST['user']
        userInsert.correo = request.POST['email']
        userInsert.contraseña = request.POST['password']
        userInsert.save()

        return redirect('/loginapp')
    else:
        return render(request, "signupapp.html")

def loginUser(request):
        
    if request.method == 'POST':
        username = request.POST.get('userLogin')
        password = request.POST.get('userPassword')

        usuarios_list = usuarios.objects.filter(usuario=username, contraseña=password)

        if usuarios_list.exists():
            request.session['usuario'] = usuarios_list[0].usuario
            return redirect('/homepage')
        else:
            messages.success(request, 'Usuario o contraseña incorrectos!!!')
            return render(request, 'loginapp.html')

def changePassword(request):
    if request.method == 'POST':
        username = request.POST.get('userRecover')
        password = request.POST.get('passwordRecover')
        confirm_password = request.POST.get('confirmPassword')

        usuarios_list = usuarios.objects.filter(usuario=username)

        if usuarios_list.exists():
            if password == confirm_password:
                # Actualizar la contraseña del usuario
                usuario = usuarios_list.first()
                usuario.contraseña = password
                usuario.save()
                messages.success(request, 'Contraseña actualizada correctamente.')
            else:
                messages.error(request, 'Las contraseñas no coinciden.')
        else:
            messages.error(request, 'Usuario incorrecto!!!')

    return render(request, 'recoverpassword.html')