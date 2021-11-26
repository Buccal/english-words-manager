import { createRouter, createWebHashHistory } from 'vue-router'
import Layout from "@/layout";

const routes = [
  {
    path: '',
    component: Layout,
    redirect: "index",
    children: [{
      path: "index",
      component: () => import('@/views/Home.vue'),
      name: "首页",
      meta: { title: "首页", icon: "dashboard", noCache: true, affix: true }
    },
    {
      path: 'frequency',
      name: 'WordFrequency',
      component: () => import('@/views/WordFrequency.vue')
    },
    {
      path: 'known-words-manager',
      name: 'KnownWordsManager',
      component: () => import('@/views/KnownWordsManager.vue'),
    },
    {
      path: 'template-words/:level',
      component: () => import('@/views/TemplateWords.vue'),
      props: true
    }]
  },
  {
    path: '/logo',
    name: 'logo',
    redirect: "index",
    component: () => import('@/views/Home.vue'),
  },
  {
    path: '/logout',
    name: 'logout',
    redirect: "index",
    component: () => import('@/views/Home.vue'),
  },
  // {
  //   path: "/",
  //   component: Layout,
  //   meta:{
  //     requireAuth: true
  //   },
  //   children: [{
  //     path: 'frequency',
  //     name: 'WordFrequency',
  //     component: () => import('@/views/WordFrequency.vue')
  //   },
  //   {
  //     path: 'known-words-manager',
  //     name: 'KnownWordsManager',
  //     component: () => import('@/views/KnownWordsManager.vue'),
  //   },
  //   {
  //     path: 'template-words/:level',
  //     component: () => import('@/views/TemplateWords.vue'),
  //     props: true
  //   }]
  // },
  {
    path: '/login',
    name: 'Login',
    component: () => import('@/views/login.vue')
  },
  {
    path: '/:pathMatch(.*)*',
    name: 'NotFound',
    component: () => import('@/views/404.vue')
  }
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router
