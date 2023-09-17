import auth from '@/api/auth'
import * as types from '@/store/modules/mutation-types'
import store from '@/store/index'
import router from '@/router/index'

export default {
  //ログイン時の非同期通信
  login({ commit }, data) {
    auth.login(data.user)
      .then((res) => {
        //ログインに変更
        localStorage.setItem('idToken', res.data.idToken)
        localStorage.setItem('refreshToken', res.data.refreshToken)
        //mutationを呼び出し
        store.commit(types.LOGIN, res.data)
        store.commit('clearError')
        router.push('/')
      })
      .catch(error => {
        var msg = ""
        console.log(error)
        console.log(error, error.message, typeof error.message)
        if (error.message === "INVALID_EMAIL") {
          msg = "メールアドレスの形式が正しくありません"
        }
        else if (error.message === "MISSING_PASSWORD") {
          msg = "パスワードが入力されていません"
        }
        else if (error.message === "INVALID_LOGIN_CREDENTIALS") {
          msg = "メールまたはパスワードが間違っています"
        }
        store.commit('setError', msg)
      })
  },
  //ログアウト時の非同期通信
  logout({ commit }) {
    auth.logout()
      .then((res) => {
        localStorage.removeItem('idToken')
        localStorage.removeItem('refreshToken')
        commit(types.LOGOUT, { idtoken: null, refreshtoken: null })
        router.push('/login')
      })
      .catch(error => { 
        throw error
      })
  }
}