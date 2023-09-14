import { createStore } from 'vuex'
import actions from '@/store/modules/actions'
import mutations from '@/store/modules/mutations'

const state = {
  auth: {
    token: localStorage.getItem('token'),
    userId: null
  }
}

export default createStore({
  state,
  actions,
  mutations,
})
