<template>
  <div>
    <el-table :data="bpy_script_arr" style="width: 100%">
      <el-table-column label="Date" prop="date"> </el-table-column>
      <el-table-column label="Name" prop="name"> </el-table-column>
      <el-table-column align="right">
        <template slot="header" slot-scope="scope">
          <el-input v-model="search" size="mini" placeholder="输入关键字搜索" />
        </template>
        <template slot-scope="scope">
          <el-button size="mini" @click="handleEdit(scope.$index, scope.row)"
            >Edit</el-button
          >
          <el-button
            size="mini"
            @click="handleDelete(scope.$index, scope.row)"
            >save</el-button
          >
        </template>
      </el-table-column>
    </el-table>
  </div>
</template>

<script>
export default {
  name: 'BpyShelf',
  props: {
    msg: String
  }
  ,data() {
    return {
      bpy_script_arr: ["1", "2"]
    };
  }
}
</script>

