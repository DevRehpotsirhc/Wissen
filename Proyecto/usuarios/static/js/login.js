//     const form = document.getElementById("form-login");
//     const message = document.getElementById("message");

//     form.addEventListener("submit", function (e) {
//     e.preventDefault();

//     const usuario = document.getElementById("usuario").value.trim();
//     const clave = document.getElementById("clave").value.trim();

//     const usuarioValido = /^Wissen$/ || /^wissen$/;
//     const claveValida = /^1234wissen$/;

//     if (usuarioValido.test(usuario) && claveValida.test(clave)) {
//         message.style.color = "limegreen";
//         message.textContent = "Usuario o contraseña correctos";
//         alert("¡ Bienvenido(a) al Observador Digital!");
//     } else {
//         message.style.color = "crimson";
//         message.textContent = "Usuario o contraseña incorrectos";
//     }
//     });

    // Mostrar/ocultar contraseña Ojo
    const iconOjo = document.getElementById("icon_ojo");
    const inputPass = document.getElementById("clave");

    iconOjo.addEventListener("click", () => {
    if (inputPass.type === "password") {
        inputPass.type = "text";
        iconOjo.classList.remove("fa-eye");
        iconOjo.classList.add("fa-eye-slash");
    } else {
        inputPass.type = "password";
        iconOjo.classList.remove("fa-eye-slash");
        iconOjo.classList.add("fa-eye");
    }
    });
    
    // Validaciones usuario y contraseña
    document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('form-login');
    const usuarioInput = document.getElementById('usuario');
    const claveInput = document.getElementById('clave');
    const messageDiv = document.getElementById('message');

    // Validación para usuario
    usuarioInput.addEventListener('input', function(e) {
    const value = e.target.value.trim();
    const maxCaracteres = 50;
    const caracteresInvalidos = /[^a-zA-Z0-9]/g;

    // Limpiar caracteres inválidos
    if (caracteresInvalidos.test(value)) {
        e.target.value = value.replace(caracteresInvalidos, '');
        showMessage('Solo se permiten letras y números en el usuario', 'error');
    }

    // Validar longitud máxima
    if (e.target.value.length > maxCaracteres) {
        e.target.value = e.target.value.slice(0, maxCaracteres);
        showMessage(`Máximo ${maxCaracteres} caracteres permitidos`, 'error');
    }
});

// Validación para contraseña
    claveInput.addEventListener('input', function(e) {
        const value = e.target.value.trim();
        const maxCaracteres = 50;
        const caracteresValidos = /[^a-zA-Z0-9ñÑ]/g;

        // Limpiar caracteres inválidos
        if (caracteresInvalidos.test(value)) {
            e.target.value = value.replace(caracteresValidos, '');
            showMessage('Solo se permiten letras y números en la contraseña', 'error');
        }

        // Validar longitud máxima 50 caracteres
        if (e.target.value.length > maxCaracteres) {
            e.target.value = e.target.value.slice(0, maxCaracteres);
            showMessage(`Máximo ${maxCaracteres} caracteres permitidos`, 'error');
        }
    });

    // muestra el mensaje de error 
    function showMessage(msg, type) {
        messageDiv.innerHTML = `
            <div class="alert ${type}">
                ${msg}
            </div>
        `;
        
    // Limpiar mensaje después de 5 segundos
    setTimeout(() => {
        messageDiv.innerHTML = '';
    }, 5000);
    }
});