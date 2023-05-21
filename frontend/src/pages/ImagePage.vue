<template>
  <div class="image">
    <q-btn class="menu__btn" round flat icon="close" @click="closeApp" />
    <img :src="url" alt="no">
  </div>
</template>

<script setup lang='ts'>
import { onMounted, ref } from 'vue';
import { useRoute } from 'vue-router';
const route = useRoute()
const url = ref('')
onMounted(() => {
  const id = route.params.id
  url.value = '/placeholder/' + id + '.jpg'
})

function closeApp () {
  if (process.env.MODE === 'electron') {
    window.myWindowAPI.closeImg()
  }
}
</script>

<style scoped lang='scss'>
.image {
  background-color: rgba(128, 128, 128, 0.311);
  position: relative;
}

.menu__btn {
  position: absolute;
  top: 10px;
  right: 10px;
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
</style>
