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

