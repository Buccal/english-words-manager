import { createApp } from 'vue'
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'
// import './assets/styles/themes/theme-day/index.css'
import zhCn from 'element-plus/es/locale/lang/zh-cn'
import App from './App.vue'
import router from './router'
import store from './store'
import HasPermission from './directive/hasPermission'
import './permission'

createApp(App)
  .use(router)
  .use(ElementPlus, { locale: zhCn })
  .use(store)
  .use(HasPermission)
  .mount('#app')
