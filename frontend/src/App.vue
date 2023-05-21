<template>
  <main-layout v-if="useLayout" />
  <router-view v-else />
</template>

<script setup lang="ts">
import { onMounted, ref } from 'vue';
import { useRoute } from 'vue-router';
import MainLayout from './layouts/MainLayout.vue';
import { useSessionStore } from './stores/sessionStore';
const sessionStore = useSessionStore()
const route = useRoute()
const useLayout = ref(true)

onMounted(() => {
  sessionStore.getFromLs()
  if (route.meta.emptyLayout) {
    useLayout.value = false
  }
})
</script>
