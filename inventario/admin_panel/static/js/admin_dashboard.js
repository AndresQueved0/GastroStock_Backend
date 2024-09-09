document.addEventListener('DOMContentLoaded', function() {
    const links = document.querySelectorAll('#myLink');
    const sections = document.querySelectorAll('section');

    // Función para mostrar una sección y ocultar las demás
    function showSection(sectionId) {
        sections.forEach(section => {
            if (section.id === sectionId) {
                section.style.display = 'block';
            } else {
                section.style.display = 'none';
            }
        });
    }

    // Añadir evento click a cada enlace
    links.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            const sectionToShow = this.getAttribute('data-content');
            showSection(sectionToShow);
        });
    });

    // Mostrar la sección de inventario por defecto
    showSection('inventario');
    })

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

document.addEventListener('DOMContentLoaded', function() {
    const deleteButtons = document.querySelectorAll('.delete-empleado');
    const deleteModal = new bootstrap.Modal(document.getElementById('deleteEmpleadoConfirmModal'));
    let empleadoIdToDelete = null;

    deleteButtons.forEach(button => {
        button.addEventListener('click', function(event) {
            event.preventDefault();
            empleadoIdToDelete = this.getAttribute('data-id');
            deleteModal.show();
        });
    });
}),

    document.getElementById('confirmDeleteEmpleado').addEventListener('click', function() {
        if (empleadoIdToDelete) {
            deleteEmpleado(empleadoIdToDelete);
        }
    });

    function deleteEmpleado(empleadoId) {
        fetch(`/admin-panel/borrar-empleado/${empleadoId}/`, {
            method: 'POST',
            headers: {
                'X-CSRFToken': getCookie('csrftoken'),
                'Content-Type': 'application/json'
            },
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                const card = document.querySelector(`.card[data-empleado-id="${empleadoId}"]`);
                if (card) {
                    // Animación de desvanecimiento
                    card.style.opacity = '0';
                    card.style.transform = 'scale(0.8)';
                    setTimeout(() => {
                        card.closest('.col').remove(); // Elimina toda la columna
                        reorganizarTarjetas();
                    }, 300); // 300ms para la animación
                }
                deleteModal.hide();
                showAlert('success', 'Empleado eliminado con éxito.');
            } else {
                console.error('Error al eliminar el empleado:', data.error);
                showAlert('danger', `Error al eliminar el empleado: ${data.error}`);
            }
        })
        .catch(error => {
            console.error('Error al procesar la solicitud:', error);
            showAlert('danger', 'Error al procesar la solicitud de eliminación.');
        });
    }


    function showAlert(type, message) {
        const alertPlaceholderEmpleado = document.getElementById('alertPlaceholderEmpleado');
        const wrapper = document.createElement('div');
        wrapper.innerHTML = [
            `<div class="alert alert-${type} alert-dismissible" role="alert">`,
            `   <div>${message}</div>`,
            '   <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>',
            '</div>'
        ].join('');
        alertPlaceholderEmpleado.append(wrapper);

        setTimeout(() => {
            const alert = bootstrap.Alert.getOrCreateInstance(wrapper.firstChild);
            alert.close();
        }, 5000);
    }

