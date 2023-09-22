import { createRouter, createWebHistory } from 'vue-router'
import Login from '@/components/organisms/LoginView.vue'
import Top from '@/components/organisms/TopView.vue'
import SignUp from '@/components/organisms/SignupView.vue'

import { authorizeToken } from '@/router/guards'

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
  },
  {
    path: '/signup',
    name: 'Signup',
    component: SignUp
  },
]

//ルーティング情報を扱うルータを作る
const router = createRouter({
  history: createWebHistory(),
  routes
})

//イベントの起きる順番を指定
//beforeEach
//全てのルート遷移で、共通のロジックを適用可能

//beforeEnter
//特定のルートのナビゲーション前に実行

//beforeRouteEnter
//特定のコンポーネントのルートが読み込まれる前に実行
//コンポーネント内のデータは使用不可

//beforeRouteUpdate
//同じコンポーネントでルートを変更する時に実行

router.beforeEach(authorizeToken) //ログインせずにログイン限定ページのアクセスを防ぐ

export default router