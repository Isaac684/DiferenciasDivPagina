const validateRegister = document.getElementById('registerButton');

validateRegister.addEventListener('click', (e) => {
    e.preventDefault();

    var user = document.getElementById("user").value;
    var email = document.getElementById("email").value;
    var password = document.getElementById("password").value;

    var userError = document.getElementById("userError");
    var emailError = document.getElementById("emailError");
    var passwordError = document.getElementById("passwordError");

    // Validación del campo "User"
    if (!user.match(/^[a-z0-9]+$/)) {
        userError.innerText = "Solo se permiten letras minúsculas y números.";
    } else {
        userError.innerText = "";
    }

    // Validación del campo "Email"
    if (!email.match(/^[\w-]+(\.[\w-]+)*@([\w-]+\.)+[a-zA-Z]{2,7}$/)) {
        emailError.innerText = "Dirección de correo electrónico no válida.";
      } else {
        emailError.innerText = "";
    }

    // Validación del campo "Password"
    if (password.length < 8 || !password.match(/^(?=.*[a-zA-Z0-9])(?=.*[!@#$%^&*()])[a-zA-Z0-9!@#$%^&*()]{8,}$/)) {
        passwordError.innerText = "La contraseña debe tener al menos 8 caracteres y contener al menos un símbolo.";
    } else {
        passwordError.innerText = "";
    }
});
