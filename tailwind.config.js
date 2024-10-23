/** @type {import('tailwindcss').Config} */
module.exports = {
    content: [
        './templates/**/*.html',
        './node_modules/flowbite/**/*.js'
    ],
    theme: {
        extend: {
            colors: {
                primary: {
                    "50": "#eff6ff",
                    "100": "#076ca9",
                },
                secondary: {
                    "50": "#ddffcb",
                    "100": "#257f00"
                }
            }
        },
    },
    plugins: [
        require('flowbite/plugin')
    ],
}

