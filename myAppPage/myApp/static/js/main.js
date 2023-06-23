const buttonAceptar = document.querySelector('#button-aceptar')
const inputPuntos = document.querySelector('#cantidad-puntos')
const ingresarXY = document.querySelector('.puntosXY')
let puntoIngresado = false;


inputPuntos.addEventListener('keypress', function (e) {
    var key = e.which || e.keyCode; // Obtener el código de tecla presionada
    //Verificar si el código de tecla no corresponde a un número
    if (key < 48 || key > 57) {
        e.preventDefault(); // Evitar la acción predeterminada (no ingresar el carácter)
    }

    //este codigo sera para cuando se ingresen los valores de X y Y
    // if ((key < 48 || key > 57) && key !== 46 || (key === 46 && puntoIngresado)) {
    //     e.preventDefault(); // Evitar la acción predeterminada (no ingresar el carácter)
    // }
    // // Si se presionó el punto y no se ha ingresado previamente, marcar como ingresado
    // if (key === 46 && !puntoIngresado) {
    //     puntoIngresado = true;
    // }
})

buttonAceptar.addEventListener('click',function () {
    cantPuntos = inputPuntos.value
    if (cantPuntos != '') {
        ingresarXY.innerHTML= ''
        for (let i = 0; i < cantPuntos; i++) {
            ingresarXY.innerHTML += `
            <label class="form-label">Ingrese el valor para el punto ${i+1}:</label>
            <div class="input-group mb-3" id="grupoPuntos${i+1}">
                <input type="text" class="form-control" placeholder="Valor de x${i+1}">
                <input type="text" class="form-control" placeholder="Valor de y${i+1}">
            </div>`
        }
    }
})