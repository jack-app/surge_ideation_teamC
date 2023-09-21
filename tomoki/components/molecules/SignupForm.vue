<template>
    <div class="setup-form">
    <div class="setup-header">
      <div class="setup-text">Surbeに新規登録</div>
      <div v-if="error" class="error-message blinking-text">{{ error }}</div>
    </div>
    <form @submit.prevent="signup()">
    <div class="input-item">
      <div class="input-item-fix">
      <input
        id="name"
        autocomplete="off"
        type="text"
        v-model="name"
        placeholder="ユーザー名(半角・全角文字可)"
        required
        autofocus
      >
      </div>
      <div class="input-item-fix">
      <input
        id="email"
        autocomplete="off"
        type="text"
        v-model="email"
        placeholder="メールアドレス"
        required
      >
      </div>
      <div class="input-item-fix">
      <input
        id="password"
        autocomplete="off"
        type="password"
        v-model="password"
        placeholder="パスワード(6文字以上)"
        required
      >
      </div>
      <div class="input-item-fix">
      <input
        id="confirm"
        autocomplete="off"
        type="password"
        v-model="confirmPassword"
        placeholder="パスワードを再度入力"
        required
      >
      </div>
    </div>
    <div class="setup-button">
      <button class="btn btn-secondary btn-lg" @click="login()">サインイン</button>
      <button class="btn btn-primary btn-lg" type="submit">サインアップ</button>
    </div>
    </form>
  </div>
</template>

<script>
  import { defineComponent } from 'vue';
  import { mapState } from 'vuex';
  import "@/public/blick.css";

  export default defineComponent({
    //nameはデバッグの区別用
    name: 'SetupForm',

    //データを定義、this.emailなどで参照できる
    data() {
      return {
        name: '',
        email: '',
        password: '',
        confirmPassword: ''
      }
    },
    props: {
      setup: {
        type: Function,
        required: true
      }
    },
    //エラーメッセージを検出
    computed: {
      ...mapState(['error'])
    },
    methods: {
      signup() {
        return this.setup({
          'user': {
            'name': this.name,
            'email': this.email,
            'password': this.password,
            'confirmPassword': this.confirmPassword
          }
        })
        .catch(err => { throw err })
      },
      login() {
        this.$router.push("/login")
      }
    }
  })
</script>

<style scoped>
input {
  width: 100%;
  padding: .5em;
  font: inherit;
}
button {
  padding: 0.5em 1em;
  margin: 1em 0;
}
.setup-form {
  display: block;
}
.setup-text {
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
  display: block;
  height: 1em;
  color: red;
}
</style>