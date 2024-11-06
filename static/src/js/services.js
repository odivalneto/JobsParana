class ApiService {

    constructor(baseURL) {
        this.baseURL = baseURL
    }

    async get(endpoint, headers = {}, params = {}) {
        return await fetch(endpoint, {
            method: 'GET',
            headers: headers,
            body: params,
        }).then(response => response.json())
    }

    async post(endpoint, headers = {}, params = {}) {
        return await fetch(endpoint, {
            method: 'POST',
            headers: headers,
            body: JSON.stringify(params)
        }).then(response => response.json())
            .catch(error => error.response)

    }

    async put(endpoint, headers = {}, params = {}) {
        return await fetch(endpoint, {
            method: 'PUT',
            headers: headers,
            body: JSON.stringify(params)
        }).then(response => response.json())
            .catch(error => error.response)
    }

    async delete(endpoint, headers = {}, params = {}) {
        return await fetch(endpoint, {
            method: 'DELETE',
            headers: headers,
            body: JSON.stringify(params)
        }).then(response => response.json())
            .catch(error => error.response)
    }

    async patch(endpoint, headers = {}, params = {}) {
        return await fetch(endpoint, {
            method: 'PATCH',
            headers: headers,
            body: JSON.stringify(params)
        }).then(response => response.json())
            .catch(error => error.response)
    }
}

export {ApiService};