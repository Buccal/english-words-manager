<template>
  <el-table :data="tableData" :default-sort="{prop: 'frequency', order: 'descending'}">
    <el-table-column label="序号">
      <template v-slot="scope">
        {{scope.$index+1}}
      </template>
    </el-table-column>
    <el-table-column prop="id" label="编号" min-width="250px"></el-table-column>
    <el-table-column prop="word" label="单词" sortable></el-table-column>
    <el-table-column prop="frequency" label="词频" sortable></el-table-column>
    <el-table-column label="是否为生词">
      <template #default="scope">
        <el-switch
            :value="!scope.row.newFlag"
            active-color="#13ce66"
            inactive-color="#ff4949"
            @change="scope.row.newFlag = !$event"
        >
        </el-switch>
      </template>
    </el-table-column>
  </el-table>
</template>

<script>
import axios from 'axios';
export default {
  name: "WordList",
  props: ["data"],
  data(){
    return {
      tableData: JSON.parse(JSON.stringify(this.data)),
    }
  },
  methods: {
  },
}
</script>

<style lang="scss" scoped>
  
</style>