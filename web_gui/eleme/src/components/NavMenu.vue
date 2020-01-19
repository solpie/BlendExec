<template>
  <div>
    <el-row>
      <el-page-header @back="goBack" title="BlendExec"> </el-page-header>

      <el-switch
        v-model="is_show_shelf"
        active-color="#13ce66"
        inactive-color="#ff4949"
        @change="on_show_shelf_changed"
      >
      show shelf
      </el-switch>
    </el-row>
  </div>
</template>

<script>
import { api } from "@/api/v1.js";

export default {
  data() {
    return {
      hwnd_arr: [],
      is_show_shelf: true,
      title_hwnd: "no hwnd",
      activeIndex: "1",
      activeIndex2: "1"
    };
  },
  mounted() {
    this.init_nav();
  },
  methods: {
    async init_nav() {
      //   let res = await api.get_hwnd();
      //   console.log("init_nav", res.hwnd_arr);
      //   let a = [];
      //   for (let item of res.hwnd_arr) {
      //     let hwnd = item[0];
      //     let title = item[1];
      //     a.push({ hwnd: hwnd, title: title });
      //   }
      //   if (a.length === 1) {
      //     this.on_sel_hwnd(a[0]);
      //   }
      //   this.hwnd_arr = a;
    },
    on_sel_hwnd(item) {
      api.hwnd = item.hwnd;
      this.title_hwnd = item.title + " | " + item.hwnd;
      console.log("on_sel_hwnd", item.title, item.hwnd);
    },
    on_click_hwnd() {
      console.log("on_click_hwnd");
      this.init_nav();
    },
    on_show_shelf_changed() {
      console.log("on_show_shelf_changed", this.is_show_shelf);
      this.$eventHub.$emit("show_shelf", this.is_show_shelf);
      setTimeout(() => {
        this.$eventHub.$emit("win_resize");
      }, 20);
    },
    goBack() {
      window.location.reload();
    }
  }
};
</script>
