// Script para mostrar un modal de confirmación antes de eliminar/rechazar
let accionAConfirmar = null;

function confirmarAccion(event, mensaje, accion) {
    event.preventDefault();
    const modal = document.getElementById('modalConfirmacion');
    document.getElementById('modalMensaje').innerText = mensaje;
    accionAConfirmar = accion;
    // Mostrar el modal
    var modalBootstrap = new bootstrap.Modal(modal);
    modalBootstrap.show();
}

// Al confirmar en el modal, ejecutar la acción guardada
window.addEventListener('DOMContentLoaded', function() {
    document.getElementById('btnConfirmarAccion').addEventListener('click', function() {
        if (typeof accionAConfirmar === 'function') {
            accionAConfirmar();
            accionAConfirmar = null;
        }
    });
    // Si el usuario cierra el modal o presiona cancelar, limpiar la acción pendiente
    document.getElementById('btnCancelarAccion').addEventListener('click', function() {
        accionAConfirmar = null;
        // Cerrar el modal correctamente
        var modal = bootstrap.Modal.getInstance(document.getElementById('modalConfirmacion'));
        if (modal) {
            modal.hide();
        }
        // Eliminar cualquier backdrop o blur residual
        document.body.classList.remove('modal-open');
        let backdrops = document.querySelectorAll('.modal-backdrop');
        backdrops.forEach(function(bd) { bd.remove(); });
    });
    document.getElementById('modalConfirmacion').addEventListener('hidden.bs.modal', function () {
        accionAConfirmar = null;
        // Eliminar cualquier backdrop o blur residual
        document.body.classList.remove('modal-open');
        let backdrops = document.querySelectorAll('.modal-backdrop');
        backdrops.forEach(function(bd) { bd.remove(); });
    });
});

// Botones de eliminar o rechazar
// Botones de eliminar o rechazar
window.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('.btnEliminacion').forEach(function(btn) {
        btn.addEventListener('click', function(e) {
            let mensaje = '¿Estás seguro que deseas realizar esta acción?';
            if (btn.classList.contains('btn-danger')) {
                mensaje = '¿Estás seguro que deseas ELIMINAR este PDF?';
            }
            if (btn.classList.contains('btn-decline')) {
                mensaje = '¿Estás seguro que deseas RECHAZAR este PDF?';
            }
            if (btn.classList.contains('btn-success')) {
                mensaje = '¿Estás seguro que deseas APROBAR este PDF?';
            }
            // Guardar la función original a ejecutar tras confirmar
            const pk = btn.getAttribute('data-pk') || btn.getAttribute('data-id') || btn.value;
            // Forzar backdrop estático y permitir cierre por backdrop y ESC
            const modal = document.getElementById('modalConfirmacion');
            if (modal) {
                modal.setAttribute('data-bs-backdrop', 'true');
                modal.setAttribute('data-bs-keyboard', 'true');
            }
            confirmarAccion(e, mensaje, function() {
                if (typeof window.redirectToUrl === 'function' && pk) {
                    window.redirectToUrl(pk);
                } else {
                    // Fallback por si se requiere otra acción
                    const url = btn.getAttribute('data-url');
                    if (url) {
                        window.location.href = url;
                    }
                }
            });
        });
    });
});
// Eliminar duplicidad de listeners
// (No agregar más listeners para .btnEliminacion)

