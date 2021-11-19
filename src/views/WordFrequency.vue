<template>
<div class="wordfrequency">
  <el-form ref="ruleform" :model="form" label-width="120px">
    <el-form-item label="文本：">
      <el-input v-model="form.context" type="textarea" :autosize="{ minRows: 10, maxRows: 20 }"></el-input>
    </el-form-item>
    <el-form-item>
      <el-button type="primary" @click="onSubmit">计算词频</el-button>
    </el-form-item>
  </el-form>
  <WordList :formData="data.wordsList" :showFrequency="flag"></WordList>
</div>
</template>

<script setup>
import { ref, reactive } from "vue";
import WordList from "../components/WordList"
import { wordfrequency } from "@/api/index"

const ruleform = ref(null);

const form = reactive({
  context: "",
})

const data = reactive({
  wordsList: []
});

let flag = ref(true)

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
      data.wordsList = res.data.map(item=>{
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