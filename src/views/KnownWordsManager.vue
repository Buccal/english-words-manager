<template>
<div class="knownWordsManager">
  <WordList :formData="wordsList" :showFrequency="false"></WordList>
</div>
</template>

<script setup>
import { reactive, onMounted } from "vue";
import WordList from "../components/WordList"
import { getKnownWords } from "@/api/index"

let wordsList = reactive([]);

onMounted(() => {
  let user_id = localStorage.getItem("user_id");
  if(!user_id){
    alert("请先登录");
    router.replace({
      path: '/login',
      query: {
        redirect: router.currentRoute.fullPath
      }
    })
  }
  getKnownWords(user_id).then(res => {
    if(res.code === 200) {
      wordsList = res.data.map(item => {
        let temp = {};
        temp.word = item
        temp.newFlag = false
        return temp
      })
    }
  })
});
</script>

<style lang="scss" scoped>

</style>