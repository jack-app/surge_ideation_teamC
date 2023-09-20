import * as types from '@/store/modules/mutation-types'

//vuexストアのstateの状態を変更
export default {
  [types.LOGIN] (state, payload) {
    state.auth.idtoken = payload.idtoken
    state.auth.refreshtoken = payload.refreshtoken
  },
  [types.LOGOUT] (state, payload) {
    state.auth.idtoken = payload.idtoken
    state.auth.refreshtoken = payload.refreshtoken
  },
  setError(state, error) {
    state.error = error
  },
  clearError(state) {
    state.error = null
  }
}
