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
const permaLink = 'http://localhost:8000/api'

export default {
  logout: async () => {
    config.url = permaLink + '/logout'
    config.method = 'post'
    config.data = JSON.parse(localStorage.getItem('data'))
    try {
      const res = await axios.request(config)
    } catch (error) {
      throw error
    }
  },
  googleauth: async () => {
    config.url = permaLink + '/googleauth'
    config.method = 'get'
    console.log(config)
    try {
      const res = await axios.request(config)
      console.log(res.data)
      return res
    } catch (error) {
      throw error
    }
  }
}