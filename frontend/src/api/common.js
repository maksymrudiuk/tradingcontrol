import axios from 'axios'

export const HTTP = axios.create({
  // baseURL: 'http://192.168.43.197:8000/api/v1/'
  baseURL: 'http://127.0.0.1:8000/api/v1/'
})
