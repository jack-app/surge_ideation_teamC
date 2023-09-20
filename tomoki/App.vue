<script setup>
//composition APIのシンタックスシュガー(異なる構文)
import { RouterView } from 'vue-router'
</script>

<template>
  <RouterView />
>>>>>>> tomoki/database:tomoki/App.vue
</template>

<style>
html:before,
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
