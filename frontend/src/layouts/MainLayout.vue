<template>
  <div class="wrapper">
    <TheHeader class="header" />
    <main class="main _container">
      <router-view v-slot="{ Component }">
        <transition name="fade" mode="out-in">
          <component :is="Component" />
        </transition>
      </router-view>
    </main>
  </div>
</template>

<script setup lang="ts">
import TheHeader from 'src/components/TheHeader.vue';
</script>

<style scoped lang="scss">
.wrapper {
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  align-items: center;
  // background: url('../assets/images/main.jpg');
  background-position: center;
  background-repeat: no-repeat;
  background-size: cover;
}

.main {
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
}

.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.3s;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
</style>
