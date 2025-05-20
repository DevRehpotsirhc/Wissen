document.addEventListener("DOMContentLoaded", function () {
    const rolSelect = document.querySelector('select[name="rol"]');
    const cargoField = document.querySelector('select[name="cargo"]').parentElement;
    const materiasField = document.querySelector('select[name="materias"]').parentElement;
    const cursosField = document.querySelector('select[name="cursos"]').parentElement;
    const cursoField = document.querySelector('select[name="id_curso"]').parentElement;

    function actualizarVisibilidadCampos() {
        const rol = rolSelect.value;
        cargoField.style.display = rol === 'admin' ? 'block' : 'none';
        materiasField.style.display = rol === 'docen' ? 'block' : 'none';
        cursosField.style.display = rol === 'docen' ? 'block' : 'none';
        cursoField.style.display = rol === 'estud' ? 'block' : 'none';
    }

    rolSelect.addEventListener('change', actualizarVisibilidadCampos);
    actualizarVisibilidadCampos();
});