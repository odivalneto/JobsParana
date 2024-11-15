import {ApiService} from "./services.js";

const apiService = new ApiService("localhost:8000")

const is_actual_work = document.querySelector("#id_is_actual");

if (mask_date && is_actual_work) {
    is_actual_work.addEventListener("change", (e) => {

        mask_date.forEach(e => {
            if (e.id === 'id_end_date') {
                e.value = null;
                e.disabled = is_actual_work.checked;
                e.required = !is_actual_work.checked;
            }
        })

    })
}

// BUTTONS ACTIONS
const remove_action = document.querySelector('#remove_action');
const confirm_action = document.querySelector('#confirm_action')
const logout_action = document.querySelector('#logout_action');

//FORM ADDRESS
const address = document.getElementById('id_address');
const country = document.getElementById('id_country');
const state = document.getElementById('id_state');
const city = document.getElementById('id_city');
const region = document.getElementById('id_region');
const number = document.getElementById('id_number');
const complement = document.getElementById('id_complement');

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

if (logout_action) {
    logout_action.onclick = () => {
        logout()
    }
}

// GET COOKIES
function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(';').shift()
}

// LOGOUT
function logout() {
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
            data['statusCode'] === 200 ? window.location.replace(data['redirectToUrl']) : null;
        })
    } catch (error) {
        console.error('Error add application', error)
    }

}


if (mask_zipcode) {
    mask_zipcode.oninput = async function () {
        maskZipcode(this)
        if (mask_zipcode.value.length === 9) {
            await get_address_zipcode(mask_zipcode.value)
        }
    }
}

// GET ADDRESS BY ZIPCODE
async function get_address_zipcode(zipcode) {
    const baseURL = `https://viacep.com.br/ws/${zipcode.replace('-', '')}/json/`
    try {
        fetch(baseURL, {
            method: 'GET',
        }).then(response => response.json())
            .then(data => {

                if (!data['erro']) {
                    state.value = data['estado']
                    region.value = data['bairro']
                    city.value = data['localidade']
                    address.value = data['logradouro']
                    country.value = 'Brasil'
                    number.value = ''
                    complement.value = ''
                }

            })
    } catch (e) {
        console.error('Error get zipcode', e)
    }

}