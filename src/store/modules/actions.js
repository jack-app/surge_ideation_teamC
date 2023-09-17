import auth from '@/api/auth'
import * as types from './mutation-types'

export default {
  //ログイン時の非同期通信
  login({ commit }, data) {
    auth.login(data.user)
      .then((res) => {
        //ログインに変更
        localStorage.setItem('idToken', res.data.idToken)
        localStorage.setItem('refreshToken', res.data.refreshToken)
        //mutationを呼び出し
        commit(types.LOGIN, res.data)
        window.location.href = "/"
      })
      .catch(error => {
        throw error //エラーを親コンポーネントに伝える
      })
  },
  //ログアウト時の非同期通信
  logout({ commit }) {
    auth.logout()
      .then((res) => {
        localStorage.removeItem('idToken')
        localStorage.removeItem('refreshToken')
        commit(types.LOGOUT, { idtoken: null, refreshtoken: null })
      })
      .catch(error => { 
        throw error
      })
  }
}