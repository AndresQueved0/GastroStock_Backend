document.addEventListener('DOMContentLoaded', function() {
    const sidebarLinks = document.querySelectorAll('.sidebar a');

    sidebarLinks.forEach(function(link) {
        link.addEventListener('click', function(event) {
            event.preventDefault(); // Evita el comportamiento predeterminado del enlace

            // Remover la clase 'hover' de todos los enlaces
            sidebarLinks.forEach(function(l) {
                l.classList.remove('hover');
            });

            // Agregar la clase 'hover' solo al enlace clicado
            link.classList.add('hover');
        });
    });

 // Ocultar todo el contenido al cargar la página
    document.querySelectorAll('.container-fluid section').forEach(section => {
    section.style.display = 'none';
});

// Mostrar por defecto el contenido de "mesas"
document.getElementById('inventario').style.display = 'block';
    });

document.querySelectorAll('.d-flex .sidebar a').forEach(menuItem => {
menuItem.addEventListener('click', () => {
    // Ocultar todo el contenido
    document.querySelectorAll('.container-fluid section').forEach(section => {
        section.style.display = 'none';
    });

    // Mostrar el contenido seleccionado
    const contentId = menuItem.getAttribute('data-content');
    document.getElementById(contentId).style.display = 'block';
});
});