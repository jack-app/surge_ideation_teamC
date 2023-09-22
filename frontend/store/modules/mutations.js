import * as types from '@/store/modules/mutation-types'

//vuexストアのstateの状態を変更
export default {
  [types.LOGIN] (state, payload) {
    state.auth = payload
  },
  [types.LOGOUT] (state, payload) {
    state.auth = payload
  }
}
