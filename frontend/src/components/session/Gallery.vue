<template>
  <div class="gallery" v-if="props.data?.images.length > 0">
    <div class="gallery__main" ref="gallery">
      <InfoCard :data="polygons" />
      <img class="main" ref="image" :src="mainUrl" alt="img" @click="openWindow">
      <Transition>
        <div class="polygon"
          :style="{ top: y, left: x - getLeftMargin + 'px', width: width + 'px', height: height + 'px' }"
          @click="openWindow" v-if="filter.mask">
          <svg width="100%" height="100%">
            <template v-for="(item, idx) in polygons?.gooses">
              <polygon :id="'poly' + idx" :points="points[idx]"
                :style="{ fill: getColor(item.class_name), opacity: 0.4 }">
              </polygon>
            </template>
          </svg>
          <template v-for="(item, idx) in polygons?.gooses">
            <q-tooltip :target="'#poly' + idx" :offset="[0, 0]" class="bg-indigo text-h5">
              {{ getClass(item.class_name) }}
            </q-tooltip>
          </template>
        </div>
      </Transition>
    </div>
    <div class="gallery-scroll">
      <template v-for="(item, idx) in filteredData" v-if="filteredData.length">
        <img class="img-bot" :src="getImageUrl(item.token)" alt="Лебедь"
          :class="{ 'img-selected': item.token === selectedImg }" @click="selectImage(item.token)">
      </template>
      <div class="empty" v-else>По вашему запросу ничего не найдено</div>
    </div>
  </div>
</template>

<script setup lang='ts'>
import InfoCard from './InfoCard.vue'
import { ref, onMounted, onUpdated, computed } from 'vue';
import { useElementBounding, useWindowSize, useResizeObserver } from '@vueuse/core'
import { api } from 'src/boot/axios';

interface IPolygon {
  counts: {
    0: number,
    1: number,
    2: number
  },
  classes: string[]
  size: [number, number],
  gooses: {
    box: [number, number, number, number],
    class_name: 'shipun' | 'maloy' | 'klikun',
    class_id: number
    polygon: [number, number][]
  }[],
}
interface IImage {
  session_id: number,
  name: string,
  creation_datetime: number,
  token: string,
  classes: string
}
interface IData {
  creation_datetime: number,
  desc: string,
  id: number,
  images: IImage[]
}
interface IFilter {
  klikun: boolean,
  shipun: boolean,
  small: boolean,
  mask: boolean
}
interface IProps {
  filter: IFilter,
  data: IData
}
const props = defineProps<IProps>()

const image = ref<HTMLImageElement | null>(null)
const gallery = ref<HTMLDivElement | null>(null)
const mainUrl = ref('')
const polygons = ref<IPolygon>()
const { x, y, width, height } = useElementBounding(image)
const galleryBounding = useElementBounding(gallery)
const screen = useWindowSize()

const baseUrl = 'http://109.248.175.44:8000/'
const imgUrl = baseUrl + 'images/'
const polygonUrl = baseUrl + 'image/'
const points = ref<string[]>([])

useResizeObserver(image, (entries) => {
  points.value = formatPolygons()
})

const filteredData = computed(() => {
  console.log(props.data.images);

  return props.data.images.filter(img => {
    if (props.filter.klikun && img.classes.includes('klikun')) return true
    if (props.filter.shipun && img.classes.includes('shipun')) return true
    if (props.filter.small && img.classes.includes('maloy')) return true
    return false
  })
})

const selectedImg = ref(filteredData.value[0].token)

onMounted(async () => {
  if (props.data) {
    const token = filteredData.value[0].token
    mainUrl.value = imgUrl + token + '.jpg'
    await fetchPolygons(token)
  }
})

onUpdated(async () => {
})

function getClass (className: 'shipun' | 'maloy' | 'klikun') {
  if (className == 'shipun') return 'Лебедь шипун'
  if (className == 'maloy') return 'Малый лебедь'
  if (className == 'klikun') return 'Лебедь кликун'
}

function getColor (className: 'shipun' | 'maloy' | 'klikun') {
  if (className == 'shipun') return 'green'
  if (className == 'maloy') return 'blue'
  if (className == 'klikun') return 'red'
}

async function fetchPolygons (token: string) {
  try {
    const data = await api(polygonUrl + token)
    if (data.status !== 200) throw new Error()
    polygons.value = data.data
    points.value = formatPolygons()
  } catch (error) {
    console.log('Ошибка загрузки полигонов');
  }
}

function formatPolygons () {
  let polyArr: string[] = []

  polygons.value?.gooses.forEach(goose => {
    let polyString = ''
    goose.polygon.forEach(polygon => {
      if (polygon[0] && polygon[1]) {
        // @ts-ignore
        const h = polygon[1] * polygons.value?.size[0]
        // @ts-ignore
        const w = polygon[0] * polygons.value?.size[1]

        const pX = (width.value / polygons.value?.size[1]) * w
        const pY = (height.value / polygons.value?.size[0]) * h
        polyString += Math.round(pX) + ' ' + Math.round(pY) + ', '
      }
    })
    polyArr.push(polyString.slice(0, -2))
  })
  return polyArr
}

function getImageUrl (token: string) {
  return `${imgUrl}${token}.jpg`
}

const getLeftMargin = computed(() => {
  return (screen.width.value - galleryBounding.width.value) / 2
})

async function selectImage (token: string) {
  mainUrl.value = getImageUrl(token)
  selectedImg.value = token
  await fetchPolygons(token)
}

function openWindow () {
  if (process.env.MODE === 'electron') {
    window.myWindowAPI.openImage(mainUrl.value)
  }
}

</script>

<style scoped lang='scss'>
.polygon {
  position: absolute;
}

.gallery {
  width: 100%;
  height: 65vh;
  margin-bottom: 10px;
  display: flex;
  flex-direction: column;
  gap: 60px;
}

.gallery__main {
  position: relative;
  width: 100%;
  height: 60%;
  display: flex;
  gap: 30px;
  justify-content: center;
}

.main__container {
  height: 38vh;
}

.main {
  height: 100%;
  object-fit: cover;
  border: 2px solid $text;
}

.gallery-scroll {
  padding-bottom: 20px;
  display: flex;
  gap: 20px;
  overflow-x: scroll;
  position: relative;
  height: 20vh;
  $scroll-color: #c4c9cc;

  &::-webkit-scrollbar-track {
    border-radius: 8px;
    border: 1px solid rgb(138, 138, 138);
  }

  &::-webkit-scrollbar-thumb {
    border-radius: 8px;
    background-color: $scroll-color;
  }

  &::-webkit-scrollbar-thumb:active {
    background-color: #a5a7a8 !important;
  }

  .img-bot {
    max-width: 300px;
    width: 100%;
    height: 100%;
    object-fit: cover;
    border: 2px solid gray;
    border-radius: 10px;
    cursor: pointer;
  }

  .img-selected {
    border: 2px solid $positive;
  }
}

.empty {
  width: 100%;
  text-align: center;
  font-size: 24px;
}

// transition
.v-enter-from,
.v-leave-to {
  opacity: 0;
  transition: all .3s;
}

.v-enter-to,
.v-leave-from {
  opacity: 1;
  transition: all .3s;
}
</style>
