<script setup>
  import LogoutButton from '@/components/molecules/LogoutButton.vue';
  const data = JSON.parse(localStorage.getItem("data"))
</script>

<template>
    <div class="Topbar">
        <div class="item-flex">
            <div class="leftitem-fix">
                <div class="icon-img"><img class="user-picture" :src=iconSrc /></div>
                <div class="user-name">{{ userName }}</div>
            </div>
            <div class="button-fix"><LogoutButton /></div>
        </div>
    </div>
</template>

<script>
  export default {
    data() {
        const data = JSON.parse(localStorage.getItem("data"))
        return {
            iconSrc: data.icon,
            userName: data.name
        }
    }
  }
</script>

<style scoped>
.Topbar {
    height: 80px;
    background-color: white;
    border-bottom: solid 5px #517f9a;
    -webkit-user-select: none;
    -moz-user-select: none;
    -ms-user-select: none;
    user-select: none;
}
.item-flex {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding-top: 5px;
}
.leftitem-fix {
    display: flex;
    align-items: center;
}
.icon-img {
    margin: 0 8px 0 10px;
}
.user-picture {
    width: 60px;
    border-radius: 50%;
    box-sizing: border-box;
    border: solid 1px #f1f1f1;
}
.user-name {
    cursor: default;
}
.button-fix {
    margin: 0 10px;
}
</style>