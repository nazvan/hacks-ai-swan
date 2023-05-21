<template>
  <q-dialog ref="dialogRef" @hide="onDialogHide" persistent class="dialog">
    <q-card class="dialog-card q-dialog-plugin">
      <q-card-section class="row items-center">
        <span class="text-h6">Создать новую сессию</span>
      </q-card-section>

      <q-card-section class="q-pt-none">
        <q-input dense v-model="sessionInfo.name" autofocus dark label="Название" />
      </q-card-section>
      <q-card-section class="q-pt-none">
        <q-input dense v-model="sessionInfo.desc" autofocus dark label="Описание" />
      </q-card-section>

      <q-card-actions align="right">
        <q-btn flat label="Отмена" @click="onDialogCancel" />
        <q-btn flat label="Добавить" @click="createSession" :disable="!sessionInfo.name" :loading="isLoading" />
      </q-card-actions>
    </q-card>
  </q-dialog>
</template>

<script setup lang='ts'>
import { reactive, ref } from 'vue';
import { useDialogPluginComponent } from 'quasar';
import { useSessionStore } from 'src/stores/sessionStore';
import { api } from 'src/boot/axios';
defineEmits([...useDialogPluginComponent.emits])
const { dialogRef, onDialogHide, onDialogOK, onDialogCancel } = useDialogPluginComponent()
const sessionInfo = reactive({
  name: '',
  desc: ''
})
const isLoading = ref(false)
const sessionStore = useSessionStore()
async function createSession () {
  try {
    isLoading.value = true
    const data = await api.post('/session', sessionInfo)
    if (data.status !== 200) throw new Error()
    sessionStore.setToLs(data.data.name, data.data.id)
    onDialogOK()
  } catch (error) {
    console.log(error);
  } finally {
    isLoading.value = false
  }
}
</script>

<style scoped lang='scss'>
.text {
  font-size: 20px;
}
</style>
