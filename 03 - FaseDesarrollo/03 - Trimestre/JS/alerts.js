function cerrarsesion() {
    Swal.fire({
        title: '¿Estás seguro de cerrar sesión?',
        text: "Se perderán los cambios realizados si cierras sesión sin guardar.",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Sí, salir.'
      }).then((result) => {
        if (result.isConfirmed) {
            window.location="login.html";
        }
    })
}

$('#cerrar').click(function (event)
{
    Swal.fire({
        title: '¿Estás seguro de cerrar sesión?',
        text: "Se perderán los cambios realizados si cierras sesión sin guardar.",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Sí, salir.'
      }).then((result) => {
        if (result.isConfirmed) {
            window.location="login.html";
        }
    })
});
