<template>
  <div id="app">
    <el-container>
      <el-header>
        <NavMenu />
      </el-header>
      <el-container style="height:1080px;overflow: hidden;">
        <el-aside v-show="is_show_shelf" style="border: 1px solid #222">
          <BpyShelf />
        </el-aside>
        <el-main style="padding:0px">
          <CharSelector msg="Welcome to Your Vue.js App" />
        </el-main>
      </el-container>
    </el-container>
  </div>
</template>

<script>
import NavMenu from "./components/NavMenu.vue";
import BpyShelf from "./components/BpyShelf";
import CharSelector from "./components/CharSelector";
export default {
  name: "app",
  components: {
    BpyShelf,
    CharSelector,
    NavMenu
  },
  mounted() {
    this.$eventHub.$on("show_shelf", v => {
      this.is_show_shelf = v;
    });
  },
  data() {
    return {
      is_show_shelf: true,
      bpy_script_arr: ["1", "2"]
    };
  }
};
</script>
<style>
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  
  color: #eee;
}
body{
  background: #2b2b2b
}
</style>
