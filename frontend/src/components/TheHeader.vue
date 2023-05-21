<template>
  <header class="header _container  q-electron-drag">
    <div class="header-left">
      <img src="../assets/images/logo.png" alt="logo">
      <nav class="nav">
        <q-btn flat class="link" :class="{ 'link-active': isLinkActive('/') }" to="/">Главная</q-btn>
        <q-btn flat class="link" :class="{ 'link-active': isLinkActive('/sessions') }" to="/sessions">Сессии</q-btn>
        <q-btn flat class="link" :class="{ 'link-active': isLinkActive('/instructions') }"
          to="/instructions">Инструкции</q-btn>
        <q-btn flat class="link" :class="{ 'link-active': isLinkActive('/contacts') }" to="/contacts">Контакты</q-btn>
      </nav>
    </div>
    <div class="menu  q-electron-drag">
      <q-btn class="menu__btn" round flat icon="minimize" @click="minimize" />
      <q-btn class="menu__btn" round flat icon="crop_square" @click="toggleMaximize" />
      <q-btn class="menu__btn" round flat icon="close" @click="closeApp" />
    </div>
  </header>
</template>

<script setup lang='ts'>
import { computed } from 'vue';
import { useRoute } from 'vue-router';
const route = useRoute()

const isLinkActive = computed(() => {
  const path = route.fullPath
  return function (link: string) {
    if (link === path) {
      return true
    } else {
      return false
    }
  }
})

function closeApp () {
  if (process.env.MODE === 'electron') {
    window.myWindowAPI.close()
  }
}

function minimize () {
  if (process.env.MODE === 'electron') {
    window.myWindowAPI.minimize()
  }
}

function toggleMaximize () {
  if (process.env.MODE === 'electron') {
    window.myWindowAPI.toggleMaximize()
  }
}
</script>

<style scoped lang='scss'>
.menu {
  width: 100%;
  display: flex;
  gap: 20px;
  justify-content: flex-end;
}

.menu__btn {
  background: none;
  box-shadow: none;
  border-radius: 100px;
  color: rgb(177, 177, 177);
  cursor: pointer;
  transition: all .3s;

  &:hover {
    color: #fff;
  }
}

.header {
  display: flex;
  // height: 50px;
  padding: 15px 0 10px 0;
  justify-content: space-between;
  align-items: center;
  border-bottom: 1px solid rgba(255, 255, 255, 0.591);
  z-index: 2000;
  background-color: $dark;
}

.header-left {
  height: 100%;
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 20px;
}

.header-right {
  display: flex;
  gap: 20px;
  font-size: 30px;
}

.nav {
  height: 100%;
  display: flex;
  align-items: center;
  gap: 20px;
  font-size: 18px;

  .link {
    display: flex;
    align-items: center;
    height: 100%;
  }

  .link-active {
    background: linear-gradient(0deg, rgba(255, 255, 255, 1) 7%, rgba(0, 212, 255, 0) 7% 100%);
  }
}

.router-link-active {
  border-bottom: 3px solid #fff;
}

.tabs {
  height: 100%;
  display: flex;
  align-items: center;
}

.icon {
  margin: 0 15px;
  padding: 5px;
  font-size: 30px;
  font-weight: 700;
  color: gray;
  transition: all .3s;
  border-radius: 100px;
  cursor: pointer;

  &:hover {
    background-color: rgba(128, 128, 128, 0.5);
    color: #fff;
  }
}
</style>
