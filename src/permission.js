import { ElMessageBox } from 'element-plus'
import router from './router'
import store from './store'
import { removeToken, removeTokenType } from "@/utils/auth";

const whiteList = ['/known-words-manager', '/template-words/primary', '/template-words/middle', '/template-words/high', '/logout']

router.beforeEach((to, from, next) => {
  if (store.getters.loginStatus) {
    if (to.path === '/login') {
      next({ path: '/' })
    } else {
      // 获取用户信息，并测试令牌是否过期
      store.dispatch('GetInfo').then(() => {
        next()
      }).catch(() => {
        store.commit('$_removeStorage')
        removeToken()
        removeTokenType()
        next({ path: '/login' })
      })
    }
  } else {
    if (whiteList.indexOf(to.path) === -1) {
      next() // 不在登录名单里，直接进入
    } else {
      ElMessageBox.confirm(
        '此页面需登录才能访问，请问是否登录',
        '提示',
        {
          confirmButtonText: '登录',
          cancelButtonText: '回首页'
        })
        .then(() => {
          next(`/login?redirect=${to.fullPath}`) // 否则全部重定向到登录页
        })
        .catch(() => {
          console.log(next({ path: '/' }))
        })
    }
  }
})
