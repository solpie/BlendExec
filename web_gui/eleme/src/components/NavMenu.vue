<template>
  <div>
    <el-menu
      :default-active="activeIndex2"
      mode="horizontal"
      @select="handleSelect"
      @open="on_click_hwnd"
      background-color="#545c64"
      text-color="#fff"
      active-text-color="#ffd04b"
    >
      <el-menu-item index="1">BlendExec</el-menu-item>
      <!-- <el-menu-item index="2"> -->
      <el-submenu index="2">
        <template slot="title">Hwnd</template>
        <el-menu-item
          v-for="(item, i) in hwnd_arr"
          :key="i"
          @click="on_sel_hwnd(item)"
          >{{ item.title }}</el-menu-item
        >
      </el-submenu>
      <!-- </el-menu-item> -->
      <el-menu-item index="3">setting</el-menu-item>
    </el-menu>
  </div>
</template>

<script>
import { api } from "@/api/v1.js";

export default {
  data() {
    return {
      hwnd_arr: [],
      activeIndex: "1",
      activeIndex2: "1"
    };
  },
  mounted() {
    this.init_nav();
  },
  methods: {
    async init_nav() {
      let res = await api.get_hwnd();
      console.log("init_nav", res.hwnd_arr);
      let a = [];
      for (let item of res.hwnd_arr) {
        let hwnd = item[0];
        let title = item[1];
        a.push({ hwnd: hwnd, title: title });
      }
      this.hwnd_arr = a;
    },
    on_sel_hwnd(item) {
      api.hwnd = item.hwnd;
      console.log("on_sel_hwnd", item.title, item.hwnd);
    },
    on_click_hwnd() {
      console.log("on_click_hwnd");
      this.init_nav();
    },
    handleSelect(key, keyPath) {
      console.log(key, keyPath);
    }
  }
};
</script>
