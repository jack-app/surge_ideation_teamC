import { createApp } from 'vue';
import App from '@/App.vue';
import router from '@/router/index';
import store from '@/store/index';

//フロントエンドのアプリを構成
//引数はVueのルートコンポーネント
const app = createApp(App);

//Vueインダクタンスを構成
//app.use(router);
//app.use(store);

//Vueアプリのインスタンスを作成
app.mount('#app')
