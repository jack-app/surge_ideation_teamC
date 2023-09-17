//外部のAPIサーバーとやり取りする
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
    return "OK"
    return axios.request(config)
    //非同期処理のリクエストで成功したら.then()
    //失敗したら.catchを投げる
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
