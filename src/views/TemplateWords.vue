<template>
  <div class="templateWords">
    <WordList
      :form-data="data.wordsList"
      :button-list="data.buttonList"
    ></WordList>
  </div>
</template>

<script setup>
import { reactive, defineProps, onMounted } from "vue";
import WordList from "../components/WordList";
import { getTemplateWords } from "@/api/index";

const props = defineProps({
  level: {
    type: String,
    required: true,
    default() {
      return 'primary';
    },
  }
});

const data = reactive({
  wordsList: [],
  buttonList: {
    setAllKnown: true,
    saveModify: true,
  }
});

onMounted(() => {
  getTemplateWords(props.level).then((res) => {
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
