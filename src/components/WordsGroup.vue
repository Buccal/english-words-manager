<template>
  <div class="operationGroup">
    <el-button size="small" @click="handleSelectAll">全选</el-button>
    <el-button size="small" @click="handleExpandGroup">展开所有</el-button>
    <el-button size="small" @click="importSelected">导入选中</el-button>
    <el-dropdown size="small" split-button @command="handleCommand" style="margin-left: 10px;">
      更多
      <template #dropdown>
        <el-dropdown-menu>
          <!-- <el-dropdown-item command=""></el-dropdown-item> -->
          <el-dropdown-item command="collapse-all">折叠所有</el-dropdown-item>
          <el-dropdown-item command="import-all">导入全部单词</el-dropdown-item>
        </el-dropdown-menu>
      </template>
    </el-dropdown>
  </div>
  <el-collapse v-model="data.activeGroups">
    <el-collapse-item :title="item.group" :name="item.group" v-for="(item, key) in data.wordsGroupList">
      <el-checkbox
        v-model="item.checkAll"
        :indeterminate="item.isIndeterminate"
        @change="handleCheckAllChange(item)"
        >全选</el-checkbox
      >
      <el-checkbox-group
        v-model="item.checkedWords"
        @change="handleCheckedWordsChange(item)"
      >
        <el-checkbox v-for="word in item.words" :key="word" :label="word" style="width: 150px;">{{
          word
        }}</el-checkbox>
      </el-checkbox-group>
    </el-collapse-item>
  </el-collapse>
</template>

<script setup>
import { reactive, defineProps, computed, watch, onMounted } from 'vue'

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
    default: "A",
  },
});

const groupList = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"];

const data = reactive({
  activeGroups: [],
  uniqueWords: [],
  wordsGroupList: [],
});

const allCheckedWords = computed(() => {
  return data.wordsGroupList.reduce((acc, item, index) => {
    return index === 1
      ? acc.checkedWords.concat(item.checkedWords)
      : acc.concat(item.checkedItems);
  });
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

const handleSelectAll = () => {
  for(let item of data.wordsGroupList){
    item.checkedWords = [...item.words];
    item.checkAll = true;
    item.isIndeterminate = false;
  }
}

const handleExpandGroup = () => {
  data.activeGroups = [...groupList];
}

const importSelected = () => {
  //
}

const handleCommand = (command) => {
  switch (command) {
    case "collapse-all":
      data.activeGroups = [];
      break;
    case "import-all":
      //
      break;
    default:
      // statements_def
      break;
  }
}

const handleCheckAllChange = (item) => {
  item.checkedWords = item.checkAll
    ? [...item.words]
    : [];
  item.isIndeterminate = false;
};

const handleCheckedWordsChange = (item) => {
  let checkedCount = item.checkedWords.length,
    itemCount = item.words.length;
  item.checkAll = checkedCount === itemCount;
  item.isIndeterminate = checkedCount > 0 && checkedCount < itemCount;
};

const filterWords = (wordsArray, filterStr) => {
  return wordsArray.filter(item => item[0].toUpperCase() === filterStr);
};

const uniqueArray = (arr) =>  {
  return Array.from(new Set(arr))
};

const init = () => {
  data.activeGroups = props.defaultGroup.split("");
  data.uniqueWords = uniqueArray(props.words);
  data.wordsGroupList = []
  for(let i=0; i<groupList.length; i++){
    let tempItem = {
      group: "",
      checkAll: false,
      isIndeterminate: false,
      words: [],
      checkedWords: [],
    };
    tempItem.group = groupList[i];
    tempItem.words = filterWords(data.uniqueWords, tempItem.group);
    if(tempItem.words.length){
      data.wordsGroupList.push(tempItem);
    }
  }
};

</script>

<style type="text/css" scoped>
.operationGroup {
  margin-top: 20px;
  margin-bottom: 20px;
  text-align: right;
}
</style>
