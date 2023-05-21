<template>
  <div class="session_container">
    <div class="session__actions">
      <div class="actions__main">
        <q-btn color="primary" icon="note_add" label="Новая сессия" @click="saveDialog" />
        <q-btn color="primary" icon="folder" label="Открыть сессию" @click="loadDialog" />
        <q-btn color="primary" icon="add" label="Добавить изображения" @click="fileInput?.click()"
          v-if="sessionStore.session.id" />
        <input ref="fileInput" type="file" accept="image/*" multiple class="input" id="fileInput"
          @change="filesHandler" />
      </div>
      <div class="actions__name">
        <p>{{ sessionStore.session.name }}</p>
      </div>
      <div class="actions__close" v-if="sessionStore.session.id">
        <q-btn round icon="close" @click="sessionStore.$reset" />
      </div>
    </div>
    <div class="loader" v-if="isLoading">
      <q-spinner color="primary" size="5em" />
      <p v-if="refetchData">Идет обработка изображений. Пожалуйста, подождите</p>
    </div>
    <div class="session" v-else-if="sessionStore.session.id && fetchedData">
      <div class="session__filter" v-if="fetchedData?.images?.length > 0">
        <h5>Фильтр:</h5>
        <q-checkbox v-model="filter.shipun" dark label="Лебедь шипун" />
        <q-checkbox v-model="filter.klikun" dark label="Лебедь кликун" />
        <q-checkbox v-model="filter.small" dark label="Малый лебедь" />
        <q-toggle v-model="filter.mask" color="primary" :label="filter.mask ? 'Маска включена' : 'Маска отключена'" />
      </div>
      <Gallery :filter="filter" :data="fetchedData" v-if="fetchedData?.images?.length > 0" />
      <div class="empty" v-else>Добавте изображения для обработки</div>
    </div>
  </div>
</template>

<script setup lang='ts'>
import Gallery from 'src/components/session/Gallery.vue';
import LoadSessionDialog from 'src/components/dialogs/LoadSessionDialog.vue';
import SaveSessionDialog from 'src/components/dialogs/SaveSessionDialog.vue';
import { ref, reactive, onMounted } from 'vue';
import { useQuasar } from 'quasar';
import { useDialog } from 'src/composables/useDialog'
import { useSessionStore } from 'src/stores/sessionStore';
import { api } from 'src/boot/axios';
import { IFetchSession } from 'src/types/session';

const $q = useQuasar()

function saveDialog () {
  $q.dialog({
    component: SaveSessionDialog
  }).onOk(async () => {
    await fetchData()
  }).onCancel(() => { })
}

function loadDialog () {
  $q.dialog({
    component: LoadSessionDialog
  }).onOk(async () => {
    await fetchData()
  }).onCancel(() => { })
}

const fileInput = ref<HTMLInputElement | null>(null)
const sessionStore = useSessionStore()
const isLoading = ref(false)
const refetchData = ref(false)
const fetchedData = ref<IFetchSession>()

const filter = reactive({
  shipun: true,
  klikun: true,
  small: true,
  mask: true
})

onMounted(async () => {
  await fetchData()
})

async function fetchData (refetch = false) {
  try {
    isLoading.value = true
    if (refetch) refetchData.value = true
    const id = sessionStore.session.id
    if (!id) return
    const data = await api('/session/' + id)
    if (data.status !== 200) throw new Error()
    fetchedData.value = data.data
    if (!fetchedData.value) throw new Error()
    if (sessionStore.session.id != fetchedData.value.id) {
      sessionStore.setToLs(fetchedData.value.name, fetchedData.value.id)
    }
    console.log('fetched');
  } catch (error) {
    console.log('fetch error');
  } finally {
    isLoading.value = false
    refetchData.value = false
  }
}

async function filesHandler () {
  if (fileInput.value && fileInput.value.files?.length) {
    try {
      isLoading.value = true
      refetchData.value = true
      const formData = new FormData()
      for (let i = 0; i < fileInput.value.files.length; i++) {
        const file = fileInput.value.files[i]
        formData.append('images', file)
      }
      const data = await api.post('/image/upload', formData, {
        params: {
          id: sessionStore.session.id
        },
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      })
      if (data.status !== 200) throw new Error()
      await fetchData(true)
    } catch (error) {
      console.log('ошибка загрузки файлов');
      console.log(error);
    } finally {
      isLoading.value = false
    }
  }
}

</script>

<style scoped lang='scss'>
.session_container {
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
}

.session__actions {
  width: 100%;
  padding-top: 20px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.actions__main {
  display: flex;
  gap: 20px;
}

.session {
  margin: 20px 0;
  flex-grow: 1;
}


.session__filter {
  margin-bottom: 20px;
  display: flex;
  align-items: center;
  gap: 20px;
}

.counter {
  display: inline-block;
  background: #fff;
  border-radius: 100px;
  height: 30px;
  width: 30px;
  color: #000;
}

.input {
  display: none;
}

.session__images {
  max-height: 800px;
  padding-bottom: 20px;
  display: flex;
  flex-wrap: wrap;
  gap: 50px;
  overflow-y: scroll;
  overflow-x: hidden;
}

.actions__name {
  font-size: 24px;

  p {
    text-shadow: 0 0 10px rgb(0, 0, 0);
  }
}

.loader {
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  gap: 20px;
}

.empty {
  font-size: 24px;
}
</style>
