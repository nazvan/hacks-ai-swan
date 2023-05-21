import { defineStore } from 'pinia'
import { ref } from 'vue'

export const useImageStore = defineStore('images', () => {
  const files = ref<File[]>([])
  function $reset () {
    files.value = []
  }

  return { files, $reset }
})
