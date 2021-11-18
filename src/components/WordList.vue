<template>
  <div id="word-list">
    <el-form :model="form" :inline="true" label-width="68px">
      <el-form-item prop="search">
        <el-input v-model="form.search" size="small" placeholder="搜索单词" @keyup.enter.native="search" clearable/>
      </el-form-item>
      <el-form-item v-if="showFrequency">
        <el-button size="small"><el-icon class="el-icon--left"><Collection /></el-icon>保存到生词本</el-button>
        <el-button size="small" @click="saveKnownWords"><el-icon class="el-icon--left"><Plus /></el-icon>添加到熟词库</el-button>
        <el-button size="small" @click="setAllKnown"><el-icon class="el-icon--left"><TurnOff /></el-icon>全部设为熟词</el-button>
      </el-form-item>
      <el-form-item v-if="!showFrequency">
        <el-button size="small" @click="updateKnownWords">保存修改</el-button>
        <el-dropdown @command="handleCommand">
            <el-button type="small">
              导入<el-icon class="el-icon--right"><ArrowDown /></el-icon>
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
    <el-table :data="showData" :default-sort="{prop: 'frequency', order: 'descending'}" border stripe height="250">
      <el-table-column label="序号">
        <template v-slot="scope">
          {{scope.$index+1}}
        </template>
      </el-table-column>
      <el-table-column prop="word" label="单词" sortable></el-table-column>
      <el-table-column prop="frequency" label="词频" v-if="showFrequency" sortable></el-table-column>
      <el-table-column label="是否为生词" prop="newFlag" :filters="[
          { text: '生词', value: true },
          { text: '熟词', value: false },
        ]"
        :filter-method="filterNew"
        filter-placement="bottom-end">
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

<script>
import { ref } from 'vue'
import { add } from "@/api/index"
import { Collection, Plus, TurnOff, ArrowDown } from '@element-plus/icons'
export default {
  name: "WordList",
  props: ["data", "showFrequency"],
  components: {
    Collection,
    Plus,
    TurnOff,
    ArrowDown,
  },
  data(){
    return {
      tableData: [],
      showData: [],
      form: {
        search: "",
      },
      currentPage: 1
    }
  },
  computed:{
    total() {
      return this.tableData.length
    }
  },
  methods: {
    filterNew(value, row) {
      return row.newFlag === value
    },
    saveKnownWords() {
      let words = this.tableData.map(item => {
        if(!item.newFlag){
          return item.word
        }
      });
      if(!words.length){
        alert("请设置熟词")
        return
      }
      add({
        user_id: localStorage.getItem("user_id"),
        words: words
      }).then(res => {
        if(res.code === 200){

        }
      })
    },
    search() {
      if(!this.search){
        alert("请输入单词进行搜索");
        return;
      }
      let self = this;
      this.showData = this.tableData.filter(item => item.word.indexOf(self.search) !== -1);
    },
    setAllKnown(){
      this.showData.map(item=>{
        item.newFlag = false;
        return item;
      })
    },
    handleCurrentChange() {
      this.showData = this.tableData.slice(100*(this.currentPage-1), 100*this.currentPage);
    },
    updateKnownWords() {

    },
    handleCommand(command){
      if(command === "primary" || command === "middle" || command === "high"){

      }else{
        alert("暂不支持")
      }
    },
    init(){
      this.tableData = JSON.parse(JSON.stringify(this.data));
      this.showData = this.tableData.slice(0, 100);
      this.form.search = "";
      this.currentPage = 1;
    },
  },
  watch: {
    data(){
      this.init();
    }
  }
}
</script>

<style lang="scss" scoped>

</style>