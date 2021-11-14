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

  <ol>
    <li v-for="(word, index) in wordsList" :key="index">{{word[0]}}：{{word[1]}}</li>
  </ol>
</div>
</template>

<script>
import axios from 'axios';
export default {
  data() {
    return {
      form: {
        context: "",
      },
      wordsList: [],
    }
  },
  methods: {
    onSubmit() {
      axios.post("http://127.0.0.1:8000/wordfrequency", {
        context: this.form.context
      }).then(res=>{
          if(res.status === 200){
            // this.wordsList = res.data.slice(0, 10);
            this.wordsList = res.data;
          }
      })
    },
  },
}
</script>

<style lang="scss" scoped>
  .wordfrequency{
     width: 70%;
     margin: 0 auto;
     text-align: left;
  }
</style>