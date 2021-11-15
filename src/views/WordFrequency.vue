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

<!--   <ol>
    <li v-for="(word, index) in wordsList" :key="index">{{word[0]}}：{{word[1]}}</li>
  </ol> -->
  <WordList :data="wordsList"></WordList>
</div>
</template>

<script>
import axios from 'axios';
import WordList from "../components/WordList"
export default {
  components: {
    WordList,
  },
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
      var res = {
        status: 200,
        data: [
        {
          "id": "c080f071662645aa86ee4f5ccfdd0fec",
          "word": "my",
          "frequency": 129
        },
        {
          "id": "389dc497d5f14e11a1df3c317f15f68f",
          "word": "mother",
          "frequency": 10
        },
        {
          "id": "7d58feb6e9004d02a00d406a86e42155",
          "word": "drove",
          "frequency": 2
        },
        {
          "id": "3548670690ff471e977a771b122da6da",
          "word": "me",
          "frequency": 85
        }]
      }
      // axios.post("http://127.0.0.1:8000/wordfrequency", {
      //   context: this.form.context
      // }).then(res=>{
          if(res.status === 200){
            this.wordsList = res.data;
          }
      // })
    
    },
  },
  created() {
    this.onSubmit();
  }
}
</script>

<style lang="scss" scoped>
  .wordfrequency{
     width: 70%;
     margin: 0 auto;
     text-align: left;
  }
</style>