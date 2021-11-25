import { ElMessageBox } from 'element-plus'
import router from './router'
import store from './store'

const whiteList = ['/login', '/index', '/frequency']

router.beforeEach((to, from, next) => {
  if (store.getters.loginStatus) {
    // if (to.path === '/login') {
    //   next({ path: '/' })
    // } else {
    //   // 判断store初始化信息是否完成，否则，dispatch actions
    // }
    next();
  } else {
    if (whiteList.indexOf(to.path) !== -1) {
      next(); // 在免登录白名单，直接进入
    } else {
      ElMessageBox.confirm(
        '此页面需登录才能访问，请问是否登录',
        '提示',
        {
          confirmButtonText: '登录',
          cancelButtonText: '回首页',
        })
      .then(() => {
        next(`/login?redirect=${to.fullPath}`) // 否则全部重定向到登录页
      })
      .catch(() => {
        console.log(next({ path: '/' }));
      })
    }
  }
});