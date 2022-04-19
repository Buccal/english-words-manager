<template>
  <div class="wordFrequency">
    <el-form
      ref="ruleForm"
      :model="form"
      label-width="120px"
      label-position="top"
    >
      <el-form-item label="文本：">
        <el-input
          v-model="form.context"
          type="textarea"
          :autosize="{ minRows: 10, maxRows: 20 }"
        ></el-input>
      </el-form-item>
      <el-form-item>
        <el-button
          type="primary"
          @click="onSubmit"
        >计算词频</el-button>
      </el-form-item>
    </el-form>
    <WordList
      :form-data="data.wordsList"
      :show-frequency="true"
      :button-list="data.buttonList"
    ></WordList>
  </div>
</template>

<script setup>
import { ref, reactive } from 'vue'
import store from '@/store/index'
import WordList from '../components/WordList'
import { wordFrequency } from '@/api'

const ruleForm = ref(null)

const form = reactive({
  context: ''
})

const data = reactive({
  wordsList: [],
  buttonList: {
    newWordBook: true,
    setKnown: true,
    setAllKnown: true
  }
})

const onSubmit = () => {
  if (!form.context) {
    alert('请输入内容')
    return
  }
  wordFrequency({
    content: form.context.replace(/\n/, " ")
  }).then((res) => {
    if (res.code === 200) {
      data.wordsList = res.data
    }
  })
}
</script>

<style lang="scss" scoped>
</style>
