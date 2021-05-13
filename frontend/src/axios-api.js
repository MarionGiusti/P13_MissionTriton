import axios from 'axios'

const baseURL = process.env.VUE_APP_ROOT_API

const getAPI = axios.create({
    baseURL: baseURL,
    timeout: 1000,
})

export { getAPI, baseURL }
