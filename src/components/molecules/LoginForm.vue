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
    data () {
      return {
        email: '',
        password: ''
      }
    },
    props: {
      login: {
        type: Function,
        required: true
      }
    },
    methods: {
      handle () {
        //これがログイン処理
        return this.login({
          'user': {
            'email': this.email,
            'password': this.password,
          }
        })
        .catch(err => { throw err })
      }
    }
  });
  </script>
  
  <style scoped>
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
  