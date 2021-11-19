<template>
<div class="wordfrequency">
  <el-form ref="form" :model="form" label-width="120px">
    <el-form-item label="文本：">
      <el-input v-model="form.context" type="textarea" :autosize="{ minRows: 10, maxRows: 20 }"></el-input>
    </el-form-item>
    <el-form-item>
      <el-button type="primary" @click="onSubmit">计算词频</el-button>
    </el-form-item>
  </el-form>

  <WordList :data="wordsList" :showFrequency="true"></WordList>
</div>
</template>

<script setup>
import { reactive } from "vue";
import WordList from "../components/WordList"
import { wordfrequency } from "@/api/index"

const form = reactive({
  context: "",
})

const wordsList = reactive([]);

const onSubmit = () => {
  if(!form.context){
    alert("请输入内容")
    return
  }
  wordfrequency({
    user_id: localStorage.getItem("user_id"),
    context: form.context
  }).then(res => {
    if(res.code === 200){
      wordsList = res.data.map(item=>{
        item.newFlag = true;
        return item;
      });
    }
  })
}
</script>

<style lang="scss" scoped>
  .wordfrequency{
     text-align: left;
  }
</style>