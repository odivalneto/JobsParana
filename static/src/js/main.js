import {ApiService} from "./services.js";

const apiService = new ApiService("localhost:8000")

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

// REMOVE JOB APPLICATION
function remove_application() {
    const url = window.location.pathname;

    try {

        apiService.delete(url, {
            'X-CSRFToken': getCookie('csrftoken'),
            'Accept': 'application/json',
        }, {
            'value': 'remove_application'
        }).then(data => {
            data['statusCode'] === 200 ? window.location.replace(data['redirectToUrl']) : null;
        }).catch(error => {
            console.log(error)
        })

    } catch (error) {
        console.error('Error deleting application', error)
    }
}

// CONFIRM JOB APPLICATION
function confirm_application() {
    const url = window.location.pathname;
    try {
        apiService.post(url, {
            'X-CSRFToken': getCookie('csrftoken'),
            'Accept': 'application/json',
        }, {
            'application': 'success'
        }).then(data => {
            console.log(data)
        })
    } catch (error) {
        console.error('Error add application', error)
    }

}

const remove_action = document.querySelector('#remove_action');
const confirm_action = document.querySelector('#confirm_action')

if (confirm_action) {
    confirm_action.onclick = () => {
        confirm_application()
    }
}

if (remove_action) {
    remove_action.onclick = () => {
        remove_application()
    }
}