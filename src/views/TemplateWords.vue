<template>
  <div class="templateWords">
    <WordList :form-data="data.wordsList"></WordList>
  </div>
</template>

<script setup>
import { reactive, onMounted } from "vue";
import WordList from "../components/WordList";
import { getTemplateWords } from "@/api/index";

const data = reactive({
  wordsList: [],
});

onMounted(() => {
  getTemplateWords(user_id).then((res) => {
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
