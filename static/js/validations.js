document.addEventListener('DOMContentLoaded', function() {
    var form = document.getElementById('id-terceros');
    var nombreInput = document.getElementById('id_name');
    var errorNombre = document.getElementById('errorNombre');

    form.addEventListener('submit', function(event) {
        if (nombreInput.value === '' || nombreInput.value.length < 3) {
            event.preventDefault(); // Evita que el formulario se envíe

            errorNombre.textContent = 'El nombre es obligatorio y debe tener al menos 3 caracteres';
            nombreInput.focus(); // Coloca el foco en el campo de nombre
        }
    });

    // Agregar evento para borrar el mensaje de error cuando se modifica el campo nombre
    nombreInput.addEventListener('input', function() {
        errorNombre.textContent = ''; // Borra el mensaje de error
    });
});
