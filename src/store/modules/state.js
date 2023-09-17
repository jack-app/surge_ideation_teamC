//storeで取り扱う状態を全て定義
export default {
    auth: {
      idtoken: localStorage.getItem('idToken'),
      refreshtoken: localStorage.getItem('refreshToken')
    },
    error: null
}