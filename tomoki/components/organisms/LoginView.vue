<template>
  <div class="login-view">
    <LoginForm :login=handleLogin />
  </div>
</template>

<script>
  import { defineComponent } from 'vue';
  import LoginForm from '@/components/molecules/LoginForm.vue';
  
  //setup()によって、template内で値を参照できる
  export default defineComponent({
    //nameはデバッグの区別用
    name: 'LoginView',

    // 子コンポーネントを登録、template内で参照できる
    components: {
        LoginForm
    },

    methods: {
      //ボタンを押した時にhandleLogin(LoginForm.vueのthis.loginで呼び出している)
      handleLogin(authInfo) {

        //Vuexのストアにアクセス
        //非同期処理なので.then()や.catch()を含む
        //内部で別の変数を処理できるので便利
        //storeのactionのloginにアクセス
        return this.$store.dispatch('login', authInfo)

      }
    }
  });
</script>

<style scoped>
.login-view {
  width: 400px;
  margin: auto;
}
</style>
  