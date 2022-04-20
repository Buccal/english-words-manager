// 引入axios
import axios from 'axios'

// 【非必要】 引入错误提示语
import errorCode from '@/utils/errorCode'
import store from '@/store/index'

import { getToken, getTokenType } from '@/utils/auth'
import { ElMessage, ElMessageBox } from 'element-plus'

// 设置默认请求头
axios.defaults.headers['Content-Type'] = 'application/json'

// 设置默认请求地址
axios.defaults.baseURL = 'http://127.0.0.1:8000/'

// 设置默认的请求超时时间
axios.defaults.timeout = 10000

const server = axios.create()

// 请求拦截器
server.interceptors.request.use(
  config => {
    if (config.url === '/user/register' || config.url === '/user/login') {
      config.data = 'grant_type=password&username=' + config.data.username + '&password=' + encodeURIComponent(config.data.password)
      config.headers['Content-Type'] = 'application/x-www-form-urlencoded'
    } else {
      // 判断是否存在token
      if (store.getters.loginStatus) {
        // 每个http header都加上token
        config.headers.Authorization = getTokenType() + ' ' + getToken()
      }

      // get请求映射params参数
      if (config.method === 'get' && config.params) {
        // 拼接请求地址
        let url = config.url + '?'
        for (const propName of Object.keys(config.params)) {
          const value = config.params[propName]
          let part = encodeURIComponent(propName) + '='
          if (value !== null && typeof (value) !== 'undefined') {
            if (typeof value === 'object') {
              for (const key of Object.keys(value)) {
                const params = propName + '[' + key + ']'
                let subPart = encodeURIComponent(params) + '='
                url += subPart + encodeURIComponent(value[key]) + '&'
              }
            } else {
              url += part + encodeURIComponent(value) + '&'
            }
          }
        }
        url = url.slice(0, -1)
        config.params = {}
        config.url = url
      }
    }

    return config
  },
  err => {
    this.$router.push('/login').then(() => {})
    return Promise.reject(err)
  })

// 响应拦截器
server.interceptors.response.use(function (res) {
  const rtn = res.data
  // 映射错误信息
  rtn.msg = rtn.msg || res.data.msg || errorCode[rtn.code] || errorCode.default

  if (rtn.code === 401) {
    ElMessageBox.confirm('登录状态已过期，您可以继续留在该页面，或者重新登录', '系统提示', {
        confirmButtonText: '重新登录',
        cancelButtonText: '取消',
        type: 'warning'
      }
    ).then(() => {
      store.dispatch('Logout').then(() => {
        this.$router.replace({
          // 跳转到登录页重新获取token
          path: '/login',
          query: {
            // 登陆后回到当前页面
            redirect: this.$router.currentRoute.fullPath
          }
        }).then(() => {})
      })
    }).catch(() => { });
  } else if (!/^2/.test(rtn.code)) {
    rtn.status = 0
    // return
    return rtn
  }else{
    rtn.status = 1
    return rtn
  }
}, function (error) {
  let { message } = error.toJSON();
  if (message === 'Network Error') {
    message = '后端接口连接异常'
  } else if (message.includes('timeout')) {
    message = '系统接口请求超时'
  } else if (message.includes('Request failed with status code')) {
    message = '系统接口' + message.substr(message.length - 3) + '异常'
  }
  if(!message) message = "系统未知错误，请反馈给管理员"
  ElMessage({
    message: message,
    type: 'error',
    duration: 5 * 1000
  })
  return Promise.reject(error)
})

export default server
