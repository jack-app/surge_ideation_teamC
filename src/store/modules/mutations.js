import * as types from './mutation-types'

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
