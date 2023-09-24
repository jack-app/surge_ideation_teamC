//外部のAPIサーバーとやり取りする
import axios from 'axios'

const headers = {
  'Access-Control-Allow-Origin': '*',
  'Content-type': 'application/json',
}
const config = {
  method: null,
  url: null,
  headers,
  data: null
}

export default {
  logout: async () => {
    config.url = import.meta.env.VITE_APP_BACKEND_URL + '/api/logout'
    config.method = 'post'
    config.data = JSON.parse(localStorage.getItem('data'))
    await axios.request(config)
  },
  googleauth: async () => {
    config.url = import.meta.env.VITE_APP_BACKEND_URL + '/api/googleauth'
    config.method = 'get'
    console.log(config)
    const res = await axios.request(config)
    return res
  }
}