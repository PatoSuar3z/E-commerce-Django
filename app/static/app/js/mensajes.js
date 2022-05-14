function confirmDelete(){
    Swal.fire({
        title: 'Estás seguro?',
        text: "No podras deshacer la acción!",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Si , Eliminar!'
      }).then((result) => {
        if (result.isConfirmed) {
          Swal.fire(
            'Eliminado!',
            'Producto Eliminado.',
            'success'
          ).then(function(){
              window.location.href=""
          })
        }
      })
}