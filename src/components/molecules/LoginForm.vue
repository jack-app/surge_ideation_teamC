<template>
    <div class="login">
      <div class="form-item">
        <label for="email">Email</label>
        <input
          id="email"
          autocomplete="off"
          type="text"
          v-model="email"
        >
      </div>
      <div class="form-item">
        <label for="password">Password</label>
        <input
          id="password"
          autocomplete="off"
          type="password"
          v-model="password"
        >
      </div>
      <div class="form-item">
        <button class="button" @click="handle()">Login</button>
      </div>
    </div>
  </template>
  
  <script>
  import { defineComponent } from 'vue';
  
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
    //v-on(html上の特定の処理、ボタンクリックなど)をmethodsで記述
    methods: {
      handle() {
        //propsの内容を書き換える
        console.log("OK")
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
  .form-item {
    margin: 0 auto;
    text-align: center;
  }
  
  label {
    display: block;
  }
  
  input {
    width: 50%;
    padding: .5em;
    font: inherit;
  }
  
  button {
    padding: 0.5em;
    margin: 1em;
  }
  </style>
  