function toggleVisibility(id) {
    var element = document.getElementById(id);
    if (element.style.display === "none") {
        element.style.display = "block";
    } else {
        element.style.display = "none";
    }
}

document.addEventListener('DOMContentLoaded', function() {
    var calendarEl = document.getElementById('calendar');

    var calendar = new FullCalendar.Calendar(calendarEl, {
        initialView: 'dayGridMonth',
        events: [
            { title: 'Cálculo II', start: '2024-10-25T08:00:00', end: '2024-10-25T10:00:00' },
            { title: 'Física I', start: '2024-10-26T10:00:00', end: '2024-10-26T12:00:00' },
            { title: 'Programación II', start: '2024-10-27T13:00:00', end: '2024-10-27T15:00:00' }
        ]
    });

    calendar.render();
});

function sendMessage() {
    var chatBox = document.getElementById('chat-box');
    var message = document.getElementById('chat-message').value;

    if (message.trim() !== '') {
        var newMessage = document.createElement('p');
        newMessage.textContent = message;
        chatBox.appendChild(newMessage);

        document.getElementById('chat-message').value = ''; // Limpiar el campo de texto
        chatBox.scrollTop = chatBox.scrollHeight; // Desplazar hacia abajo automáticamente
    }
}

function validateForm() {
    var name = document.getElementById('name').value;
    var email = document.getElementById('email').value;
    var password = document.getElementById('password').value;

    if (name === '' || email === '' || password === '') {
        alert('Por favor, completa todos los campos.');
        return false;
    }

    if (password.length < 6) {
        alert('La contraseña debe tener al menos 6 caracteres.');
        return false;
    }

    alert('Registro exitoso');
    return true;
}