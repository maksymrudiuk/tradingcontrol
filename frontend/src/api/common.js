import axios from 'axios'

var baseURL = 'http://127.0.0.1:8000/api/v1/'

if (process.env.NODE_ENV === 'production') {
  baseURL = 'https://trading-control.tk/api/v1/'
}

export const HTTP = axios.create({
  // baseURL: 'http://192.168.43.86:8000/api/v1/'
  baseURL: baseURL
})
