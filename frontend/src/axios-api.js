import axios from 'axios'

// axios.defaults.xsrfCookieName = 'csrftoken';
// axios.defaults.xsrfHeaderName = 'X-CSRFToken';

const getAPI = axios.create({
    baseURL: 'http://127.0.0.1:8000',
    timeout: 1000,
//     headers: {
//         "Content-Type": "application/json",
//         "X-CSRFToken": Cookies.get('csrftoken')
//    },
})

export { getAPI }