import axios from 'axios'

const headers = {}
headers['Content-type'] = 'application/json'

const config = {
  method: null,
  url: 'http://localhost:8081', // APIサーバー
  headers,
  data: null
}

export default {
  login: (authInfo) => {
    config.method = 'post'
    config.data = authInfo

    return axios.request(config)
      .then(res => res)
      .catch(error => { throw error })
  },
  logout: () => {
    config.method = 'delete'
    return axios.request(config)
      .then(res => res)
      .catch(error => { throw error })
  }
}
