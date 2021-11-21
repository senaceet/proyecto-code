function cerrarsesion() {
    Swal.fire({
        title: '¿Estás seguro de cerrar sesión?',
        text: "Si cierras sesión sin guardar, se perderán los cambios realizados.",
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
        title: '¿Estás seguro de querer cerrar sesión?',
        text: "Si cierras sesión sin guardar, se perderán los cambios realizados.",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Sí, salir.'
      }).then((result) => {
        if (result.isConfirmed) {
            window.location="{% url 'login' %}"; /* Enviar al login.html con Django */
        }
    })
});
