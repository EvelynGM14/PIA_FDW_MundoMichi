
function enviarFormularioAdopcion() {

    const formulario = document.querySelector('.formulario');
    

    formulario.addEventListener('submit', function(event) {
        event.preventDefault(); 
        

        if (validarFormulario()) {
            alert('Gracias por tu interés en adoptar un gatito. ¡Te contactaremos pronto!');
        } else {
            alert('Por favor, completa todos los campos.');
        }
    });
}


function validarFormulario() {
    const nombre = document.getElementById('nombre').value;
    const telefono = document.getElementById('telefono').value;
    const email = document.getElementById('email').value;
    const direccion = document.getElementById('direccion').value;
    const tipoVivienda = document.getElementById('tipo_vivienda').value;
    const mascotasActuales = document.querySelector('input[name="mascotas_actuales"]:checked');
    const experiencia = document.getElementById('experiencia').value;
    const razonAdopcion = document.getElementById('razon_adopcion').value;


    return nombre !== '' && telefono !== '' && email !== '' && direccion !== '' && tipoVivienda !== '' && mascotasActuales && experiencia !== '' && razonAdopcion !== '';
}


window.onload = function() {
    enviarFormularioAdopcion();
};