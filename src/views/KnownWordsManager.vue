<template>
  <div class="knownWordsManager">
    <WordList
      :form-data="data.wordsList"
      :button-list="data.buttonList"
    ></WordList>
  </div>
</template>

<script setup>
import { reactive, onMounted } from 'vue'
import store from '@/store/index'
import WordList from '../components/WordList'

const data = reactive({
  wordsList: [],
  buttonList: {
    saveModify: true,
    importWord: true
  }
})

onMounted(() => {
  let temp = [];
  store.state.user.words.forEach(item => {
    temp.push({
      word: item,
      isKnown: true
    })
  })
  data.wordsList = temp
})
</script>

<style lang="scss" scoped>
</style>
