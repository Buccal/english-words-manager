<template>
<div class="knownWordsManager">
  <WordList :data="wordsList" :showFrequency="false"></WordList>
</div>
</template>

<script>
import WordList from "../components/WordList"
import { getKnownWords } from "@/api/index"
export default {
  components: {
    WordList,
  },
  data() {
    return {
      wordsList: [],
    }
  },
  methods: {

  },
  created() {
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
        this.wordsList = res.data.map(item => {
          let temp = {};
          temp.word = item
          temp.newFlag = false
          return temp
        })
      }
    })
  }
}
</script>

<style lang="scss" scoped>

</style>