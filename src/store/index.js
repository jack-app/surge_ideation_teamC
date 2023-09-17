import { createStore } from 'vuex'
import state from './modules/state'
import actions from './modules/actions'
import mutations from './modules/mutations'

console.log("OK");

//vuexのストアをexportする
//actionsでmutationsに備える処理を実行
//mutationsでstoreの値を変更
//vuex4以降はcreateStore
const store = createStore({
  state,
  actions,
  mutations,
})

export default store;