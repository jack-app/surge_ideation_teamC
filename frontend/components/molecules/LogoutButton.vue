<template>
    <div class="logout">
        <div class="logout-button">
        <button class="btn btn-primary btn-lg" @click="logout()">サインアウト</button>
        </div>
    </div>
</template>

<script>
  import { defineComponent } from 'vue';
  
  export default defineComponent({
    name: 'LogoutButton',
    //v-on(html上の特定の処理、ボタンクリックなど)をmethodsで記述
    methods: {
        logout() {
            //storeを介してログアウトを実行
            return this.$store.dispatch('logout')
        }
      }
  })
</script>