import { createStore } from 'vuex'
import { getToken } from "@/utils/auth";
import { getUserInfo } from "@/api";

const store = createStore({
  state () {
    return {
      access_token: '',
      token_type: '',
      user: {
        username: "",
        emial: "",

      }
    }
  },
  getters: {
    loginStatus: () => {
      return Boolean(getToken())
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
  },
  actions: {
    // 获取用户信息
    GetInfo() {
      return new Promise((resolve, reject) => {
        getUserInfo().then(res => {
          resolve(res)
        }).catch(err => {
          reject(err)
        })
      })
    },
    Logout(){

    }
  }
})

export default store
