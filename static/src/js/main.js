// GET COOKIES
function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(';').shift()
}

// LOGOUT
async function logout() {
    fetch('/accounts/logout/', {
        method: 'POST',
        headers: {
            'X-CSRFToken': getCookie('csrftoken')
        }
    }).then(response => {
        response.ok ? window.location.reload() : null;
    })
}

// REMOVE APPLICATION
async function remove_application() {
    const url = window.location.pathname;
    fetch(url, {
        method: 'POST',
        headers: {
            'X-CSRFToken': getCookie('csrftoken')
        },
        body: JSON.stringify({'value':'remove_application'})
    }).then(response => {
        response.json().then(data => {
            if (data['success']) {
                window.location.replace(data['redirectTo']);
            }
        })
    })
}