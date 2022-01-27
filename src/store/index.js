import { createStore } from 'vuex'

const store = createStore({
  state () {
    return {
      access_token: '',
      token_type: ''
    }
  },
  getters: {
    loginStatus: (state) => {
      return Boolean(state.access_token)
    }
  },
  mutations: {
    $_setStorage (state, payload) {
      state.access_token = payload.access_token
      state.token_type = payload.token_type
    },
    $_removeStorage (state) {
      state.access_token = ''
    }
  }
})

export default store
