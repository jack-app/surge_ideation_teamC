<script setup>
  import LoginButton from '@/components/molecules/LoginButton.vue';
  import "@/public/blick.css";
  import { useRouter } from 'vue-router'
  import router from '@/router/index'
  import * as types from '@/store/modules/mutation-types'
  import store from '@/store/index'

  // クエリが存在したらログイン認証する
  const query = useRouter().currentRoute.value.query
  console.log(query)
  if (query.id !== undefined && query.token !== undefined && query.name !== undefined && query.icon !== undefined) {
      store.commit(types.LOGIN, query)
      localStorage.setItem("data", JSON.stringify(query))
      router.push('/')
  }
  
</script>

<template>
  <div class="loginpage-view">

    <div class="fix-content">
      <div class="app-title">
        <h4>飛び込もう</h4>
        <div class="no-break"><h1>Surbe</h1><h4>の</h4><h3>世界</h3><h4>へ</h4></div>
      </div>
    </div>
    <div class="fix-content">
      <div class="introduce-text">
      <p>
        楽しいとき悲しいとき落ち込んだとき<br/>
        感情を動かすのは<br/>
        音楽のサビだった・・・<br/>
      </p>
      </div>
    </div>
    <div class="fix-content">
    <div class="error-message blinking-text">{{ queryParam }}</div>
    </div>
    <LoginButton class="login-button"/>
  </div>
</template>

<script>
  export default {
    computed: {
      queryParam() {
        return this.$route.query.error;
      }
    }
  }
</script>

<style scoped>
/* 上 */
html:before {
  height: 5px;
  width: 100vw;
  left: 0;
  top: 0;
  margin-top: 20px;
  opacity: 0.5;
}

/* 右 */
html:after {
  width: 5px;
  height: 100vh;
  right: 0;
  top: 0;
  margin-right: 20px;
  opacity: 0.5;
}

/* 下 */
body:before {
  height: 5px;
  width: 100vw;
  bottom: 0;
  left: 0;
  margin-bottom: 20px;
  opacity: 0.5;
}

/* 左 */
body:after {
  width: 5px;
  height: 100vh;
  top: 0;
  left: 0;
  margin-left: 20px;
  opacity: 0.5;
}

h1 {
  color: #4bace3;
  padding: 0;
  margin: 0;
}
.loginpage-view {
  padding-top: calc(50vh - 130px);
  text-align: center;
  display: block;
}
.loginpage-view > * {
  display: inline-block;
}
.fix-content {
  display: flex;
  justify-content: center;
}
.app-title {
  margin-bottom: 30px;
}
.app-title > * {
  color: #5b8299;
  padding: 0;
  margin: 0;
  text-align: left;
}
.no-break > * {
  display: inline;
}
.introduce-text {
  margin-bottom: 20px;
  text-align: left;
}
.error-message {
  font-family: monospace;
  color: red;
}
</style>