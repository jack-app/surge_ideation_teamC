<template>
    <h1>Top page</h1>
    <button class="button" @click="logout()">Logout</button>
  </template>
  
  <script>
  import { defineComponent } from 'vue';
  
  export default defineComponent({
    name: 'TopView',
    methods: {
      //vuexのstoreを実行する
      //ログイン情報はstoreで内部的に変更するので便利
      logout () {
        return this.$store.dispatch('logout')
          .then(() => {
            this.$router.push('/login')
          })
          .catch(error => { throw error })
      }
    }
  });
  </script>
  