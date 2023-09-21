<template>
    <div class="logout">
        <div class="login-button">
        <button class="btn btn-danger btn-lg" @click="login()">YouTubeでログイン</button>
        </div>
    </div>
</template>

<script>
  import { defineComponent } from 'vue';
  
  export default defineComponent({
    name: 'LoginButton',
    //v-on(html上の特定の処理、ボタンクリックなど)をmethodsで記述
    methods: {
        login() {
            return this.$store.dispatch('googleauth')
        }
    }
  })
</script>