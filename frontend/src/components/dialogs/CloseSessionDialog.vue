<template>
  <q-dialog ref="dialogRef" @hide="onDialogHide" persistent class="dialog">
    <q-card class="dialog-card q-dialog-plugin">
      <q-card-section class="row items-center">
        <span class="text">Вы уверены, что хотите закрыть сессию?</span>
      </q-card-section>

      <q-card-actions align="right">
        <q-btn flat label="Нет" @click="onDialogCancel" />
        <q-btn flat label="Да" @click="onDialogOK" />
      </q-card-actions>
    </q-card>
  </q-dialog>
</template>

<script setup lang='ts'>
import { useDialogPluginComponent } from 'quasar';
defineEmits([...useDialogPluginComponent.emits])
const { dialogRef, onDialogHide, onDialogOK, onDialogCancel } = useDialogPluginComponent()
</script>

<style scoped lang='scss'>
.text {
  font-size: 20px;
}
</style>
