<template>
  <div class="login">
    <div class="login-header">
      <div class="login-text">Surbeにログイン</div>
      <div v-if="error" class="error-message blinking">{{ error }}</div>
    </div>
    <div class="input-item">
      <div class="input-item-fix">
      <input
        id="email"
        autocomplete="off"
        type="text"
        v-model="email"
        placeholder="メールアドレス"
        required
        autofocus
      >
      </div>
      <div class="input-item-fix">
      <input
        id="password"
        autocomplete="off"
        type="password"
        v-model="password"
        placeholder="パスワード"
        required
      >
      </div>
    </div>
    <div class="setup-button">
      <button class="btn btn-primary btn-lg" @click="signin()">サインイン</button>
      <button class="btn btn-primary btn-lg" @click="signup()">サインアップ</button>
    </div>
  </div>
</template>
  
<script>
  import { defineComponent } from 'vue';
  import { mapState } from 'vuex';
  import "@/public/blick.css";
  
  export default defineComponent({
    name: 'LoginForm',

    //データを定義、this.emailなどで参照できる
    data() {
      return {
        email: '',
        password: ''
      }
    },
    //親コンポーネントから受け取るpropsの情報を指定
    //requiredは必須
    props: {
      //こうすることで、this.login形式で記述できる
      login: {
        type: Function,
        required: true
      }
    },
    //エラーメッセージを検出
    computed: {
      ...mapState(['error'])
    },
    //v-on(html上の特定の処理、ボタンクリックなど)をmethodsで記述
    methods: {
      signin() {
        //propsの内容を書き換える
        //thisはそのコンポーネント自体を返す
        return this.login({
          'user': {
            'email': this.email,
            'password': this.password,
          }
        })
        //エラーを表示する
        .catch(err => { throw err })
      }
    }
  });
</script>
  
<style scoped>
/* scopedを付けると現在のコンポーネントのみ適用 */
input {
  width: 100%;
  padding: .5em;
  font: inherit;
}
button {
  padding: 0.5em 1em;
  margin: 1em 0;
}
.login {
  display: block;
}
.login-text {
  text-align: center;
  font-size: 30px;
  margin: 1em 0;
}
.input-item {
  text-align: left;
}
.input-item-fix {
  margin: 0.5em 0;
}
.setup-button {
  text-align: center;
}
.setup-button > * {
  margin: 10px;
}
.error-message {
  color: red;
}
</style>
