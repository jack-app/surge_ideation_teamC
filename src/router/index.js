import { createRouter, createWebHashHistory } from 'vue-router'
import Login from '../components/organisms/LoginView.vue'
import Top from '../components/organisms/TopView.vue'
import { authorizeToken } from './guards'

//構成するルーターを設定
//SPAを実現可能
const routes = [
  {
    path: '/',
    name: 'Top',
    component: Top,
    meta: {
      requiresAuth: true
    }

  },
  {
    path: '/login',
    name: 'Login',
    component: Login
  }
]

//ルーティング情報を扱うルータを作る
const router = createRouter({
  //history: createWebHashHistory(),  //ハッシュでURLを指定する(SPAなどで便利)
  routes
})
//イベントの起きる順番を指定
//beforeEach
//beforeEnter
//beforeRouteEnter
//beforeRouteUpdate
router.beforeEach(authorizeToken) //ログインせずにログイン限定ページのアクセスを防ぐ

export default router
