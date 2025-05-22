//    // Validación con Regex
//     const form = document.getElementById("form-login");
//     const message = document.getElementById("message");

//     form.addEventListener("submit", function (e) {
//     e.preventDefault();

//     const usuario = document.getElementById("usuario").value.trim();
//     const clave = document.getElementById("clave").value.trim();

//     // Regex para validar exactamente "Lyda" y "lyda123"
//     const usuarioValido = /^Wissen$/ || /^wissen$/;
//     const claveValida = /^1234wissen$/;

//     if (usuarioValido.test(usuario) && claveValida.test(clave)) {
//         message.style.color = "limegreen";
//         message.textContent = "Usuario o contraseña correctos";
//     } else {
//         message.style.color = "crimson";
//         message.textContent = "Usuario o contraseña incorrectos";
//     }
//     });
        // alert("Usuario y contraseña correctos. Bienvenid@ " + usuario + "!");

    // Mostrar/ocultar contraseña
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
    
    document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('form-login');
    const usuarioInput = document.getElementById('usuario');
    const claveInput = document.getElementById('clave');
    const messageDiv = document.getElementById('message');

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
        const value = e.target.value;
        const caracteresInvalidos = /[^a-zA-Z0-9]/g;

        if (caracteresInvalidos.test(value)) {
            e.target.value = value.replace(caracteresInvalidos, '');
            showMessage('Solo se permiten letras y números en la contraseña', 'error');
        }
    });

    

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