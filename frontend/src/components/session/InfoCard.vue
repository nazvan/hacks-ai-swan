<template>
  <div class="info" v-if="props.data?.counts">
    <div class="info__item">
      <div class="title">Всего лебедей:</div>
      <div class="subtilte">{{ getBirdsCount }}</div>
    </div>
    <div class="info__item">
      <div class="title">Лебедь шипун:</div>
      <div class="subtilte">{{ props.data.counts[1] }}</div>
    </div>
    <div class="info__item">
      <div class="title">Лебедь кликун:</div>
      <div class="subtilte">{{ props.data.counts[0] }}</div>
    </div>
    <div class="info__item">
      <div class="title">Малый лебедь:</div>
      <div class="subtilte">{{ props.data.counts[2] }}</div>
    </div>
  </div>
</template>

<script setup lang='ts'>
import { onMounted, computed } from 'vue';
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
const props = defineProps<{
  data: IPolygon
}>()

const getBirdsCount = computed(() => {
  return props.data.counts[0] + props.data.counts[1] + props.data.counts[2]
})

</script>

<style scoped lang='scss'>
.info {
  position: absolute;
  left: 0;
  height: 100%;
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.subtilte {
  width: 100%;
  max-width: 100px;
  text-align: center;
  color: $primary;
  font-size: 20px;
  font-weight: 700;
  text-overflow: ellipsis;
  overflow: hidden;
}
</style>
