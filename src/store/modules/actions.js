import auth from '@/api/auth'
import * as types from './mutation-types'

export default {
  //vuexオブジェクトのcommitを分割代入
  login({ commit }, data) {
    //authコンポーネントの非同期処理結果をreturn
    return auth.login(data.user)
      .then((res) => {
        //ログインに変更
        localStorage.setItem('token', res.data.token)
        //mutationを呼び出し
        commit(types.LOGIN, res.data)
      })
      .catch(error => { throw error })
  },
  logout({ commit }) {
    return auth.logout()
      .then(() => {
        localStorage.removeItem('token')
        commit(types.LOGOUT, { token: null, userId: null })
      })
      .catch(error => { throw error })
  }
}
