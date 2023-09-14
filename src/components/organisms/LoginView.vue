<template>
    <div class="login-view">
      <LoginForm :login="handleLogin" />
    </div>
  </template>
  
  <script>
  import { defineComponent } from 'vue';
  import LoginForm from '@/components/molecules/LoginForm.vue'
  
  export default defineComponent({
    name: 'LoginView',
    components: {
      LoginForm
    },
  
    methods: {
      handleLogin (authInfo) {
        return this.$store.dispatch('login', authInfo)
          .then(() => {
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
  