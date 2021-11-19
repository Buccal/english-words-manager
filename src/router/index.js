import { createRouter, createWebHashHistory } from 'vue-router'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: () => import('../views/Home.vue')
  },
  {
    path: '/login',
    name: 'Login',
    component: () => import('../views/login.vue')
  },
  {
    path: '/frequency',
    name: 'WordFrequency',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/WordFrequency.vue')
  },
  {
    path: '/knownWordsManager',
    name: 'KnownWordsManager',
    component: () => import('../views/KnownWordsManager.vue')
  }
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router
