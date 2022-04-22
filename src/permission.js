import { ElMessageBox } from 'element-plus'
import router from './router'
import store from './store'

const whiteList = ['/known-words-manager', '/template-words/primary', '/template-words/middle', '/template-words/high', '/logout']

router.beforeEach((to, from, next) => {
  if (store.getters.loginStatus) {
    if (to.path === '/login') {
      next()
    } else {
      /*
      * 判断是否有权限信息
      * 没有权限的请求权限信息，有权限的判断访问地址是否在权限内
      * 若无权限访问，执行登出，重定向到登录页
      */
      // 获取用户信息，并测试令牌是否过期

      // 若无用户信息，请求用户信息
      if(!store.state.user.username){
        store.dispatch('GetInfo').then(() => {
          next()
        }).catch(() => {
          store.commit('$_removeStorage')
        })
      }else{
        next()
      }
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
