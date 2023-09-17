<template>
  <div class="login-view">
    <LoginForm :login=handleLogin />
  </div>
</template>
  
<script>
  import { defineComponent } from 'vue';
  import LoginForm from '@/components/molecules/LoginForm.vue';
  import { mapState, mapActions } from 'vuex';
  
  //setup()によって、template内で値を参照できる
  export default defineComponent({
    //nameはデバッグの区別用
    name: 'LoginView',

    // 子コンポーネントを登録、template内で参照できる
    components: {
        LoginForm
    },

    computed: {
      ...mapState({
        token: 'test'
      })
    },

    methods: {
      //ボタンを押した時にhandleLogin
      handleLogin (authInfo) {
        //Vuexのストアにアクセス
        //非同期処理なので.then()や.catch()を含む
        //内部で別の変数を処理できるので便利
        console.log(this.$store, this.store)

        //storeのactionのloginにアクセス
        return this.$store.dispatch('login', authInfo)
          .then(() => {
            //$routerでVue Routerにアクセス
            //特定のルートに移動
            this.$router.push({ path: '/' })
          })
          .catch(err => { throw err })
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
  