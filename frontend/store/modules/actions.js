import auth from '@/api/auth'
import * as types from '@/store/modules/mutation-types'
import router from '@/router/index'

export default {
  //ログアウト時の処理
  logout({ commit }) {
    commit(types.LOGOUT, null)
    localStorage.clear()
    router.push('/login')
  },
  //Google認証時の非同期通信
  googleauth() {
    auth.googleauth()
      .then((res) => {
        window.location.href = res.data
      })
      .catch((error) => {
        throw error
      })
  }
}