import { createStore } from 'vuex'
import actions from '@/store/modules/actions'
import mutations from '@/store/modules/mutations'

//storeで取り扱う状態を全て定義
const state = {
  auth: {
    token: localStorage.getItem('token'),
    userId: null
  }
}

//vuexのストアをexportする
//actionsでmutationsに備える処理を実行
//mutationsでstoreの値を変更
export default createStore({
  state,
  actions,
  mutations,
})
