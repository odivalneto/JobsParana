const search_input = document.querySelector("#search-input");

search_input.addEventListener("input", (e) => {
    e.preventDefault();
    fetch('/jobs/?search=' + e.target.value, {
        method: 'GET',
        mode: 'cors',

    }).then(res => res.ok).then(data => {
        console.log(data)
    })
})

