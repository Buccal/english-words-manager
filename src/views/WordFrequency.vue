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

  <WordList :data="wordsList"></WordList>
</div>
</template>

<script>
import WordList from "../components/WordList"
import { wordfrequency } from "@/api/index"
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
      if(!this.form.context){
        alert("请输入内容")
        return
      }
      let self = this;
      wordfrequency({
        user_id: localStorage.getItem("user_id"),
        context: this.form.context
      }).then(res => {
        if(res.code === 200){
          self.wordsList = res.data.map(item=>{
            item.newFlag = true;
            return item;
          });
        }
      })
    },
  },
  created() {
  }
}
</script>

<style lang="scss" scoped>
  .wordfrequency{
     text-align: left;
  }
</style>