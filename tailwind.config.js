/** @type {import('tailwindcss').Config} */
module.exports = {
    content: [
        './templates/**/*.html',
        './node_modules/flowbite/**/*.js',
        './static/src/js/*.js',
        './static/src/css/*.css',
    ],
    theme: {
        extend: {
            colors: {
                primary: {
                    "50": "#eff6ff",
                    "100": "#076ca9",
                    "hover": "#077eca",

                },
                secondary: {
                    "50": "#ddffcb",
                    "100": "#257f00"
                }
            }
        },
        letterSpacing: {
            'max': '.20em'
        }
    },
    plugins: [
        require('flowbite/plugin')
    ],
}

