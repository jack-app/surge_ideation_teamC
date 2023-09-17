import * as types from './mutation-types'

//vuexストアのstateの状態を変更
export default {
  [types.LOGIN] (state, payload) {
    state.auth.token = payload.token
    state.auth.userId = payload.userId
  },
  [types.LOGOUT] (state, payload) {
    state.auth.token = payload.token
    state.auth.userId = payload.userId
  },
}
