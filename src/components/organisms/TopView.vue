<template>
    <h1>Top page</h1>
    <button class="button" @click="logout()">Logout</button>
  </template>
  
  <script>
  import { defineComponent } from 'vue';
  
  export default defineComponent({
    name: 'TopView',
    methods: {
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
  