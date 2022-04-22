<template>
  <div class="templateWords">
    <WordsGroup
      :words="data.wordsList"
    ></WordsGroup>
  </div>
</template>

<script setup>
import { reactive, defineProps, onMounted } from 'vue'
import WordsGroup from '../components/WordsGroup'
import store from '@/store/index'
import { getTemplateWords } from '@/api'

const props = defineProps({
  level: {
    type: String,
    required: true,
    default () {
      return 'primary'
    }
  }
})

const data = reactive({
  wordsList: []
})

onMounted(() => {
  getTemplateWords(props.level).then((res) => {
    data.wordsList = res.data.data
  })
})
</script>

<style lang="scss" scoped>
</style>
