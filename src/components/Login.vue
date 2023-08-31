<template>
    <div>
      <button @click="startGoogleAuth">Google認証</button>
    </div>
</template>
  
<script>
  import axios from 'axios';
  
  export default {
    methods: {
      async startGoogleAuth() {
        try {
          // Google認証エンドポイントのURLを取得
          const response = await axios.post('http://localhost:8000/login'); // FastAPIエンドポイントのURLに置き換える
          const authUrl = response.data.auth_url;
  
          // 新しいウィンドウまたはタブでGoogle認証ページを開く
          window.open(authUrl, '_blank');
        } catch (error) {
          console.error('Google認証の開始時にエラーが発生しました', error);
        }
      },
    },
  };
</script>
  