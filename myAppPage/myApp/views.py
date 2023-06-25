from django.shortcuts import render, redirect
from .models import usuarios
from django.contrib import messages
import re
import io

import base64
import numpy as np
from .diferenciasDivididas import diferencias_divididas
# Create your views here.
def homepage(request):
    return render(request, 'homepageapp.html')

def login(request):
    #del request.session['usuario']
    return render(request, 'loginapp.html')

def logout(request):
    # Eliminar los datos de la sesión
    del request.session['usuario']

    # Redirigir a la página principal
    return redirect('/loginapp')

def guest_page(request):
    is_guest = True
    return render(request, 'homepageapp.html', {'is_guest': is_guest})

def signup(request):
    return render(request, 'signupapp.html')

def recover(request):
    return render(request, 'recoverpassword.html')

def userProfile(request):
    return render(request, 'userProfile.html')

def editProfile(request):
    return render(request,'editprofile.html')

def registerUser(request):
    if request.method == 'POST':
        fullName = request.POST.get('fullName')
        user = request.POST.get('userr')
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
                'fullName': fullName,
                'userr': user,
                'email': email,
                'password': password,
                'fullNameError': fullName_error,
                'userError': user_error,
                'emailError': email_error,
                'passwordError': password_error
            })
    # else:
    #     return render(request, "signupapp.html")

def loginUser(request):
    if request.method == 'POST':
        username = request.POST.get('userLogin')
        password = request.POST.get('userPassword')

        usuarios_list = usuarios.objects.filter(usuario=username, contraseña=password)

        if usuarios_list.exists():
            usuario = usuarios_list[0]
            request.session['usuario'] = {
                'nombreCompleto': usuario.nombreCompleto,
                'usuario': usuario.usuario,
                'correo': usuario.correo,
                'contraseña': usuario.contraseña
            }
            # request.session['usuario'] = usuarios_list[0].usuario
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

def saveEditedProfile(request):
    if request.method == 'POST':
        fullNameEdit = request.POST.get('fullNameEdit')
        emailEdit = request.POST.get('emailEdit')
        userEdit = request.POST.get('userEdit')
        passwordEdit = request.POST.get('passwordEdit')

        fullNameErrorEdit = None
        userErrorEdit = None
        emailErrorEdit = None
        passwordErrorEdit = None
        is_validEdit = True

        userRegister = usuarios.objects.filter(usuario=userEdit).exists()
        emailRegister = usuarios.objects.filter(correo=emailEdit).exists()
        passwordRegister = usuarios.objects.filter(contraseña=passwordEdit).exists()

        # Validación del campo "fullNameEdit"
        if not re.match(r'^[A-Za-z\s]+$', fullNameEdit):
            fullNameErrorEdit = "Solo se permiten letras y espacios en blanco."
            is_validEdit = False
        else:
            fullNameErrorEdit = ""

        # Validación del campo "userEdit"
        if not re.match(r'^[a-z0-9]+$', userEdit):
            userErrorEdit = "Solo se permiten letras minúsculas y números."
            is_validEdit = False
        elif userRegister:
            userErrorEdit = "El usuario ya está registrado."
            is_validEdit = False
        else:
            userErrorEdit = ""

        # Validación del campo "emailEdit"
        if not re.match(r'^[\w-]+(\.[\w-]+)*@([\w-]+\.)+[a-zA-Z]{2,7}$', emailEdit):
            emailErrorEdit = "Dirección de correo electrónico no válida."
            is_validEdit = False
        elif emailRegister:
            emailErrorEdit = "El correo ya está registrado."
            is_validEdit = False
        else:
            emailErrorEdit = ""

        # Validación del campo "passwordEdit"
        if len(passwordEdit) < 8 or not re.match(r'^(?=.*[a-zA-Z0-9])(?=.*[!@#$%^&*()])[a-zA-Z0-9!@#$%^&*()]{8,}$', passwordEdit):
            passwordErrorEdit = "La contraseña debe tener al menos 8 caracteres y contener al menos un símbolo."
            is_validEdit = False
        elif passwordRegister:
            passwordErrorEdit = "La contraseña ya está registrada."
            is_validEdit = False
        else:
            passwordErrorEdit = ""

        if is_validEdit:
            try:
                usuarioActual = request.session.get('usuario')
                usuarioEditado = usuarios.objects.get(usuario=usuarioActual['usuario'])

                usuarioEditado.nombreCompleto = fullNameEdit
                usuarioEditado.usuario = userEdit
                usuarioEditado.correo = emailEdit
                usuarioEditado.contraseña = passwordEdit
                usuarioEditado.save()

                # Actualizar el campo de usuario en la sesión
                usuarioActual['nombreCompleto'] = fullNameEdit
                usuarioActual['usuario'] = userEdit
                usuarioActual['correo'] = emailEdit
                usuarioActual['contraseña'] = passwordEdit
                request.session['usuario'] = usuarioActual

                return redirect('/userProfile')
            except:
                # Manejar el caso en que el usuario no existe en la base de datos
                pass
        else:
            return render(request, 'editProfile.html', {
                'fullNameEdit': fullNameEdit,
                'emailEdit': emailEdit,
                'userEdit': userEdit,
                'passwordEdit': passwordEdit,
                'fullNameErrorEdit': fullNameErrorEdit,
                'userErrorEdit': userErrorEdit,
                'emailErrorEdit': emailErrorEdit,
                'passwordErrorEdit': passwordErrorEdit,
            })
    
def realizarEjercicio(request):
    if request.method == 'POST':
        image64 = None
        #verificarRespuesta = request.POST.get('verificarRespuesta')
        #pasoApaso = request.POST.get('pasoApaso')
        valoresX = request.POST.getlist('valorX')
        valoresY = request.POST.getlist('valorY')
        enterosX = list(map(float, valoresX))
        enterosY = list(map(float, valoresY))
        print(enterosX)
        print(enterosY)
        mtdd = diferencias_divididas()
        mtdd.insercion_datos(enterosX,enterosY)

        # cambio
        mtdd.mostrar_resultados()

        arrayDatos = mtdd.mostrar_resultados()
        nombres_columnas = arrayDatos[0]
        tablaRedondeada = np.round(arrayDatos[1], decimals=4)
        
        plt = mtdd.mostrar_grafica()

        #Creamos el archivo
        buffer = io.BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        #codificamos la imagen
        image64 = base64.b64encode(buffer.getvalue()).decode()

        titulo_tabla, tabla, dDividida, polinomio, polisimple = mtdd.calcular_polinomio()
        
        return render(request, 'homepageapp.html', {
            'iamgenG':image64,
            'tabla': tablaRedondeada,
            'nombres_columnas': nombres_columnas,
            'dDividida': dDividida,
            'polinomio': polinomio,
            'polisimple': polisimple
        })