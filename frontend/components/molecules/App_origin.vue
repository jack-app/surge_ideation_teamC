<script setup>
import { ref, onMounted, defineComponent } from "vue"
import store from '@/store/index'

// 非同期通信のモジュールをインポート
import axios from 'axios';

// スワイプでスクロールさせない
function disableScroll(event) {
  event.preventDefault()
}

// イベントと関数を紐付け
document.addEventListener('touchmove', disableScroll, { passive: false })

// 本来はバックエンドからプレイリストID内の動画URLを記述する
const videoUrls = ref([
  'https://www.youtube.com/embed/oy6MDr6I6rM?start=10&end=20',
  'https://www.youtube.com/embed/bqigIHMComE?start=10&end=20',
  'https://www.youtube.com/embed/m34DPnRUfMU?start=10&end=20'
  // 他のURLを追加
])

// const currentVideoIndex = ref(0)

console.log(store.state.auth)

// // 現在の動画URLを取得
const currentVideoUrl = ref(videoUrls.value[0])

// // YouTubeプレーヤーの読み込み完了時の処理
// function onVideoPlayerLoad() {
//   const player = document.getElementById('player')
//   player.addEventListener('pause', (event) => {
//     // 動画が一時停止されたら次の動画に切り替えて再生
//     playNextVideo()
//     console.log('hello')
//   })
// }

// // 次の動画を再生する関数
// function playNextVideo() {
//   currentVideoIndex.value = (currentVideoIndex.value + 1) % videoUrls.value.length
//   currentVideoUrl.value = videoUrls.value[currentVideoIndex.value] // URLを更新
//   const player = document.getElementById('player')
//   player.src = currentVideoUrl.value
//   player.play()
// }

function nextVideo() {
  const currentIndex = videoUrls.value.indexOf(videoUrl.value)
  if (currentIndex < videoUrls.value.length - 1) {
    videoUrl.value = videoUrls.value[currentIndex + 1]
  }
}

onMounted(() => {
  // 初期の動画が再生された後、次の動画に切り替えるタイマーをセット
  setTimeout(nextVideo, 10000) // 10秒後に次の動画に切り替える例
})
</script>

<template>
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>surbe</title>
  </head>

  <!-- reset.css destyle -->
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/destyle.css@1.0.15/destyle.css" />

  <body>
    <div class="content">
      <h2 class="title">-surbe-</h2>

      <!-- この中のbuttonタグが感情を表すボタン -->
      <!-- @click="関数名" でボタンをクリックしたときに関数を実行できる -->
      <section id="choice">
        <div class="space1"></div>
        <button class="choice1" @click="click()">happy</button>
        <button class="choice2">sad</button>
        <button class="choice3">chill</button>
        <div class="space2"></div>
        <div class="space3"></div>
        <button class="choice4">fight</button>
        <button class="choice5">like</button>
        <button class="choice6">etc</button>
        <div class="spacce4"></div>
      </section>

      <!-- <section id="music">
        <p class="music1">だから僕は音楽をやめた</p>
        <p class="music1">愛を伝えたいだとか</p>
        <p class="music1">私は最強</p>
      </section> -->
      <section id="yt-wrap">
        <div id="yt-block">
          <div class="videoWrapper">
            <iframe
              id="player"
              width="80%"
              height="60%"
              :src="currentVideoUrl"
              frameborder="0"
              @load="onVideoPlayerLoad"
              @ended="playNextVideo"
            ></iframe>
          </div>
          <span id="play"></span>
        </div>
      </section>

      <section id="recommend">
        <h1 class="if">if...</h1>
        <p class="music2">music</p>
        <p class="music2">music</p>
      </section>

      <div class="player">
        <h1 class="feel">feeling list</h1>

        <!-- 再生ボタン部分 これを押して再生・停止を交互に切り替えたい-->
        <button class="play">▶</button>
        
        <button class="fav">♡</button>
      </div>
    </div>
  </body>
</template>

<script>
export default defineComponent({
    name: 'SendPlaylistID',
    methods: {
        async click() {
            // プレイリストIDを送る処理を書く

            // これはWebサイトのHeader情報(変えないほうがいい)
            const headers = {
              'Access-Control-Allow-Origin': '*',
              'Content-type': 'application/json',
            }

            // Webサイトの中身のデータ部分
            const config = {
              method: 'post',
              url: import.meta.env.VITE_APP_BACKEND_URL + '/api/playlistid',
              headers,
              data: {
                // これは「楽しい感情」のプレイリストID
                // これ以外にも「悲しい感情」「寂しい感情」などのプレイリストIDを、ボタンに合わせて振り分けていきたい
                playlistID: 'PLNG3n51ur1CeF29__IjcUS09_ME66_pVQ'
              },
            }

            try {
              //　ここからバックエンドとやり取りを行う
              const res = await axios.request(config)

              // 動作確認用のconsole.log()
              console.log(res.data)
            } catch (error) {
              throw error
            }
        }
    }
})
</script>

<style>
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
html,
body {
  overflow: hidden;
  font-family: Arial Black;
}

h1,
h2 {
  color: #5b8299;
}

h1 {
  padding: 3px;
  margin-left: 10%;
}

.title {
  margin-top: 10%;
  font-size: xx-large;
  text-align: center;
  margin-bottom: 4%;
}

.content {
  width: 100%;
  height: 100%;
  position: absolute;
  margin-top: 5%;
  margin-left: auto;
  margin-right: auto;
  border: #000;
}

.choice {
  flex-wrap: wrap;
}

.choice1 {
  width: 17%;
  height: 30px;
  background-color: #e9af9d;
  color: whitesmoke;
  opacity: 0.7;
  text-align: center;
  margin: 2%;
  margin-left: 20%;
}

.choice2 {
  width: 17%;
  height: 30px;
  background-color: #a2c4de;
  color: whitesmoke;
  opacity: 0.7;
  text-align: center;
  margin: 2%;
}

.choice3 {
  width: 17%;
  height: 30px;
  background-color: #9de2d6;
  color: whitesmoke;
  opacity: 0.7;
  text-align: center;
  margin: 2%;
}

.choice4 {
  width: 17%;
  height: 30px;
  background-color: #949494;
  color: whitesmoke;
  opacity: 0.7;
  text-align: center;
  margin: 2%;
  margin-left: 20%;
}

.choice5 {
  width: 17%;
  height: 30px;
  background-color: #c7add6;
  color: whitesmoke;
  opacity: 0.7;
  text-align: center;
  margin: 2%;
}

.choice6 {
  width: 17%;
  height: 30px;
  background-color: #5b8299;
  color: whitesmoke;
  opacity: 0.7;
  text-align: center;
  margin: 2%;
}
.videoWrapper {
  text-align: center;

  margin-top: 5%;
}

.if {
  margin-top: 5%;
  margin-left: 13%;
  font-size: x-large;
}

.music1 {
  text-align: center;
  width: 80%;
  margin-left: 10%;
  margin-top: 5%;
  padding: 1%;
  background-color: #fff;
}

#music {
  background-color: #5b8299;
  display: block;
  margin-top: 4%;
  margin-left: 20%;
  margin-right: 20%;
  width: 60%;
  height: 20%;
  padding-top: 5%;

  opacity: 0.7;
}

.music2 {
  text-align: center;
  width: 50%;
  margin-top: 1%;
  margin-left: 25%;
  margin-bottom: 2%;
  padding: 1%;
  background-color: #e9af9d;
  opacity: 0.7;
}

.feel {
  margin-top: 5%;
  font-size: x-large;
}

.play {
  margin-top: 5%;
  margin-left: 38%;
  font-size: 80px;
  color: #5b8299;
}

.fav {
  margin-top: 10%;
  margin-left: 10%;
  padding-top: 10%;
  font-size: xx-large;
  color: #ce8bbf;
}

.player {
  width: 75%;
  margin-left: 13%;
  border-bottom: solid #5b8299;
}

/* sp */
@media screen and (max-width: 600px) {
}
</style>
