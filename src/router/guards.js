//storeの状態に従って、ログイン状態を管理
import store from '../store/index'

/*
ナビゲーションカード(beforeEachなど)のコールバック関数
引数はto,from,next
to ナビゲーション先のルート情報
from 元のルートの情報
next ナビゲーションを制御する
*/
export const authorizeToken = (to, from, next) => {
  if (to.matched.some(page => page.meta.requiresAuth) && (store.state.auth.token === null)) {
    next('/login')
  } else {
    next()
  }
}
