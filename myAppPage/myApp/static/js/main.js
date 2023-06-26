const buttonAceptar = document.querySelector('#button-aceptar')
const inputPuntos = document.querySelector('#cantidad-puntos')
const ingresarXY = document.querySelector('.puntosXY')
const ButtonEnviar = document.querySelector('#Enviar')

// ButtonEnviar.addEventListener('submit',function (e) {
//     let  valoresX = document.querySelectorAll('#valorX');
//     let valoresY = document.querySelectorAll('#valorY');

//     for (let key in valoresX) {
//         if (key.value == '') {
//             e.preventDefault()
//         }
//     }
//     for (let key2 in valoresY) {
//         if (key2.value == '') {
//             e.preventDefault()
//         }
//     }
// })

inputPuntos.addEventListener('keypress', function (e) {
    let key = e.which || e.keyCode; // Obtener el código de tecla presionada
    if(!inputPuntos.value == ''){
        ingresarXY.innerHTML = `
        <label class="form-label">Ingrese el valor para el punto</label>
        <div class="input-group mb-3">
            <input type="text" class="form-control" disabled placeholder="Valor de x">
            <input type="text" class="form-control" disabled placeholder="Valor de y">
        </div>`
    }    
    //Verificar si el código de tecla no corresponde a un número
    if (key < 48 || key > 57) {
        ingresarXY.innerHTML = `
            <label class="form-label">Ingrese el valor para el punto</label>
            <div class="input-group mb-3">
                <input type="text" class="form-control" disabled placeholder="Valor de x">
                <input type="text" class="form-control" disabled placeholder="Valor de y">
            </div>`
        e.preventDefault(); // Evitar la acción predeterminada (no ingresar el carácter)
    }
})

inputPuntos.addEventListener('keyup', function (e) {
    let key = e.which || e.keyCode; // Obtener el código de tecla presionada
    if(!inputPuntos.value == ''){
        ingresarXY.innerHTML = `
        <label class="form-label">Ingrese el valor para el punto</label>
        <div class="input-group mb-3">
            <input type="text" class="form-control" disabled placeholder="Valor de x">
            <input type="text" class="form-control" disabled placeholder="Valor de y">
        </div>`
    }    
    //Verificar si el código de tecla no corresponde a un número
    if (key < 48 || key > 57) {
        ingresarXY.innerHTML = `
            <label class="form-label">Ingrese el valor para el punto</label>
            <div class="input-group mb-3">
                <input type="text" class="form-control" disabled placeholder="Valor de x">
                <input type="text" class="form-control" disabled placeholder="Valor de y">
            </div>`
        e.preventDefault(); // Evitar la acción predeterminada (no ingresar el carácter)
    }
})

buttonAceptar.addEventListener('click',function () {
    cantPuntos = inputPuntos.value
    if (cantPuntos != '') {
        if (cantPuntos<=100 && cantPuntos>2) {            
            ingresarXY.innerHTML= ''
            for (let i = 0; i < cantPuntos; i++) {
                ingresarXY.innerHTML += `
                <div class="col-md-5 col-lg-5 ">
                    <label class="form-label">Ingrese el valor para el punto ${i+1}:</label>
                    <div class="input-group mb-3">
                        <input type="text" class="form-control" name="valorX" id="valorX" placeholder="Valor X${i+1}">
                        <input type="text" class="form-control" name="valorY" id="valorY" placeholder="Valor Y${i+1}">
                    </div>
                </div>`
            }
        }
    }

    let  valoresX = document.querySelectorAll('#valorX');
    let valoresY = document.querySelectorAll('#valorY');
    eventoInputsXY(valoresX)
    eventoInputsXY(valoresY)
})

const eventoInputsXY = (valores) =>{
    for (var i = 0; i < valores.length; i++) {
        valores[i].addEventListener('keypress', function(e) {
            var key = e.which || e.keyCode; // Obtener el código de tecla presionada
            var inputValue = this.value // Obtener el valor actual del campo
    
            // Verificar si el código de tecla no corresponde a un número ni al punto
            if ((key < 48 || key > 57) && key !== 46) {
            e.preventDefault() // Evitar la acción predeterminada (no ingresar el carácter)
            }
    
            // Verificar si ya hay un punto en el valor del campo
            if (inputValue.indexOf('.') !== -1 && key === 46) {
            e.preventDefault() // Evitar la acción predeterminada (no ingresar el segundo punto)
            }
        })
    }
}

