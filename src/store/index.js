import { createStore } from 'vuex'

const key = 'user_id'

const store = createStore({
  state () {
    return {
      user_id: localStorage.getItem(key) ? localStorage.getItem(key) : "",
    }
  },
  getters: {
    loginStatus: (state) => {
      return Boolean(state.user_id);
    }
  },
  mutations: {
    $_setStorage(state, payload) {
      state.user_id = payload.user_id;
      localStorage.setItem(key, payload.user_id);
    },
    $_removeStorage(state) {
      state.user_id = "";
      localStorage.removeItem(key);
    }
  },
});

export default store;