<template>
  <el-table :data="tableData">
    <el-table-column label="序号">
      <template v-slot="scope">
        {{scope.$index+1}}
      </template>
    </el-table-column>
    <el-table-column
      v-for="col in cols"
      :prop="col.prop"
      :label="col.label"
      sortable>
    </el-table-column>

    <el-table-column label="设为生词">
      <template #default="scope">
        <el-switch
            v-model="scope.row.newFlag"
            active-color="#13ce66"
            inactive-color="#ff4949"
            @change="handleStatusChange(scope.row)"
        >
        </el-switch>
      </template>
    </el-table-column>
  </el-table>
</template>

<script>
export default {
  name: "WordList",
  data(){
    return {
      tableData: [{
        word: 'the',
        frequency: 325,
        newFlag: false
      }, {
        word: 'this',
        frequency:24,
        newFlag: false
      }, {
        word: 'that',
        frequency: 151,
        newFlag: false
      }],
      cols: [
        {prop: 'word', label: '单词'},
        {prop: 'frequency', label: '词频'},
      ],
    }
  },
  methods: {
    handleStatusChange(row) {
      console.log(row);
      debugger
    }
  }
}
</script>

<style lang="scss" scoped>
  
</style>