from django.shortcuts import render, redirect
from .models import usuarios
from django.contrib import messages
import re

# Create your views here.
def homepage(request):
    return render(request, 'homepageapp.html')

def login(request):
    return render(request, 'loginapp.html')

def signup(request):
    return render(request, 'signupapp.html')

def recover(request):
    return render(request, 'recoverpassword.html')

def registerUser(request):
    if request.method == 'POST':
        fullName = request.POST.get('fullName')
        user = request.POST.get('user')
        email = request.POST.get('email')
        password = request.POST.get('password')

        fullName_error = None
        user_error = None
        email_error = None
        password_error = None
        is_valid = True

        userRegister = usuarios.objects.filter(usuario=user).exists()
        emailRegister = usuarios.objects.filter(correo=email).exists()
        passwordRegister = usuarios.objects.filter(contraseña=password).exists()

        # Validación del campo "fullName"
        if not re.match(r'^[A-Za-z\s]+$', fullName):
            fullName_error = "Solo se permiten letras y espacios en blanco."
            is_valid = False
        else:
            fullName_error = ""

        # Validación del campo "User"
        if not re.match(r'^[a-z0-9]+$', user):
            user_error = "Solo se permiten letras minúsculas y números."
            is_valid = False
        elif userRegister:
            user_error = "El usuario ya está registrado."
            is_valid = False
        else:
            user_error = ""

        # Validación del campo "Email"
        if not re.match(r'^[\w-]+(\.[\w-]+)*@([\w-]+\.)+[a-zA-Z]{2,7}$', email):
            email_error = "Dirección de correo electrónico no válida."
            is_valid = False
        elif emailRegister:
            email_error = "El correo ya está registrado."
            is_valid = False
        else:
            email_error = ""

        # Validación del campo "Password"
        if len(password) < 8 or not re.match(r'^(?=.*[a-zA-Z0-9])(?=.*[!@#$%^&*()])[a-zA-Z0-9!@#$%^&*()]{8,}$', password):
            password_error = "La contraseña debe tener al menos 8 caracteres y contener al menos un símbolo."
            is_valid = False
        elif passwordRegister:
            password_error = "La contraseña ya está registrada."
            is_valid = False
        else:
            password_error = ""

        if is_valid:
            # Realizar las operaciones necesarias para guardar el usuario en la base de datos
            userInsert = usuarios()
            userInsert.nombreCompleto = fullName
            userInsert.usuario = user
            userInsert.correo = email
            userInsert.contraseña = password
            userInsert.save()

            return redirect('/loginapp')
        else:
            return render(request, "signupapp.html", {
                'fullNameError': fullName_error,
                'userError': user_error,
                'emailError': email_error,
                'passwordError': password_error
            })
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
                if len(password) >= 8 and re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
                    # Actualizar la contraseña del usuario
                    usuario = usuarios_list.first()
                    usuario.contraseña = password
                    usuario.save()
                    messages.success(request, 'Contraseña actualizada correctamente.')
                else:
                    messages.error(request, 'La contraseña debe tener al menos 8 caracteres y al menos un símbolo.')
            else:
                messages.error(request, 'Las contraseñas no coinciden.')
        else:
            messages.error(request, 'Usuario incorrecto!!!')

    return render(request, 'recoverpassword.html')