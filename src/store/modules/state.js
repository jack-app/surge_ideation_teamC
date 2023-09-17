//storeで取り扱う状態を全て定義
export default {
    auth: {
      token: localStorage.getItem('token'),
      userId: null
    }
}