import { defineStore } from 'pinia'
import { ref, reactive } from 'vue'

export const useSessionStore = defineStore('session', () => {
  const session = reactive({
    name: '',
    id: null
  })
  const sessionLoading = ref(false)
  function $reset () {
    session.name = ''
    session.id = null
    localStorage.clear()
  }

  function getFromLs() {
    const name = localStorage.getItem('session_name')
    const id = localStorage.getItem('session_id')
    if (name && id) {
      // @ts-ignore
      session.id = id
      session.name = name
    }
  }

  function setToLs(name: string, id: number) {
    localStorage.setItem('session_name', name)
    localStorage.setItem('session_id', id.toString())
    // @ts-ignore
    session.id = id
    session.name = name
  }

  return { session, $reset, sessionLoading, getFromLs, setToLs }
})
