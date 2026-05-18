// --- BASE DE DATOS LOCAL EN EL NAVEGADOR ---
if (!localStorage.getItem('users')) {
    const defaultUsers = [
        { name: 'Patricia', email: 'patricia@codingdojo.com', password: '123', role: 'Admin' },
        { name: 'Andrea', email: 'andrea@codingdojo.com', password: '123', role: 'Usuario' },
        { name: 'Katya', email: 'katya@codingdojo.com', password: '123', role: 'Usuario' }
    ];
    localStorage.setItem('users', JSON.stringify(defaultUsers));
}

if (!localStorage.getItem('messages')) {
    localStorage.setItem('messages', JSON.stringify([]));
}

// Selectores Comunes
const getUsers = () => JSON.stringify(localStorage.getItem('users'));
const getLoggedUser = () => JSON.parse(localStorage.getItem('loggedUser'));

// --- LOGICA DE AUTENTICACIÓN ---
if (document.getElementById('registerForm')) {
    document.getElementById('registerForm').addEventListener('submit', (e) => {
        e.preventDefault();
        const name = document.getElementById('regName').value;
        const email = document.getElementById('regEmail').value;
        const password = document.getElementById('regPassword').value;
        const confirm = document.getElementById('regConfirm').value;

        if (password !== confirm) return alert('Las contraseñas no coinciden');

        let users = JSON.parse(localStorage.getItem('users'));
        if (users.find(u => u.email === email)) return alert('El correo ya está registrado');

        // El primer usuario registrado podría ser Admin, los demás por defecto son Usuario
        const role = users.length === 0 ? 'Admin' : 'Usuario';
        users.push({ name, email, password, role });
        localStorage.setItem('users', JSON.stringify(users));

        alert('Registro exitoso. Ya puedes iniciar sesión.');
        document.getElementById('registerForm').reset();
    });
}

if (document.getElementById('loginForm')) {
    document.getElementById('loginForm').addEventListener('submit', (e) => {
        e.preventDefault();
        const email = document.getElementById('loginEmail').value;
        const password = document.getElementById('loginPassword').value;

        const users = JSON.parse(localStorage.getItem('users'));
        const user = users.find(u => u.email === email && u.password === password);

        if (!user) return alert('Credenciales incorrectas');

        localStorage.setItem('loggedUser', JSON.stringify(user));

        if (user.role === 'Admin') {
            window.location.href = 'templates/admin_usuario.html';
        } else {
            window.location.href = 'templates/enviar_mensaje.html';
        }
    });
}

function logout() {
    localStorage.removeItem('loggedUser');
    // Ajuste de ruta según dónde se encuentre el usuario
    window.location.href = window.location.pathname.includes('templates') ? '../index.html' : 'index.html';
}

// --- LOGICA DEL DASHBOARD DE ADMINISTRADOR ---
function renderAdminTable() {
    const users = JSON.parse(localStorage.getItem('users'));
    const tbody = document.getElementById('adminUserTable');
    tbody.innerHTML = '';

    users.forEach((user, index) => {
        tbody.innerHTML += `
            <tr>
                <td>${user.name}</td>
                <td>${user.email}</td>
                <td>${user.role}</td>
                <td class="actions-cell">
                    <button onclick="goToEdit('${user.email}')" style="background:#f1c40f; padding:5px 10px;">✏️</button>
                    <button onclick="deleteUser('${user.email}')" class="btn-danger" style="padding:5px 10px;">🗑️</button>
                    <button onclick="goToMessages('${user.email}')" style="background:#34495e; padding:5px 10px;">✉️</button>
                </td>
            </tr>
        `;
    });
}

// --- LOGICA DEL DASHBOARD DE USUARIO REGULAR ---
function renderUserTable() {
    const users = JSON.parse(localStorage.getItem('users'));
    const tbody = document.getElementById('userTable');
    tbody.innerHTML = '';

    users.forEach((user) => {
        tbody.innerHTML += `
            <tr>
                <td>${user.name}</td>
                <td>${user.email}</td>
                <td>${user.role}</td>
                <td>
                    <button onclick="goToMessages('${user.email}')" style="background:#34495e; padding:5px 10px;">✉️ Enviar Mensaje</button>
                </td>
            </tr>
        `;
    });
}

// --- CREAR Y EDITAR USUARIOS (ADMIN) ---
if (document.getElementById('createUserForm')) {
    document.getElementById('createUserForm').addEventListener('submit', (e) => {
        e.preventDefault();
        const name = document.getElementById('newName').value;
        const email = document.getElementById('newEmail').value;
        const password = document.getElementById('newPassword').value;
        const confirm = document.getElementById('newConfirm').value;
        const role = document.getElementById('newRole').value;

        if (password !== confirm) return alert('Contraseñas no coinciden');

        let users = JSON.parse(localStorage.getItem('users'));
        if (users.find(u => u.email === email)) return alert('Email ya ocupado');

        users.push({ name, email, password, role });
        localStorage.setItem('users', JSON.stringify(users));
        window.location.href = 'admin_usuario.html';
    });
}

function goToEdit(email) {
    localStorage.setItem('userToEdit', email);
    window.location.href = 'editar_usuario.html';
}

function loadEditUserData() {
    const emailToEdit = localStorage.getItem('userToEdit');
    const users = JSON.parse(localStorage.getItem('users'));
    const user = users.find(u => u.email === emailToEdit);

    if (user) {
        document.getElementById('editName').value = user.name;
        document.getElementById('editEmail').value = user.email;
        document.getElementById('editRole').value = user.role;
    }
}

if (document.getElementById('editUserForm')) {
    document.getElementById('editUserForm').addEventListener('submit', (e) => {
        e.preventDefault();
        const email = document.getElementById('editEmail').value;
        const name = document.getElementById('editName').value;
        const password = document.getElementById('editPassword').value;
        const role = document.getElementById('editRole').value;

        let users = JSON.parse(localStorage.getItem('users'));
        const userIndex = users.findIndex(u => u.email === email);

        if (userIndex !== -1) {
            users[userIndex].name = name;
            users[userIndex].role = role;
            if (password.trim() !== '') {
                users[userIndex].password = password;
            }
            localStorage.setItem('users', JSON.stringify(users));
            window.location.href = 'admin_usuario.html';
        }
    });
}

function deleteUser(email) {
    if (confirm('¿Seguro que deseas eliminar este usuario?')) {
        let users = JSON.parse(localStorage.getItem('users'));
        users = users.filter(u => u.email !== email);
        localStorage.setItem('users', JSON.stringify(users));
        renderAdminTable();
    }
}

// --- SISTEMA DE MENSAJES Y COMENTARIOS ---
function goToMessages(targetEmail) {
    localStorage.setItem('targetUserEmail', targetEmail);
    window.location.href = 'dashboard_mensaje.html';
}

function goBackDashboard() {
    const loggedUser = getLoggedUser();
    if (loggedUser.role === 'Admin') {
        window.location.href = 'admin_usuario.html';
    } else {
        window.location.href = 'enviar_mensaje.html';
    }
}

function renderMessagesWall() {
    const targetEmail = localStorage.getItem('targetUserEmail');
    const users = JSON.parse(localStorage.getItem('users'));
    const targetUser = users.find(u => u.email === targetEmail);
    
    document.getElementById('messageTargetTitle').innerText = `${targetUser.name} - Mensajes a ${targetUser.name}`;

    const messages = JSON.parse(localStorage.getItem('messages')) || [];
    const container = document.getElementById('messagesContainer');
    container.innerHTML = '';

    // Filtrar mensajes dirigidos a este usuario específico
    const filteredMessages = messages.filter(m => m.to === targetEmail);

    filteredMessages.forEach((msg) => {
        let commentsHtml = '';
        if (msg.comments) {
            msg.comments.forEach(c => {
                commentsHtml += `
                    <div class="comment-item">
                        <div class="meta-info">Comentario de ${c.fromName}, hace un momento</div>
                        <p>${c.text}</p>
                    </div>
                `;
            });
        }

        container.innerHTML += `
            <div class="message-item">
                <div class="meta-info">Mensaje de ${msg.fromName}, hace un momento</div>
                <p><strong>${msg.text}</strong></p>
                
                <div class="comments-section">
                    ${commentsHtml}
                </div>

                <div style="margin-top: 10px; display:flex; gap: 5px;">
                    <input type="text" id="commentInput-${msg.id}" placeholder="Escribe un comentario..." style="flex:1; padding:5px;">
                    <button onclick="postComment(${msg.id})" style="padding:5px 10px; font-size:12px;">Enviar</button>
                </div>
            </div>
        `;
    });
}

if (document.getElementById('postMessageForm')) {
    document.getElementById('postMessageForm').addEventListener('submit', (e) => {
        e.preventDefault();
        const text = document.getElementById('messageContent').value;
        const fromUser = getLoggedUser();
        const toEmail = localStorage.getItem('targetUserEmail');

        const messages = JSON.parse(localStorage.getItem('messages'));
        const newMsg = {
            id: Date.now(),
            to: toEmail,
            fromEmail: fromUser.email,
            fromName: fromUser.name,
            text: text,
            comments: []
        };

        messages.push(newMsg);
        localStorage.setItem('messages', JSON.stringify(messages));
        document.getElementById('postMessageForm').reset();
        renderMessagesWall();
    });
}

function postComment(messageId) {
    const inputElement = document.getElementById(`commentInput-${messageId}`);
    const text = inputElement.value;
    if (text.trim() === '') return;

    const fromUser = getLoggedUser();
    let messages = JSON.parse(localStorage.getItem('messages'));
    
    const msgIndex = messages.findIndex(m => m.id === messageId);
    if (msgIndex !== -1) {
        if (!messages[msgIndex].comments) messages[msgIndex].comments = [];
        
        messages[msgIndex].comments.push({
            fromEmail: fromUser.email,
            fromName: fromUser.name,
            text: text
        });

        localStorage.setItem('messages', JSON.stringify(messages));
        renderMessagesWall();
    }
}