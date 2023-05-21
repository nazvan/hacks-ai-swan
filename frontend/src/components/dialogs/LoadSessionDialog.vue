<template>
  <q-dialog ref="dialogRef" @hide="onDialogHide" persistent class="dialog">
    <q-card class="dialog-card q-dialog-plugin">
      <q-card-section class="row items-center">
        <span class="text-h6">Открыть сессию</span>
      </q-card-section>

      <q-card-section class="q-pt-none sessions__container">
        <q-spinner color="primary" size="3em" v-if="isLoading" />
        <div class="sessions__list">
          <span v-if="!sessions.length">Вы еще не сохранили сессий</span>
          <q-table :rows="sessions" :columns="columns" row-key="id" flat dark class="transparent text-h5" hide-pagination
            :filter="filter" virtual-scroll :rows-per-page-options="[0]" style="height: 400px"
            v-model:pagination="pagination" @row-click="(e, row) => getSession(row.id)" v-else>
            <template v-slot:top-right>
              <q-input dark borderless dense debounce="300" v-model="filter" placeholder="Поиск">
                <template v-slot:append>
                  <q-icon name="search" />
                </template>
              </q-input>
            </template>
            <template #no-data>
              <p>По Вашему запросу ничего не найдено</p>
            </template>
          </q-table>
        </div>
      </q-card-section>

      <q-card-actions align="right">
        <q-spinner color="primary" size="3em" v-if="loadingSelectedSession" />
        <q-btn flat label="Отмена" @click="onDialogCancel" v-else />
      </q-card-actions>
    </q-card>
  </q-dialog>
</template>

<script setup lang='ts'>
import { ref, onMounted } from 'vue';
import { useDialogPluginComponent } from 'quasar';
import { api } from 'src/boot/axios';
import { IFetchSession } from 'src/types/session'
import { useSessionStore } from 'src/stores/sessionStore';

const $emit = defineEmits([...useDialogPluginComponent.emits, 'reload'])
const { dialogRef, onDialogHide, onDialogOK, onDialogCancel } = useDialogPluginComponent()
const sessions = ref<IFetchSession[]>([])
const isLoading = ref(false)
const loadingSelectedSession = ref(false)
const sessionStore = useSessionStore()
const filter = ref('')
const pagination = ref({ rowsPerPage: 0 })

const columns = [
  { name: 'name', label: 'Навзание', field: 'name', align: 'left', sortable: true },
  { name: 'creation_datetime', label: 'Дата создания', field: 'creation_datetime', align: 'right', format: val => formatDate(val), sortable: true },
]

onMounted(async () => {
  try {
    isLoading.value = true
    const data = await api('/session')
    sessions.value = data.data
  } catch (error) {
    console.log('Ошибка загрузки сессий');
  } finally {
    isLoading.value = false
  }
})

async function getSession (id: number) {
  try {
    loadingSelectedSession.value = true
    const data = await api('/session/' + id)
    sessionStore.setToLs(data.data.name, data.data.id)
    $emit('reload')
    onDialogOK()
  } catch (error) {
    console.log("Ошибка загрузки сессии с id: " + id);
  } finally {
    loadingSelectedSession.value = false
  }
}

function formatDate (dateUnix: number) {
  const date = new Date(dateUnix * 1000)
  const foramtedDate = date.toLocaleDateString('ru-Ru')
  const time = date.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })
  return foramtedDate + ' ' + time
}

</script>

<style scoped lang='scss'>
.sessions__container {
  display: flex;
  justify-content: center;
}

.text {
  font-size: 20px;
}

.sessions__list {
  width: 100%;
}

.table {
  background-color: transparent;
}

.session {
  width: 100%;
  height: 50px;
  padding: 0 15px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  transition: all .3s;
  cursor: pointer;

  &:hover {
    background-color: rgba(128, 128, 128, 0.559);
  }
}
</style>
