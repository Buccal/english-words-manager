<template>
  <div class="knownWordsManager">
    <WordList
      :form-data="data.wordsList"
      :button-list="data.buttonList"
    ></WordList>
  </div>
</template>

<script setup>
import { reactive, onMounted } from "vue";
import WordList from "../components/WordList";
import { getKnownWords } from "@/api/index";

const data = reactive({
  wordsList: [],
  buttonList: {
    saveModify: true,
    importWord: true,
  }
});

onMounted(() => {
  let user_id = localStorage.getItem("user_id");
  if (!user_id) {
    alert("请先登录");
    router.replace({
      path: "/login",
      query: {
        redirect: router.currentRoute.fullPath,
      },
    });
  }
  getKnownWords(user_id).then((res) => {
    if (res.code === 200) {
      data.wordsList = res.data.map((item) => {
        let temp = {};
        temp.word = item;
        temp.newFlag = false;
        return temp;
      });
    }
  });
});
</script>

<style lang="scss" scoped>
</style>
