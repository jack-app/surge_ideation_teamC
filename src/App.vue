<script setup>
import { RouterLink, RouterView } from 'vue-router'
function disableScroll(event) {
  event.preventDefault()
}

// イベントと関数を紐付け
document.addEventListener('touchmove', disableScroll, { passive: false })
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
      <section id="choice">
        <div class="space1"></div>
        <button class="choice1">happy</button>
        <button class="choice2">sad</button>
        <button class="choice3">chill</button>
        <div class="space2"></div>
        <div class="space3"></div>
        <button class="choice4">fight</button>
        <button class="choice5">like</button>
        <button class="choice6">etc</button>
        <div class="spacce4"></div>
      </section>

      <section id="music">
        <p class="music1">だから僕は音楽をやめた</p>
        <p class="music1">愛を伝えたいだとか</p>
        <p class="music1">私は最強</p>
      </section>

      <section id="recommend">
        <h1 class="if">if...</h1>
        <p class="music2">music</p>
        <p class="music2">music</p>
      </section>

      <div class="player">
        <h1 class="feel">feeling list</h1>
        <button class="play">▶</button>
        <button class="fav">♡</button>
      </div>
    </div>
  </body>
</template>