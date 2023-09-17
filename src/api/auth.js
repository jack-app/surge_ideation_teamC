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
  login: async (authInfo) => {
    config.url = permaLink + '/login'
    config.method = 'post'
    config.data = authInfo
    try {
      const res = await axios.request(config)
      if (res.data.error !== undefined) {
        throw new Error(res.data.error.message)
      }
      else {
        return res
      }
    } catch (error) {
      throw error
    }
  },
  logout: async () => {
    config.url = permaLink + '/logout'
    config.method = 'post'
    config.data = {
      "id_token": localStorage.getItem('idToken')
    }
    try {
      const res = await axios.request(config)
    } catch (error) {
      throw error
    }
  }
}