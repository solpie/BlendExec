<template>
  <div>
    <el-table :data="bpy_script_arr" style="width: 100%">
      <el-table-column label="Name" prop="name"> </el-table-column>
      <el-table-column align="right">
        <template slot="header" slot-scope="scope">
          <el-input size="mini" placeholder="search" />
        </template>
        <template slot-scope="scope">
          <el-button size="mini" @click="on_run(scope.row)">Run</el-button>
          <el-button size="mini" @click="handleDelete(scope.$index, scope.row)"
            >Edit</el-button
          >
        </template>
      </el-table-column>
    </el-table>
  </div>
</template>

<script>
import { api } from "@/api/v1.js";
export default {
  name: "BpyShelf",
  props: {
    msg: String
  },
  mounted() {
    this.init_shelf();
  },
  methods: {
    async init_shelf() {
      let res = await api.get_bpy();
      console.log("init_shelf", res.bpy_arr);
      let a = [];
      for (let item of res.bpy_arr) {
        let name = item[0];
        let path = item[1];
        if (name.search(".py") > -1) {
          a.push({ name: name, path: path });
        }
      }
      this.bpy_script_arr = a;
    },
    on_run(item) {
      //   api.run(item.name)
      api.run_bpy(api.hwnd, item.path);
      console.log("on_run", item);
    }
  },
  data() {
    return {
      bpy_script_arr: ["1", "2"]
    };
  }
};
</script>
