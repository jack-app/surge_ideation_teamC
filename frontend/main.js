import { createApp } from 'vue';
import App from '@/App.vue';
import router from '@/router/index';
import store from '@/store/index';
import VueYoutube from 'vue-youtube-vue-3';

//フロントエンドのアプリを構成
//引数はVueのルートコンポーネント
const app = createApp(App);

//Vueインダクタンスを構成
app.use(router);
app.use(store);
app.use(VueYoutube) // YouTubeの制御方法

//Vueアプリのインスタンスを作成
app.mount('#app')
