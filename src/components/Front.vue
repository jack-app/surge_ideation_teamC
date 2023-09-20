<template>
  <!doctype html>
  <html lang="ja">
    <head>
      <meta charset="UTF-8" />
      <meta name="viewport" content="width=device-width, initial-scale=1.0" />
      <title>Document</title>
    </head>
    <body>
      <div class="helloworld">
        {{ msg2 }}
      </div>
    </body>
  </html>
</template>

<script>
export default {
    name: "HelloWorld"
    props: {

        msg: String,
        msg2: String
    }
}
</script>

<style></style>
