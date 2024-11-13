const mask_date = document.querySelector('#id_birth_date')
const mask_phone = document.querySelector('#id_phone_number')
const mask_zipcode = document.querySelector('#id_zipcode')
const mask_start_date = document.querySelector('#id_start_date')
const mask_end_date = document.querySelector('#id_end_date')

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
    value = value.replace(/(\d{5})(\d)/, "$1-$2"); //75024-040
    input.value = value;
}

if (mask_date) {
    mask_date.oninput = function () {
        maskDate(this);
    }
}

if (mask_start_date && mask_end_date) {
    mask_start_date.oninput = function () {
        maskDate(this);
    }
    mask_end_date.oninput = function () {
        maskDate(this);
    }
}


if (mask_phone) {
    mask_phone.oninput = function () {
        maskPhone(this);
    }
}


