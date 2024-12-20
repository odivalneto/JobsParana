// const mask_date = document.querySelector('#id_birth_date')
const mask_phone = document.querySelector('#id_phone_number')
const mask_zipcode = document.querySelector('#id_zipcode')
const mask_date = document.querySelectorAll('#id_start_date, #id_end_date, #id_birth_date')

// MASK DATE
function maskDate(input) {
    let value = input.value.replace(/\D/g, "");
    value = value.replace(/(\d{2})(\d)/, "$1/$2");
    value = value.replace(/(\d{2})(\d)/, "$1/$2");
    input.value = value;
}

// MASK PHONE NUMBER
function maskPhone(input) {
    let value = input.value.replace(/\D/g, "");
    value = value.replace(/^(\d{2})(\d)/g, "($1) $2");
    value = value.replace(/(\d{5})(\d)/, "$1-$2");
    input.value = value;
}

// MASK ZIPCODE
function maskZipcode(input) {
    let value = input.value.replace(/\D/g, "");
    value = value.replace(/(\d{5})(\d)/, "$1-$2");
    input.value = value;
}

if (mask_date) {
    mask_date.oninput = function () {
        maskDate(this);
    }
}

if (mask_date) {
    mask_date.forEach(e => {
        e.oninput = function () {
            maskDate(this);
        }
    })
}


if (mask_phone) {
    mask_phone.oninput = function () {
        maskPhone(this);
    }
}


