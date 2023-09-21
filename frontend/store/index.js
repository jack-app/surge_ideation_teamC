import { createStore } from 'vuex'
import actions from './modules/actions'
import mutations from './modules/mutations'

//vuexのストアをexportする
//actionsでmutationsに備える処理を実行
//mutationsでstoreの値を変更
//vuex4以降はcreateStore

const state = { auth: JSON.parse(localStorage.getItem("data")) }

const store = createStore({
  state,
  actions,
  mutations,
})

export default store;