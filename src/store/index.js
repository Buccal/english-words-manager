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
        email: "",

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
      // 删除已经失效或过期的token（不删除也可以，因为登录后覆盖）
      localStorage.clear()
      // ...

    }
  }
})

export default store
