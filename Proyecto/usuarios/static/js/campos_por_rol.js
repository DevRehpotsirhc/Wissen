document.addEventListener('DOMContentLoaded', function () {
  const rolSelect = document.querySelector('select[name="rol"]');

  const cargoGroup = document.getElementById('grupo-cargo');
  const materiasGroup = document.getElementById('grupo-materias');
  const cursosGroup = document.getElementById('grupo-cursos');
  const cursoEstudianteGroup = document.getElementById('grupo-id_curso');

  const cargoInput = cargoGroup.querySelector('select');
  const materiasInput = materiasGroup.querySelector('select');
  const cursosInput = cursosGroup.querySelector('select');
  const cursoEstudianteInput = cursoEstudianteGroup.querySelector('select');

  function toggleFields() {
    const rol = rolSelect.value;

    // Ocultar todo primero
    cargoGroup.style.display = 'none';
    materiasGroup.style.display = 'none';
    cursosGroup.style.display = 'none';
    cursoEstudianteGroup.style.display = 'none';

    // Quitar required de todos
    cargoInput.required = false;
    materiasInput.required = false;
    cursosInput.required = false;
    cursoEstudianteInput.required = false;

    // Mostrar y aplicar required según el rol
    if (rol === 'admin') {
      cargoGroup.style.display = 'block';
      cargoInput.required = true;
    } else if (rol === 'docen') {
      materiasGroup.style.display = 'block';
      cursosGroup.style.display = 'block';
      materiasInput.required = true;
      cursosInput.required = true;
    } else if (rol === 'estud') {
      cursoEstudianteGroup.style.display = 'block';
      cursoEstudianteInput.required = true;
    }
  }

  if (rolSelect) {
    rolSelect.addEventListener('change', toggleFields);
    toggleFields(); // Ejecutar al cargar
  }
});