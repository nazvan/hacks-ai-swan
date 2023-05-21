import CloseSessionDialog from 'src/components/dialogs/CloseSessionDialog.vue';
import SaveSessionDialog from 'src/components/dialogs/SaveSessionDialog.vue';
import LoadSessionDialog from 'src/components/dialogs/LoadSessionDialog.vue';
import { useQuasar } from 'quasar';
import { useImageStore } from 'src/stores/imageStore';
import { useSessionStore } from 'src/stores/sessionStore';

type TypeDialog = 'close' | 'save' | 'load'

export const useDialog = (type: TypeDialog) => {
  const $q = useQuasar()
  const imageStore = useImageStore()
  function close() {
    $q.dialog({
      component: CloseSessionDialog
    }).onOk(() => {
      imageStore.$reset()
    }).onCancel(() => {
    })
  }

  function save() {
    $q.dialog({
      component: SaveSessionDialog
    }).onOk(() => {

    }).onCancel(() => {

    })
  }

  function load() {
    $q.dialog({
      component: LoadSessionDialog
    }).onOk(() => {
    }).onCancel(() => {
    })
  }

  if (type === 'close') return close
  if (type === 'save') return save
  if (type === 'load') return load
}
