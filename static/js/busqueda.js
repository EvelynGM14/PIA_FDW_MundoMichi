document.addEventListener('DOMContentLoaded', function() {
    const botonBuscar = document.getElementById('btnBuscar');
    const cajaBusqueda = document.getElementById('buscar');

    botonBuscar.addEventListener('click', function() {
        let query = cajaBusqueda.value.toLowerCase();  // Obtener el término de búsqueda
        if (!query) {
            alert("Por favor ingrese un término de búsqueda.");
            return;
        }

        // Obtener todos los elementos de texto en la página
        const elementosTexto = document.body.querySelectorAll('*');

        let resultadosEncontrados = false;

        // Recorremos todos los elementos y buscamos coincidencias
        elementosTexto.forEach(function(elemento) {
            if (elemento.children.length === 0) {  // Solo considerar elementos sin hijos (texto visible)
                let contenido = elemento.textContent.toLowerCase();

                if (contenido.includes(query)) {
                    elemento.style.backgroundColor = '#FFC0CB';  // Resaltar el elemento encontrado
                    resultadosEncontrados = true;
                } else {
                    elemento.style.backgroundColor = '';  // Restaurar el color si no es coincidente
                }
            }
        });

        if (!resultadosEncontrados) {
            alert("No se encontraron resultados.");
        }
    });

    // Opcional: permitir búsqueda al presionar Enter
    cajaBusqueda.addEventListener('keydown', function(e) {
        if (e.key === 'Enter') {
            botonBuscar.click();
        }
    });
});
