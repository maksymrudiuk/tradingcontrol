import axios from 'axios'

export const HTTP = axios.create({
  baseURL: process.env.NODE_ENV === 'production'
    ? 'https://trading-control.tk/api/v1/'
    : 'http://127.0.0.1:8000/api/v1/'
})
