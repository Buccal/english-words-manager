<template>
  <div id="word-list">
    <el-form
      :model="form"
      :inline="true"
      label-width="68px"
    >
      <el-form-item prop="search" v-if="data.buttonSetting.searchWord">
        <el-input
          v-model="form.search"
          size="small"
          placeholder="搜索单词"
          @keyup.enter="search"
          clearable
        />
      </el-form-item>
      <el-form-item v-hasPermi="'frequency-operater'">
        <el-button size="small" v-if="data.buttonSetting.newWordBook">
          <el-icon class="el-icon--left">
            <Collection />
          </el-icon>保存到生词本
        </el-button>
        <el-button
          size="small"
          @click="saveKnownWords"
          v-if="data.buttonSetting.setKnown"
        >
          <el-icon class="el-icon--left">
            <Plus />
          </el-icon>添加到熟词库
        </el-button>
        <el-button
          size="small"
          @click="setAllKnown"
          v-if="data.buttonSetting.setAllKnown"
        >
          <el-icon class="el-icon--left">
            <TurnOff />
          </el-icon>全部设为熟词
        </el-button>
        <el-button
          size="small"
          @click="updateKnownWords"
          v-if="data.buttonSetting.saveModify"
        >保存修改</el-button>
        <el-dropdown
          @command="handleCommand"
          v-if="data.buttonSetting.importWord"
        >
          <el-button size="small">
            导入<el-icon class="el-icon--right">
              <ArrowDown />
            </el-icon>
          </el-button>
          <template #dropdown>
            <el-dropdown-menu>
              <el-dropdown-item command="primary">小学大纲词汇</el-dropdown-item>
              <el-dropdown-item command="middle">初中大纲词汇</el-dropdown-item>
              <el-dropdown-item command="high">高中大纲词汇</el-dropdown-item>
              <el-dropdown-item command="cet4">四级大纲词汇</el-dropdown-item>
              <el-dropdown-item command="cet6">六级大纲词汇</el-dropdown-item>
              <el-dropdown-item command="tem4">专四大纲词汇</el-dropdown-item>
              <el-dropdown-item command="tem6">专六大纲词汇</el-dropdown-item>
              <el-dropdown-item command="ielts">雅思大纲词汇</el-dropdown-item>
              <el-dropdown-item command="toefl">托福大纲词汇</el-dropdown-item>
            </el-dropdown-menu>
          </template>
        </el-dropdown>
      </el-form-item>
    </el-form>
    <el-table
      :data="data.showData"
      :default-sort="{prop: 'frequency', order: 'descending'}"
      border
      stripe
    >
      <el-table-column label="序号">
        <template v-slot="scope">
          {{scope.$index+1}}
        </template>
      </el-table-column>
      <el-table-column
        prop="word"
        label="单词"
        sortable
      ></el-table-column>
      <el-table-column
        prop="frequency"
        label="词频"
        v-if="props.showFrequency"
        sortable
      ></el-table-column>
      <el-table-column
        label="是否为生词"
        prop="newFlag"
        :filters="[
          { text: '生词', value: true },
          { text: '熟词', value: false },
        ]"
        :filter-method="filterNew"
        filter-placement="bottom-end"
        v-hasPermi="'frequency-operater'"
      >
        <template #default="scope">
          <el-switch
            v-model="scope.row.newFlag"
            active-color="#13ce66"
            inactive-color="#ff4949"
          >
          </el-switch>
        </template>
      </el-table-column>
    </el-table>
    <el-pagination
      v-model:currentPage="currentPage"
      :page-size="100"
      layout="prev, pager, next, jumper"
      :total="total"
      @current-change="handleCurrentChange"
    >
    </el-pagination>
  </div>
</template>

<script setup>
import { ref, reactive, defineProps, computed, watch, onMounted } from "vue";
import router from "@/router/index.js";
import { add } from "@/api/index";
import { Collection, Plus, TurnOff, ArrowDown } from "@element-plus/icons";

const props = defineProps({
  formData: {
    type: Array,
    required: true,
    default() {
      return [];
    },
  },

  showFrequency: {
    type: Boolean,
    required: false,
    default: false,
  },

  buttonList: {
    type: Object,
    required: false,
    default: {},
  }
});

const currentPage = ref(1);

const defaultButtonList = {
  searchWord: true,
  newWordBook: false,
  setKnown: false,
  setAllKnown: false,
  saveModify: false,
  importWord: false,
};

const data = reactive({
  tableData: [],
  showData: [],
  buttonSetting: {}
});
const form = reactive({
  search: "",
});

const total = computed(() => {
  return data.tableData.length;
});

const filterNew = (value, row) => {
  return row.newFlag === value;
};

const saveKnownWords = () => {
  let words = data.tableData.map((item) => {
    if (!item.newFlag) {
      return item.word;
    }
  });
  if (!words.length) {
    alert("请设置熟词");
    return;
  }
  add({
    user_id: localStorage.getItem("user_id"),
    words: words,
  }).then((res) => {
    if (res.code === 200) {
    }
  });
};

watch(
  () => props.formData,
  () => {
    init();
  }
);

onMounted(() => {
  init();
});

const search = () => {
  if (!search) {
    alert("请输入单词进行搜索");
    return;
  }
  data.showData = data.tableData.filter(
    (item) => item.word.indexOf(search) !== -1
  );
};

const setAllKnown = () => {
  data.showData.map((item) => {
    item.newFlag = false;
    return item;
  });
};

const handleCurrentChange = () => {
  data.showData = data.tableData.slice(
    100 * (currentPage - 1),
    100 * currentPage
  );
};

const updateKnownWords = () => {};

const handleCommand = (command) => {
  if (command === "primary" || command === "middle" || command === "high") {
    router.push('/template-words/' + command);
  } else {
    alert("暂不支持");
  }
};

const init = () => {
  data.tableData = JSON.parse(JSON.stringify(props.formData));
  data.showData = data.tableData.slice(0, 100);
  form.search = "";
  currentPage.value = 1;
  data.buttonSetting = Object.assign({}, defaultButtonList, props.buttonList);
};

</script>

<style lang="scss" scoped>
.operation {
  vertical-align: middle;
}

.el-dropdown {
  margin-left: 5px;

  & .el-button{
    padding: 8px 15px;
  }
}
</style>
