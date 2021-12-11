(function(){

    const btneliminacion = document.querySelectorAll(".btneliminacion");

    btneliminacion.forEach(btn => {
        btn.addEventListener('click',(e) => {
            const confirmacion = confirm('¿Seguro que quieres eliminarlo?');
            if(!confirmacion){
                e.preventDefault();
            }
        });
    });

})();