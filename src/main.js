import { createApp } from 'vue'
import App from './App.vue'
import router from './router/index'

//フロントエンドのアプリを構成
//引数はVueのルートコンポーネント
const app = createApp(App)

//必要なプラグインを構成
app.use(router)

//Vueアプリのインスタンスを作成
app.mount('#app')
