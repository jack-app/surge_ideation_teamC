import auth from '@/api/auth'
import * as types from '@/store/modules/mutation-types'
import store from '@/store/index'
import router from '@/router/index'
import { checkErrorMsg } from '@/store/modules/checkErrorMsg'

export default {
  //ログイン時の非同期通信
  login({ commit }, data) {
    auth.login(data.user)
      .then((res) => {
        //ログインに変更
        localStorage.setItem('idToken', res.data.idToken)
        localStorage.setItem('refreshToken', res.data.refreshToken)
        localStorage.setItem('localId', res.data.localId)
        localStorage.setItem('name', res.data.name)
        //mutationを呼び出し
        store.commit(types.LOGIN, res.data)
        store.commit('clearError')
        router.push('/')
      })
      .catch(error => {
        store.commit('setError', checkErrorMsg(error.message))
      })
  },
  //ログアウト時の非同期通信
  logout({ commit }) {
    auth.logout()
      .then((res) => {
        commit(types.LOGOUT, { idtoken: null, refreshtoken: null })
        localStorage.clear()
        router.push('/login')
      })
      .catch(error => { 
        throw error
      })
  },
  //サインアップ時の非同期通信
  signup({ commit }, data) {
    if (data.user.password !== data.user.confirmPassword) {
      store.commit('setError', "入力した二つのパスワードが一致しません")
    } else {
      auth.signup(data.user)
      .then((res) => {
        store.commit('clearError')
        router.push('/login')
      })
      .catch(error => {
        const errorDetail = JSON.parse(error.request.response)
        console.log(errorDetail)
        store.commit('setError', checkErrorMsg(errorDetail.detail))
      })
    }
  }
}