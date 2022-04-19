<template>
  <div class="operationGroup">
    <el-button
      size="small"
      @click="toggleSelectAll"
    >{{ data.selectAll ? '' : '取消'}}全选</el-button>
    <el-button
      size="small"
      @click="toggleCollapseStatus"
    >{{ data.collapseStatus ? '展开' : '折叠'}}所有</el-button>
    <el-button
      size="small"
      @click="importWords(allCheckedWords)"
    >导入选中</el-button>
    <el-button
      size="small"
      @click="importWords(uniqueWords)"
    >导入全部</el-button>
    <el-dropdown
      size="small"
      split-button
      @command="handleCommand"
      style="margin-left: 10px;"
    >
      更多
      <template #dropdown>
        <el-dropdown-menu>
          <el-dropdown-item command="remove-known">移除已熟识</el-dropdown-item>
        </el-dropdown-menu>
      </template>
    </el-dropdown>
  </div>
  <el-collapse v-model="data.activeGroups">
    <el-collapse-item
      :title="item.group"
      :name="item.group"
      v-for="(item, key) in data.wordsGroupList"
      :key="key"
    >
      <el-checkbox
        v-model="item.checkAll"
        :indeterminate="item.isIndeterminate"
        @change="handleCheckAllChange(item)"
      >全选</el-checkbox>
      <el-checkbox-group
        v-model="item.checkedWords"
        @change="handleCheckedWordsChange(item)"
      >
        <el-checkbox
          v-for="word in item.words"
          :key="word.word"
          :label="word.word"
          style="width: 150px;"
          :class="{ gray: word.isKnown}"
        >{{
          word.word
        }}</el-checkbox>
      </el-checkbox-group>
    </el-collapse-item>
  </el-collapse>
</template>

<script setup>
import { reactive, defineProps, computed, watch, onMounted } from 'vue'
import store from '@/store/index'
import { add } from '@/api/index'

const props = defineProps({
  words: {
    type: Array,
    required: true,
    default () {
      return []
    }
  },

  defaultGroup: {
    type: String,
    required: false,
    default: 'A'
  }
})

const groupList = [
  'A',
  'B',
  'C',
  'D',
  'E',
  'F',
  'G',
  'H',
  'I',
  'J',
  'K',
  'L',
  'M',
  'N',
  'O',
  'P',
  'Q',
  'R',
  'S',
  'T',
  'U',
  'V',
  'W',
  'X',
  'Y',
  'Z'
]

const data = reactive({
  activeGroups: [], // 展开分组
  originCheckedWords: [], // 初始已熟识的数据
  wordsGroupList: [],
  selectAll: true, // 全选标志
  collapseStatus: true // 折叠标志
})

// 计算所有选中
const allCheckedWords = computed(() => {
  return data.wordsGroupList.reduce((acc, item, index) => {
    return index === 1
      ? acc.checkedWords.concat(item.checkedWords)
      : acc.concat(item.checkedItems)
  })
})

watch(
  () => props.words,
  () => {
    init()
  }
)

onMounted(() => {
  init()
})

// 切换所有全选
const toggleSelectAll = () => {
  for (const item of data.wordsGroupList) {
    item.checkedWords = data.selectAll ? [...item.words] : []
    item.checkAll = data.selectAll
    item.isIndeterminate = false
  }
  data.selectAll = !data.selectAll
}

// 切换分组折叠
const toggleCollapseStatus = () => {
  data.activeGroups = data.collapseStatus ? [...groupList] : []
  data.collapseStatus = !data.collapseStatus
}

const handleCommand = (command) => {
  switch (
    command
    //
  ) {
  }
}

// 分组全选
const handleCheckAllChange = (item) => {
  item.checkedWords = item.checkAll ? [...item.words] : []
  item.isIndeterminate = false
}

// 勾选每项
const handleCheckedWordsChange = (item) => {
  const checkedCount = item.checkedWords.length
  const itemCount = item.words.length
  item.checkAll = checkedCount === itemCount
  item.isIndeterminate = checkedCount > 0 && checkedCount < itemCount
}

// 导入
const importWords = (data) => {
  if (!data.length) {
    alert('请勾选后再操作')
    return
  }
  add({
    user_id: store.state.user_id,
    words: data
  }).then((res) => {
    if (res.code === 200) {
      alert('导入成功')
    }
  })
}

// 按字母分组
const filterWords = (wordsArray, filterStr) => {
  return wordsArray.filter((item) => item.Group === filterStr)
}

// 去重
// const uniqueArray = (arr) =>  {
//   return Array.from(new Set(arr))
// };

const init = () => {
  data.activeGroups = props.defaultGroup.split('')
  // data.uniqueWords = uniqueArray(props.words);
  data.wordsGroupList = []
  data.originCheckedWords = props.words
    .filter((item) => item.isKnown)
    .map((item) => item.word)
  for (let i = 0; i < groupList.length; i++) {
    const tempItem = {
      group: '',
      checkAll: false,
      isIndeterminate: false,
      words: []
    }
    tempItem.group = groupList[i]
    tempItem.words = filterWords(props.words, tempItem.group)
    tempItem.checkedWords = tempItem.words
      .filter((item) => item.isKnown)
      .map((item) => item.word)
    if (tempItem.words.length) {
      data.wordsGroupList.push(tempItem)
    }
  }
}
</script>

<style>
.operationGroup {
  margin-top: 20px;
  margin-bottom: 20px;
  text-align: right;
}

.gray > .is-checked + .el-checkbox__label {
  color: lightgray !important;
}

.gray > .is-checked > .el-checkbox__inner {
  background-color: lightgray !important;
  border-color: lightgray !important;
}
</style>
