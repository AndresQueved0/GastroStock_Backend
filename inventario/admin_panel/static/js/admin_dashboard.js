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

            // Ocultar todo el contenido
            document.querySelectorAll('.container-fluid section').forEach(section => {
                section.style.display = 'none';
            });

            // Mostrar el contenido seleccionado
            const contentId = link.getAttribute('data-content');
            document.getElementById(contentId).style.display = 'block';
        });
    });

    // Ocultar todo el contenido al cargar la página
    document.querySelectorAll('.container-fluid section').forEach(section => {
        section.style.display = 'none';
    });

    // Mostrar por defecto el contenido de "inventario"
    document.getElementById('inventario').style.display = 'block';
});

document.addEventListener('DOMContentLoaded', function() {
    const deleteButtons = document.querySelectorAll('.delete-product');
    const deleteModal = new bootstrap.Modal(document.getElementById('deleteConfirmModal'));
    let productIdToDelete = null;

    deleteButtons.forEach(button => {
        button.addEventListener('click', function(event) {
            event.preventDefault();
            productIdToDelete = this.getAttribute('data-id');
            deleteModal.show();
        });
    });

    document.getElementById('confirmDelete').addEventListener('click', function() {
        if (productIdToDelete) {
            deleteProduct(productIdToDelete);
        }
    });

    function deleteProduct(productId) {
        fetch(`/admin-panel/borrar-producto/${productId}/`, {
            method: 'POST',
            headers: {
                'X-CSRFToken': getCookie('csrftoken'),
                'Content-Type': 'application/json'
            },
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                const row = document.querySelector(`tr[data-product-id="${productId}"]`);
                if (row) {
                    row.remove();
                }
                deleteModal.hide();
            } else {
                console.error('Error al eliminar el producto:', data.error);
            }
        })
        .catch(error => {
            console.error('Error al procesar la solicitud:', error);
        });
    }

    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
});