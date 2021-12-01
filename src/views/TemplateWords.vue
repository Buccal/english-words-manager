<template>
  <div class="templateWords">
    <WordsGroup
      :words="data.wordsList"
    ></WordsGroup>
  </div>
</template>

<script setup>
import { reactive, defineProps, onMounted } from "vue";
import WordsGroup from "../components/WordsGroup";
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
});

onMounted(() => {
  getTemplateWords(props.level).then((res) => {
    if (res.code === 200) {
      data.wordsList = res.data;
    }
  });
});
</script>

<style lang="scss" scoped>
</style>
