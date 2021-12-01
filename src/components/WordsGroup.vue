<template>
  <el-button>全选</el-button>
  <el-button @click="">导入选中单词</el-button>
  <el-dropdown split-button type="primary" @click="handleOperation">
    <template #dropdown>
      <el-dropdown-menu>
        <!-- <el-dropdown-item command=""></el-dropdown-item> -->
        <el-dropdown-item command="collapse-all">折叠所有</el-dropdown-item>
        <el-dropdown-item command="expand-all">展开所有</el-dropdown-item>
        <el-dropdown-item command="import-all">导入全部单词</el-dropdown-item>
      </el-dropdown-menu>
    </template>
  </el-dropdown>
  <el-collapse v-model="data.activeGroups">
    <el-collapse-item :title="item.group" :name="item.group" v-for="(item, key) in data.wordsGroupList">
      <el-checkbox
        v-model="item.checkAll"
        :indeterminate="item.isIndeterminate"
        @change="handleCheckAllChange"
        >全选</el-checkbox
      >
      <el-checkbox-group
        v-model="data.checkedWords"
        @change="handleCheckedWordsChange"
      >
        <el-checkbox v-for="word in item.words" :key="word" :label="word">{{
          word
        }}</el-checkbox>
      </el-checkbox-group>
    </el-collapse-item>
  </el-collapse>
</template>

<script setup>
import { reactive, defineProps, watch, onMounted } from 'vue'

const props = defineProps({
  words: {
    type: Array,
    required: true,
    default() {
      return [];
    },
  },

  defaultGroup: {
    type: String,
    required: false,
    default: "",
  },
});

const groupList = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"];

const data = reactive({
  activeGroups: [],
  wordsGroupList: [],
  checkedWords: [],
});


watch(
  () => props.words,
  () => {
    init();
  }
);

onMounted(() => {
  init();
});

const handleOperation = () => {
  //
}

const handleCheckAllChange = () => {
  console.log("all checked");
};

const handleCheckedWordsChange = () => {
  console.log("select changed");
};

const filterWords = (wordsArray, filterStr) => {
  return wordsArray.filter(item => item[0].toUpperCase() === filterStr);
};

const uniqueArray = (arr) =>  {
  return Array.from(new Set(arr))
};

const init = () => {
  data.activeGroups = props.defaultGroup.split("");
  let wordsArray = uniqueArray(props.words);
  data.wordsGroupList = []
  for(let i=0; i<groupList.length; i++){
    let tempItem = {
      group: "",
      checkAll: false,
      isIndeterminate: false,
      words: []
    };
    tempItem.group = groupList[i];
    tempItem.words = filterWords(wordsArray, tempItem.group);
    if(tempItem.words.length){
      data.wordsGroupList.push(tempItem);
    }
  }
};

</script>


