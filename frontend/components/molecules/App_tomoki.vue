<script setup>
import { RouterLink, RouterView } from "vue-router";
import { defineComponent } from "vue";

// 非同期通信のモジュールをインポート
// 無かったら、「npm install axios」をコマンドラインで実行
import axios from "axios";
import { ref, onMounted } from "vue";

// スワイプでスクロールさせない
function disableScroll(event) {
    event.preventDefault();
}

// イベントと関数を紐付け
document.addEventListener("touchmove", disableScroll, { passive: false });
</script>

<template>
    <head>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>surbe</title>
    </head>

    <!-- reset.css destyle -->
    <link
        rel="stylesheet"
        href="https://cdn.jsdelivr.net/npm/destyle.css@1.0.15/destyle.css"
    />

    <body>
        <div class="content">
            <h2 class="title">-surbe-</h2>
            <section id="choice">
                <div class="space1"></div>
                <button class="choice1" @click="click(id_happy)">happy</button>
                <button class="choice2" @click="click(id_sad)">sad</button>
                <button class="choice3" @click="click(id_chill)">chill</button>
                <div class="space2"></div>
                <div class="space3"></div>
                <button class="choice4" @click="click(id_fight)">fight</button>
                <button class="choice5" @click="click(id_like)">like</button>
                <button class="choice6" @click="click(id_etc)">etc</button>
                <div class="spacce4"></div>
            </section>

            <section id="yt-wrap">
                <div id="yt-block">
                    <div class="videoWrapper">
                        <iframe
                            id="player"
                            width="80%"
                            height="60%"
                            :src="video"
                            frameborder="0"
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

                <button class="play" @click="playFirstVideo">▶</button>
                <button class="fav">♡</button>
            </div>
        </div>
    </body>
</template>

<style>
/* html:before,
html:after,
body:before,
body:after {
  content: '';
  background: #5b8299;
  position: fixed;
  display: block;
  z-index: -1;
}

/* 上 */
/* html:before {
  height: 5px;
  width: 100vw;
  left: 0;
  top: 0;
  margin-top: 20px;
  opacity: 0.5;
}

/* 右 */
/* html:after {
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

<script>
const videoUrls = ref([
    "https://www.youtube.com/embed/oy6MDr6I6rM?start=10&end=20",
    "https://www.youtube.com/embed/bqigIHMComEstart=10&end=20",
    "https://www.youtube.com/embed/m34DPnRUfMUstart=10&end=20",
    // 他のURLを追加
]);

const currentVideoUrl = ref(""); // 現在の動画URLを保持するリファレンス

// ページが読み込まれたときに初期動画を設定
onMounted(() => {
    playFirstVideo();
});

// 動画を再生する関数
function playVideo(videoIndex) {
    currentVideoUrl.value = videoUrls.value[videoIndex];
}

// 最初の動画を再生する関数
function playFirstVideo() {
    if (videoUrls.value.length > 0) {
        video = videoUrls.value[0];
    }
}

//感情ボタンクリックするとバックに送る
export default defineComponent({
    name: "sendPlaylistID",
    data() {
        const data = JSON.parse(localStorage.getItem("data"))
        return {
            id_happy:   data.happy,
            id_sad:     data.sad,
            id_chill:   data.chill,
            id_fight:   data.fight,
            id_like:    data.like,
            id_etc:     data.etc
        }
    },
    methods: {
        async click(playlistID) {
            // プレイリストIDを送る処理を書く

            // これはWebサイトのHeader情報(変えないほうがいい)
            const headers = {
                "Access-Control-Allow-Origin": "*",
                "Content-type": "application/json",
            };

            // Webサイトの中身のデータ部分
            const config = {
                method: "post",
                url: import.meta.env.VITE_APP_BACKEND_URL + "/api/playlistid",
                headers,
                data: {
                    playlistID: playlistID,
                },
            };

            try {
                const res = await axios.request(config);
                console.log(res);
            } catch (error) {
                throw error;
            }
        }
    },
});
</script>
